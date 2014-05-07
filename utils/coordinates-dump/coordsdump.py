import sys, json, time

route = json.load(open('route.json'))

latitude = ""
longtitude = ""

for line in sys.stdin:
	split = line.split(' ')
	if split[0] == 'GPSD,O=GGA' or split[0] == 'GPSD,O=RMC':
		latitude = split[3]
		longtitude = split[4]
strDate = time.strftime('%d/%m/%y')
strTime = time.strftime('%H:%M:%S')
routeObj = {
	"lat": latitude, 
	"lng": longtitude,
	"date": strDate,
	"time": strTime
}
route.append(routeObj)
json.dump(route, open('route.json','w'))
