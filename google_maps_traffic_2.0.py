import googlemaps
import requests
import sys
import datetime
import csv
 
now = datetime.datetime.now()
#Declarations
token = '' #Enter your Google API Token'
start = sys.argv[1]
end = sys.argv[2]
log = sys.argv[3]
# get Client object
client = googlemaps.Client(key=token)
# Get directions
time = now.strftime("%H:%M:%S")
date = now.strftime("%d:%m:%Y")

directions = client.distance_matrix(start,end, departure_time=now)
result = date + "," + time + "," +str(directions["rows"][0]["elements"][0]["distance"]["value"]) + ","  + str(directions["rows"][0]["elements"][0]["duration_in_traffic"]["value"])

f = open(log,'a')
f.write(result + "\n")
f.close()

