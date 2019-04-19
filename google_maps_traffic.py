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
time = now.strftime("%d:%m:%Y-%H:%M:%S")

try:
   directions = client.directions(start,end,alternatives=True, departure_time=now)
except:
   print("MAPS API error")   

try:
   list = []
   for i,x in enumerate(directions):
      list.append([time, directions[i]["summary"],directions[i]["legs"][0]["duration_in_traffic"]["text"], directions[i]["legs"][0]["distance"]["text"]])
except:
   print("Enumeration Error")   

try:
   with open(log, "a") as f:
       writer = csv.writer(f)
       writer.writerows(list)
except:
   print("File write error")   