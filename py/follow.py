#!/usr/bin/python
import math
import time
import ephem
import os
from datetime import datetime
degrees_per_radian = 180.0 / math.pi
skyfile = 'choice.txt'

def compute_alt(altitude):
	return int(50 * int(abs(altitude)) / 90)

def compute_azimuth(azimuth):
	return int(azimuth/3.6)

def get_satelite():
	data = ""
	# fallback to ISS
	if os.path.isfile(skyfile):
		f = open(skyfile,'r')
		# read stuff from file
		d1 = f.readline().strip()
		d2 = f.readline().strip()
		d3 = f.readline().strip()
	else:
	
		d1 = 'ISS (ZARYA)             '
		d2 = '1 25544U 98067A   14261.23801446  .00018591  00000-0  32825-3 0  1047'
		d3 = '2 25544  51.6475 358.3858 0002361 110.9951 286.5700 15.50404752905766'
	

	return ephem.readtle(d1,d2,d3)

# This is Lisbon, Portugal
home = ephem.Observer()
home.lon = '-9.1333'   # +E
home.lat = '38.7667'      # +N
home.elevation = 123 # meters 

firstrun= True

while True:

	if firstrun:
		skyobject = get_satelite()
		firstrun = False
		if os.path.isfile(skyfile):
			os.remove(skyfile)
	
	home.date = datetime.utcnow()
	skyobject.compute(home)
	print('skyobject: altitude %4.1f deg, azimuth %5.1f deg' % (skyobject.alt * degrees_per_radian, skyobject.az * degrees_per_radian))
	os.system ("echo 0=" + str(compute_azimuth(skyobject.az  * degrees_per_radian)) +"% > /dev/servoblaster")
	os.system ("echo 1=" + str(compute_alt(skyobject.alt * degrees_per_radian)) + "% > /dev/servoblaster")
	time.sleep(1.0)

	if os.path.isfile(skyfile):
		firstrun = True





