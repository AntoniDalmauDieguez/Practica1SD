#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
import commands

numMapers=4

if __name__ == '__main__':
	set_context()
	
	i=0
	while i<numMapers:
		maper=create_host('http://127.0.0.1:600'+str(i))
		r = maper.lookup_url('http://127.0.0.1:5000/regis', 'Registry', 'registry')
		r.subscribe(maper)
		i=i+1

	serve_forever()
