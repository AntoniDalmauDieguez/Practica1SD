#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from collections import Counter
from time import time
import commands

numMapers=4

class Maper(object):
	_tell = ['execute']
	_ask = []
	_ref =['execute']
	def execute(self, i, red, t):
		#Descarreguem del HTTPServer el fitxer corresponent
		commands.getoutput("wget 'http://127.0.0.1:8000/small_file_"+str(i)+".txt'")
		with open('small_file_'+str(i)+".txt", 'r') as f:
			#Llegim el contingut del fitxer
			s=f.read()
			red.reducer(wordCount(s), t)
		commands.getoutput("rm 'small_file_"+str(i)+".txt'")
		
def wordCount(s):
	return len(s.split())
					
class Reducer(object):
	_tell = ['reducer']
	_ask = []
	def __init__(self):
		self.x=0
		self.num=0
		
	def reducer(self, diccionari, t):
		self.x=self.x+diccionari
		self.num=self.num+1
		
		if self.num==numMapers:
			tempsf=time()
			print "Temps d'execucio: "+str(tempsf-t)
			print "Numero de paraules: "+str(self.x)

if __name__ == '__main__':
	set_context()
	tempsi=time()
	#Creem master
	master = create_host('http://127.0.0.1:1234/')
	#Busquem el registry
	r=master.lookup_url('http://127.0.0.1:5000/regis', 'Registry', 'registry')
	#Creem el Reducer
	red=master.spawn('red', 'server/Reducer')

	#Executem els mapers
	i=0
	while i<numMapers:
		i=i+1
		#Executem els mapers per obtenir els diccionaris i els reduim amb el Reducer
		r.getMapers()[i-1].spawn('maper'+str(i), 'server/Maper').execute(i, red, tempsi)

	serve_forever()
