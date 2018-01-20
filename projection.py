import pyproj
import os
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

rawData = csv.reader(open('red_lightsplateau.csv', 'rb'), dialect='excel')

for row in rawData:
    # iter += 1
    # if iter >= 2:
    print row[4]
