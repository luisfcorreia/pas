#!/usr/bin/python

import math
import time
import ephem
import os
from datetime import datetime
from process import makestuff

def get_them(name,cnt):

	count = 0		
	for gps in visiblesats:
		if name in gps.name:
			plist.append(gps)
			count += 1
			if count==cnt:
				break

satelit = []
visiblesats = []
plist = []
min_alt = 10. * math.pi / 180.

# This is Lisbon, Portugal
home = ephem.Observer()
home.lon = '-9.9'   # +E
home.lat = '34.44'      # +N
home.elevation = 10 # meters 

satt = makestuff()
sats = satt.split('*')

for tle in sats:
	sat = tle.split('|')
	if sat[0] != '':
		satelit.append(ephem.readtle(sat[0],sat[1],sat[2]))
		
for sat in satelit:
	home.date = datetime.utcnow()
	sat.compute(home)
	
	if sat.alt > 0.174532925199:
		#print sat.name, " is visible ", sat.range , " ", sat.alt
		visiblesats.append(sat)

# filter hoe many we want
get_them('GPS',1)
get_them('COS',1)
get_them('IRI',2)
get_them('HIS',1)

f = open('list.txt','w')

for sat in plist:
	for tle in sats:
		sat1 = tle.split('|')
		if sat1[0] == sat.name:
			f.write(sat1[0]+'\n')
			f.write(sat1[1]+'\n')
			f.write(sat1[2]+'\n')

