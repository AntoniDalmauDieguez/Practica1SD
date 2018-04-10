#!/usr/bin/env 
#-*- coding: utf-8 -*-
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
import commands

if __name__ == '__main__':
	
	set_context()
	maper=create_host('http://127.0.0.1:6002')
	r = maper.lookup_url('http://127.0.0.1:5000/regis', 'Registry', 'registry')
	r.subscribe(maper)

	serve_forever()
