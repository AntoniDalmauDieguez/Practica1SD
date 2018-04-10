'''
master: divide los datos entre el numero de mapers
	-maper: word count, mira cada linia i de cada balabra crea un diccionario con indice la palabra i valor el numero de 
	veces que aparece
	-maper
	-maper

	->le mandan al reducer para que haga el calculo final (solo hay un reducer)
count words:contar palabras
word count:cuantas veces aparece cada palabra, crea un diccionario con un string como clave i el numero de veces que 
aparece como valor

1.El master coje el fichero y lo particiona segun el numero de mapers
2.Cada maper procesa su parte y cuando tengan el resultado lo mandan al reducer
'''
#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from collections import Counter
from time import time

class Maper(object):
	_tell = ['execute']
	_ask = []
	_ref =['execute']
	def execute(self, red):
		with open('Sherlock.txt') as f:
			s=f.read()
			red.reducer(wordCount(s))

class Reducer(object):
	_tell = ['reducer']
	_ask = []
	def __init__(self):
		self.x=0
		
	def reducer(self, diccionari):
		self.x=self.x+diccionari

		tempsf=time()
		print "Temps d'execucio: "+str(tempsf-tempsi)
		print "Numero de paraules: "+str(self.x)
				
def wordCount(s):
	return len(s.split())
	
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
