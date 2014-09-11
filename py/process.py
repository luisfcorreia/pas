#!/usr/bin/python

def	readfile(fil):
	
	data = ""
	f = open(fil, 'r')
	# read stuff from file
	while True:
		d1 = f.readline().strip()
		d2 = f.readline().strip()
		d3 = f.readline().strip()
		
		# idiotic EOF test
		if not d3:
			break
		
		# get only our beloved satellites
		if ('GPS' in d1) or ('HISPASAT' in d1) or ('ISS' in d1):
			data += d1 + "|" + d2 + "|" + d3 + "*"

	# return large string with data
	return data


#
# test suite
#
coisas  = ""
coisas += readfile('gps-ops.txt')
coisas += readfile('geo.txt')
coisas += readfile('stations.txt')

print coisas

