import json

geoJSON =   { 
    "type": "FeatureCollection",
    "features": [
    ]
}
#geoJSON = []
route = json.load(open('route.json'))
spots = json.load(open('spots.json'))
spotsInTime = json.load(open('spots-in-time.json'))

# create line feature from route
lineFeature = {"type": "Feature", "properties": {}, "geometry": {"type": "LineString", "coordinates": []}}
myNumber = 0
for point in route:
        if len(point["lat"]) > 0:
                spotData = spotsInTime[myNumber]
                lat = float(point["lat"])
                lng = float(point["lng"])
                lineFeature["geometry"]["coordinates"].append([lng, lat])
                for (k, v) in spotData["spots"].items():
                        signal = abs(int(v["Signal"]))
                        circle = {"type": "Feature", "properties": {"radius": signal/200.0, 'addr': k,'spotData': spots[k]}, "geometry": {"type": "Point", "coordinates": [lng, lat]}}
                        #geoJSON.append(circle)
                        geoJSON["features"].append(circle)
        myNumber += 1
geoJSON["features"].append(lineFeature)	
#geoJSON.append(lineFeature)
json.dump(geoJSON,open('data.geojson','w'))
