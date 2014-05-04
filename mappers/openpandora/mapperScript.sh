# This script is part of WifiMapper project

GPS_INTERFACE=`cat gps_interface`
ROUTE_FILE="route"
TIME_FILE="time"
INTERVAL=1 # second(s)

echo "This is mapper script of WifiMapper project. Please read manual before using it."
echo "Moving captured files..."

CAPDIR="capture-$RANDOM"
mv route $CAPDIR
mv time $CAPDIR
mv spots-in-time.json $CAPDIR
mv spots.json $CAPDIR
echo "Moving done! Invoking cleanup script..."
sh clean.sh
echo "Please make sure your GPS is already connected"
echo "Setting up wifi..."
WIFI_INTERFACE=`python get_wifi_interface.py`
echo "Press CTRL-C to stop capturing"
echo "Now hit ENTER to start capturing"
read ignore

MEASUREMENT=1
while [ 0 -lt 1 ]; do
  echo "${MEASUREMENT}	`date`" >> $TIME_FILE
  python dump-spots.py $WIFI_INTERFACE $MEASUREMENT
  python dump-signal.py $WIFI_INTERFACE $MEASUREMENT
  GPS_DUMP=`gpspipe -w -n 3 | tail --lines 1`
  echo "${MEASUREMENT}	${GPS_DUMP}" >> $ROUTE_FILE
  ((MEASUREMENT++))
  sleep $INTERVAL
done
