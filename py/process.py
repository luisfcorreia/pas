#!/usr/bin/python

def	readfile(fil):
	
	with open(fil, 'r') as f:
		d1 = f.readline()
		d2 = f.readline()
		d3 = f.readline()
		
		data = d1 + '|' + d3 + '|' + d3
		print data


readfile('gps-ops.txt')


