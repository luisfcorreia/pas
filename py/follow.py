#!/usr/bin/python
import math
import time
import ephem
import os
from datetime import datetime
degrees_per_radian = 180.0 / math.pi

def compute_alt(altitude):
    return int(50 * int(altitude) / 90)

def compute_azimuth(azimuth):
    return int(azimuth/3.6)

# This is Lisbon, Portugal
home = ephem.Observer()
home.lon = '-9.9'   # +E
home.lat = '34.44'      # +N
home.elevation = 10 # meters 

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle(
#'ISS (ZARYA)',
#'1 25544U 98067A   14245.51991314  .00013026  00000-0  23431-3 0   101',
#'2 25544  51.6451  76.2836 0003709  72.7397  20.6341 15.50183561903328'
'GPS BIIR-7  (PRN 18)',
'1 26690U 01004A   14258.27923102 -.00000011  00000-0  00000+0 0  3653',
'2 26690  53.0316 199.8591 0156962 245.0384 340.9447  2.00556488 99849'
)

while True:
    home.date = datetime.utcnow()
    iss.compute(home)
    print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    os.system ("echo 0=" + str(compute_azimuth(iss.az  * degrees_per_radian)) +"% > /dev/servoblaster")
    os.system ("echo 1=" + str(compute_alt(iss.alt * degrees_per_radian)) + "% > /dev/servoblaster")
    time.sleep(1.0)





