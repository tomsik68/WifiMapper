# This script is part of WifiMapper project

import subprocess

def iwconfigCommand():
    return ['iwconfig']

def iwlistScanCommand(interface):
    return ['iwlist',interface,'scanning']

NO_WIFI_EXTENSIONS='no wireless extensions'

# TODO: verify if the scan was successful
def scanningSuccess(iwlistOutput): 
    return True

# find target interface using iwconfig
interfacesOut = subprocess.check_output(iwconfigCommand(),stderr=subprocess.STDOUT)
interfaces = []
#   look for interfaces with wireless extensions
for line in interfacesOut.split('\n'):
    if len(line) > 0 and not line.startswith(' ') and line.find(NO_WIFI_EXTENSIONS) < 0:
        interfaces.append(line[0:line.index(' ')])

for interface in interfaces:
    print interface
