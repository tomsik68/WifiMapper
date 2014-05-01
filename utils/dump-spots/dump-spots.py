import subprocess, json, sys, iwlistparse2
jsonSpots = json.load(open('spots.json'))
interface = sys.argv[1]

iwList = subprocess.check_output(['iwlist', interface, 'scanning'])
cellsList = iwlistparse2.getCells(iwList.split('\n'))
for cell in cellsList:
	if not cell["Address"] in jsonSpots:
		jsonSpots[cell["Address"]] = cell



json.dump(jsonSpots, open('spots.json','w'))
