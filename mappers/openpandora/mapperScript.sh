# This script is part of WifiMapper project

GPS_INTERFACE=`cat gps_interface`
ROUTE_FILE="route"
INTERVAL=1 # second(s)

echo "This is mapper script of WifiMapper project. Please read manual before using it."
echo "Starting up GPS..."
sh startGPS.sh
echo "Setting up wifi..."
WIFI_INTERFACE=`python get_wifi_interface.py`
echo "Press CTRL-C to stop capturing"
echo "Now hit ENTER to start capturing"
read ignore

while [ 0 -lt 1 ]; do
  python dump-spots.py $WIFI_INTERFACE
  python dump-signal.py $WIFI_INTERFACE
  GPS_DUMP=`gpspipe -w -t -n 3 | tail --lines 1`
  echo $GPS_DUMP >> $ROUTE_FILE
  sleep $INTERVAL
done
