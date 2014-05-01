# This file is part of WifiMapper project
#!/bin/sh
sudo rfcomm connect 0 &
sleep 3 &
echo "/dev/rfcomm0" > gps_interface &
gpsd -b -n /dev/rfcomm0 &
