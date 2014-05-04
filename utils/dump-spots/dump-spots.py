import subprocess, json, sys, iwlistparse2
jsonSpots = json.load(open('spots.json'))
interface = sys.argv[1]

measurementNumber = sys.argv[2]

iwList = subprocess.check_output(['iwlist', interface, 'scanning'])
cellsList = iwlistparse2.getCells(iwList.split('\n'))
for cell in cellsList:
	if not cell["Address"] in jsonSpots:
		cell["FirstSeen"] = measurementNumber
		jsonSpots[cell["Address"]] = cell



json.dump(jsonSpots, open('spots.json','w'))
