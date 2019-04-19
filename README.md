# Google Traffic time logging

### Prerequisites
* Python3 
* Pip3 
* Git 
* [Google Directions API Key](https://cloud.google.com/maps-platform/?apis=routes) 

### Installing
Clone this repository 
```
git clone https://github.com/japper83/Google-Traffic-time-logging.git
cd Google-Traffic-time-logging
```

Install the google maps module
```
pip3 install googlemaps
```

Change the Google Maps API value
```
token = 'EbYhtflimzMpWEiNNRcfKbJubwpyNQwOXgQGZBA'
```

### Running the script
The script needs 3 parameters; startpoint, endpoint, and log filename. The log filename needs to be a CSV-file.
```
python3 google_maps_traffic.py Amsterdam Utrecht logfile.csv
```

You can use coordinates by placing the startpoint and endpoint between quotes.
```
python3 google_maps_traffic.py '52.358727, 4.891133' '52.089422, 5.114595' logfile.csv
```



