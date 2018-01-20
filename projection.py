import pyproj
x, y = (299374.82, 5041400.07)

p = pyproj.Proj("+proj=tmerc +lat_0=0 +lon_0=-73.5 +k=0.999900 +x_0=304800 +y_0=0 +ellps=GRS80 +units=m +no_defs no_defs")
lon, lat = p(x, y, inverse=True)
print lat, lon
