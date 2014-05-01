# This script is part of WifiMapper project

# In order to make this working, you need to write your GPS module's bluetooth address to file "gps_address".
# the address should look like this:  "0A:1B:2C:3D:4E:5F"
GPS=`cat gps_address`
INTERFACE="rfcomm0"

sudo hcitool cc $GPS
# The script takes note of GPS interface to be used
echo $INTERFACE > "gps_interface"
sudo rfcomm connect "/dev/${INTERFACE}" $GPS
