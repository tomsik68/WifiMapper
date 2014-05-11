## CreateRAWGeoJSON.py

This script creates **raw** GeoJSON data from your measurements. These data include points where you hit wifi hotspots and your route.

## mapSpots.py

This script takes raw capture data(just copy JSON files into this directory) and creates polygons based on where the wifi networks were located.

This script can be used to get the final view, although the polygon algorhithm is not perfect, you may want to display both "raw" data and these polygons.
