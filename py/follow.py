#!/usr/bin/python
import math
import time
import ephem
import os
from datetime import datetime
degrees_per_radian = 180.0 / math.pi

def compute_alt(altitude):
    return int(50 * int(abs(altitude)) / 90)

def compute_azimuth(azimuth):
    return int(azimuth/3.6)

# This is Lisbon, Portugal
home = ephem.Observer()
home.lon = '-9.1333'   # +E
home.lat = '38.7667'      # +N
home.elevation = 123 # meters 

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle(
#'ISS (ZARYA)',
#'1 25544U 98067A   14245.51991314  .00013026  00000-0  23431-3 0   101',
#'2 25544  51.6451  76.2836 0003709  72.7397  20.6341 15.50183561903328'
'GPS BIIF-6  (PRN 06)',    
'1 39741U 14026A   14258.69389229 -.00000041  00000-0  00000+0 0  1127',
'2 39741  55.0732 140.3956 0003099 145.3158 214.7630  2.00572832  2435'
)

while True:
    home.date = datetime.utcnow()
    iss.compute(home)
    print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    os.system ("echo 0=" + str(compute_azimuth(iss.az  * degrees_per_radian)) +"% > /dev/servoblaster")
    os.system ("echo 1=" + str(compute_alt(iss.alt * degrees_per_radian)) + "% > /dev/servoblaster")
    time.sleep(1.0)





