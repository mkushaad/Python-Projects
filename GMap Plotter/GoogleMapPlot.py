import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(37.7749,-122.4194,5)

with open("cordinates.csv",'r') as f:
    reader = csv.reader(f)
    k = 0
    
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        
        if k == 0:
            gmap.marker(lat,long,'yellow')
            k = 1
        else:
            gmap.marker(lat,long,'green')
    gmap.marker(lat,long,'blue')
    
gmap.draw("myMap.html")
