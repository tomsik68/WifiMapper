import subprocess, json, sys, iwlistparse2
jsonCaptures = json.load(open('spots-in-time.json'))
interface = sys.argv[1]

def filterList(spots):
	result = {}
	for spot in spots:
		result[spot["Address"]] = {"Signal": spot["Signal"], "Quality": spot["Quality"]}
	return result

iwList = subprocess.check_output(['iwlist', interface, 'scanning'])
spots = iwlistparse2.getCells(iwList.split('\n'))

capture = {}
capture["date"] = subprocess.check_output('date').replace('\n','')
capture["spots"] = filterList(spots)
jsonCaptures.append(capture)

json.dump(jsonCaptures, open('spots-in-time.json','w'))
