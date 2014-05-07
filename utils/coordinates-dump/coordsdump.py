import sys

for line in sys.stdin:
	split = line.split(' ')
	if split[0] == 'GPSD,O=GGA' or split[0] == 'GPSD,O=RMC':
		print split[3:4]
