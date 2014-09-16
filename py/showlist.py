#!/usr/bin/python
import math
import time
import ephem
import os
from datetime import datetime


def	readfile(fil):
	
	f = open(fil, 'r')
	return f.read()

#
# test suite
#

satelites = []

# This is Lisbon, Portugal
home = ephem.Observer()
home.lon = '-9.9'   # +E
home.lat = '34.44'      # +N
home.elevation = 10 # meters 


satt = readfile('sats.txt')
sats = satt.split('*')
min_alt = 10. * math.pi / 180.

for tle in sats:
	sat = tle.split('|')
	#print ' satelite ' +sat[0]
	if sat[0] != '':
		satelites.append(ephem.readtle(sat[0],sat[1],sat[2]))
		
		
for sat in satelites:
	home.date = datetime.utcnow()
	sat.compute(home)
	if sat.alt > min_alt:
		print sat.name, " is visible"
  
