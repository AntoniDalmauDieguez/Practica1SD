#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from collections import Counter
from itertools import izip_longest

numMapers=4

class Registry(object):
	_tell = ['subscribe']
	_ask = ['getMapers']
	_ref = ['subscribe', 'getMapers']   
	
	def __init__(self):
		self.l = []
		
	def subscribe(self, maper):
		print maper
		self.l.append(maper)
	
	def getMapers(self):
		return self.l

if __name__ == '__main__':
	set_context()
	
	host = create_host('http://127.0.0.1:5000/')
	registry = host.spawn('regis', Registry)
	print 'Registry listening at port 5000'

	serve_forever()
