# This script is part of WifiMapper project

GPS_INTERFACE=`cat gps_interface`
ROUTE_FILE="route"
TIME_FILE="time"
INTERVAL=3 # second(s)

echo "This is mapper script of WifiMapper project. Please read manual before using it."
echo "Moving captured files..."

CAPDIR="capture-${RANDOM}"
mkdir $CAPDIR
mv route $CAPDIR
mv time $CAPDIR
mv spots-in-time.json $CAPDIR
mv spots.json $CAPDIR
echo "Moving done! Invoking cleanup script..."
sh clean.sh
echo "Please make sure your GPS is already connected"
echo "Setting up wifi..."
WIFI_INTERFACE=`python get_wifi_interface.py`
echo "Wifi interface: " $INTERFACE
echo "Press CTRL-C to stop capturing"
echo "Now hit ENTER to start capturing"
read ignore

MEASUREMENT=1
while [ 0 -lt 1 ]; do
  echo "${MEASUREMENT}	`date`" >> $TIME_FILE
  python dump-spots.py $WIFI_INTERFACE $MEASUREMENT
  python dump-signal.py $WIFI_INTERFACE $MEASUREMENT
  GPS_DUMP=`gpspipe -w -n 5`
  GPS_COORDS=`echo "$GPS_DUMP" | python coordsdump.py`
  echo "${MEASUREMENT}	${GPS_COORDS}" >> $ROUTE_FILE
  MEASUREMENT=$((MEASUREMENT+1))
  sleep $INTERVAL
done
