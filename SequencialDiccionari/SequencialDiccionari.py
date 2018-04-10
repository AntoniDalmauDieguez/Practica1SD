#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from collections import Counter
from time import time
import re

class Maper(object):
	_tell = ['execute']
	_ask = []
	_ref =['execute']
	def execute(self, red):
		with open('Sherlock70.txt') as f:
			s=f.read()
			red.reducer(countWords(s))

class Reducer(object):
	_tell = ['reducer']
	_ask = []
	def __init__(self):
		self.diccionariFinal = {}
		self.num=0
		
	def reducer(self, diccionari):
		self.diccionariFinal=Counter(self.diccionariFinal)+Counter(diccionari)
		self.num=self.num+1
		
		if self.num==1:
			tempsf=time()
			print "Temps d'execucio: "+str(tempsf-tempsi)
			print self.diccionariFinal
				
def countWords(s):
	#Canviem tots els caracters que no siguin lletres, numeros o ' per espais en blanc
	s= re.sub('[.,;:_¿?!"·$%&/()\{}@#¬^<>]', ' ', s).replace('-', ' ')
	words=s.split()
	diccionari={}
	for word in words:
		if(diccionari.get(word))==None:
			diccionari[word]=1
		else:
			diccionari[word]=diccionari[word]+1
	return diccionari
	
if __name__ == '__main__':
	set_context()
	tempsi=time()
	#Creem master
	master = create_host()
	#Creem maper
	maper=master.spawn('maper', Maper)
	#Creem reducer
	red=master.spawn('reducer', Reducer)
	
	maper.execute(red)
		
	serve_forever()
