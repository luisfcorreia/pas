#!/bin/bash

# get GPS
curl -O http://www.celestrak.com/NORAD/elements/gps-ops.txt

# get ISS
curl -O http://www.celestrak.com/NORAD/elements/stations.txt

# get HISPASAT
curl -O http://www.celestrak.com/NORAD/elements/geo.txt

