#!/bin/bash

# get GPS
curl -O http://www.celestrak.com/NORAD/elements/gps-ops.txt

# get ISS
curl -O http://www.celestrak.com/NORAD/elements/stations.txt

# get HISPASAT
curl -O http://www.celestrak.com/NORAD/elements/geo.txt

# get IRIDIUM
curl -O http://www.celestrak.com/NORAD/elements/iridium.txt

# get GLONASS
curl -O http://www.celestrak.com/NORAD/elements/glo-ops.txt
