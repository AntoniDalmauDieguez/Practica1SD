#!/usr/bin/env 
#-*- coding: utf-8 -*-
import SimpleHTTPServer
import SocketServer
from itertools import izip_longest
from time import time
numMapers=4

def grouper(n, iterable, fillvalue=None):
	"Collect data into fixed-length chunks or blocks"
	#grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
	args = [iter(iterable)] * n
	return izip_longest(fillvalue=fillvalue, *args)
	
if __name__ == '__main__':
	timei=time()
	#Contem el nombre de linies del fitxer
	with open('Sherlock.txt') as f:
		n=len(f.readlines())
		n=(n/numMapers)+1
		
	#Dividim el fitxer en subfitxers
	with open('Sherlock.txt') as f:
		for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
			with open('small_file_{0}.txt'.format(i), 'w') as fout:
				fout.writelines(g)

	PORT = 8000
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

	httpd = SocketServer.TCPServer(("", PORT), Handler)
	timef=time()
	print 'Temps: '+str(timef-timei)
	print "serving at port", PORT
	httpd.serve_forever()
