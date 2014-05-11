import json
import math

def polygonContainsPoint(polygon, point):
        i = 0
        j = len(polygon)-1
        c = False
        for polyPoint in poly:
                if ( ((polyPoint[1]>point[1]) != (polygon[j][1]>point[1])) and (point[0] < (polygon[j][0]-polygon[i][0]) * (point[1]-polygon[i][1]) / (polygon[j][1]-polygon[i][1]) + polygon[i][0]) ):
                        c = not c
        return c

geoJSON =   { 
    "type": "FeatureCollection",
    "features": [
    ]
}

route = json.load(open('route.json'))
spots = json.load(open('spots.json'))
spotsInTime = json.load(open('spots-in-time.json'))

myNumber = 0
polyPointsPerSpot = 6
# feel free to play with these parameters, they're just approximate...
signalPerLat = 1.0/200002.0
signalPerLng = 1.0/200002.0

points = {}
for point in route:
        if len(point["lat"]) > 0:
                spotData = spotsInTime[myNumber]
                lat = float(point["lat"])
                lng = float(point["lng"])
                for (k, v) in spotData["spots"].items():
                        if not points.has_key(k):
                                points[k] = []
                        points[k].append([lat, lng, v])
        myNumber += 1


for spot in points.keys():
        polygons = []
        # create polygons from measured data
        for point in points[spot]:
                signal = abs(int(point[2]["Signal"]))
                pointsInPolygon = []
                ang = 0
                while ang < 360:
                        ang += 360.0/polyPointsPerSpot
                        rad = math.radians(ang)
                        pointsInPolygon.append([point[1]+signal*signalPerLng*math.sin(ang), point[0]+signalPerLat*math.cos(ang)*signal])
                polygons.append(pointsInPolygon)
        # drop points that other polygon(s) contain
        finalPoints = []
        for poly in polygons:
                for point in poly:
                        # here point, have a chance!
                        finalPoints.append(point)
                        for polygon in polygons:
                                if not (polygon is poly) and (polygonContainsPoint(polygon, point)):
                                        finalPoints.remove(point)
                                        break
        # add final points as single polygon to GeoJSON file
        essid = "<hidden>"
        if spots[spot].has_key("ESSID"):
                essid = spots[spot]["ESSID"]
        polygonFeature = {"type": "Feature", "properties": {'addr': spot, 'ESSID':essid, 'Encryption': spots[spot]["EncryptionKey"],'spotInfo': spots[spot]}, "geometry": {"type": "Polygon", "coordinates": [finalPoints]}}
        if len(finalPoints) > 4:
                geoJSON["features"].append(polygonFeature)
        
json.dump(geoJSON, open('spotMap.geojson', 'w'))
