#!/usr/bin/python
import math
import time
import ephem
import os
from datetime import datetime
from process import makestuff

def	readfile(fil):
	
	f = open(fil, 'r')
	return f.read()

#
# test suite
#

makestuff()

satelit = []
visiblesats = []

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
		satelit.append(ephem.readtle(sat[0],sat[1],sat[2]))
		
for sat in satelit:
	home.date = datetime.utcnow()
	sat.compute(home)
	
	if sat.alt > min_alt and sat.alt < 80:
		print sat.name, " is visible"
		visiblesats.append(sat)
		
		
  
