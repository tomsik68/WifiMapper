import sys, re

# Match line using regex with defined parameters. Parameters are like this: {groupNumber: "nameOfParameterInCell"}
def matchLine(line, pattern, params, cell):
    match = re.search(pattern, line)
    if match != None:
        for (k,v) in params.items():
            cell[v] = match.group(k)

# Add all found groups to desired key
def matchLineAddToArray(line, pattern, key, cell):
    match = re.search(pattern,line)
    if match != None:
        if not cell.has_key(key):
            cell[key] = []
        toAdd = []
        for group in match.groups():
            toAdd.append(group.replace('\n','').replace(';',''))
        cell[key].extend(toAdd)
        
def getCells(iwlistLines):
    cells = []
    cellData = None
    for line in iwlistLines:
        cellMatch = re.search(r'Cell (\d*) - Address: ([\w:]*)', line)
        if cellMatch != None:
            if cellData != None:
                cells.append(cellData)
            cellData = {}
            cellData["CellNumber"] = cellMatch.group(1)
            cellData["Address"] = cellMatch.group(2)
        matchLine(line, r'Channel:(\d*)', {1:"Channel"}, cellData)
        matchLine(line, r'Frequency:([\w.\s]*)', {1:"Frequency"}, cellData)
        matchLine(line, r'Quality=(\d*)/(\d*)', {1:"Quality", 2:"MaxQuality"}, cellData)
        matchLine(line, r'Signal level=(-[\w]*)', {1:"Signal"}, cellData)
        matchLine(line, r'Encryption key:([\w]*)', {1:"EncryptionKey"}, cellData)
        matchLine(line, r'ESSID:"([\w]*)"', {1:"ESSID"}, cellData)
        matchLine(line, r'Mode:([\w]*)', {1: "Mode"}, cellData)
        matchLineAddToArray(line, r'([[\d]*\s\wb/s[\s;]]*)', 'BitRates', cellData)
        matchLineAddToArray(line, r'Extra:(.+?)\n', 'Extras', cellData)
        matchLineAddToArray(line, r'IE:(.+?)\n', 'IEs', cellData)
        matchLine(line, r'Group Cipher : (.+?)\n', {1:"GroupCipher"}, cellData)
        matchLine(line, r'Pairwise Ciphers (.+?) : (.+?)\n', {2:"PairwiseCiphers"}, cellData)
        matchLine(line, r'Authentication Suites (.+?) : (.+?)\n', {2:"AuthenticationSuites"}, cellData)
        
    if cellData != None:
        cells.append(cellData)
    return cells
