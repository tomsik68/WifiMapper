# This file is part of WifiMapper project
#!/bin/sh
echo "/dev/rfcomm0" > gps_interface
sudo rfcomm connect 0
