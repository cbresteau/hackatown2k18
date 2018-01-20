#! usr/bin/python
# -*- coding: ISO-8859-1 -*-
import pyproj
import os
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
# ----------------------------Récupération données----------------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

p = pyproj.Proj("+proj=tmerc +lat_0=0 +lon_0=-73.5 +k=0.999900 +x_0=304800 +y_0=0 +ellps=GRS80 +units=m +no_defs no_defs")


# Read in raw data from csv
rawData = csv.reader(open('red_lightsplateau.csv', 'rb'), dialect='excel')
# the template. where data from the csv will be formatted to geojson
template = \
    ''' \
    { "type" : "Feature",
        "geometry" : {
            "type" : "Point",
            "coordinates" : [%s, %s]},
        "properties" : { "id" : %s, "unixTime" : "%s", "msgtext" : "%s", "userID": "%s"}
        },
    '''
# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    "features" : [
    '''
# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    # if iter >= 2:
    id = row[0]
    x = row[4]
    y = row[5]
    lat, lon = p(x, y, inverse=True)
    unixTime = 1516475517
    msgtext = row[1]
    userID = row[3]
    # output += template % (row[0], row[2], row[1], row[3], row[4])
    output += template % (lon, lat,  id,  unixTime, msgtext, userID)

# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''

# opens an geoJSON file to write the output to
outFileHandle = open("geo_redlights.json", "w")
outFileHandle.write(output)
outFileHandle.close()
