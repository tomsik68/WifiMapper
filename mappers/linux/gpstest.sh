# This script is part of WifiMapper project
echo "This is a script which will help you to test whether your GPS connection works."
echo "With successful connection, you should see lots of lines with GP prefix popping out on your screen."
echo "This script will not automatically close, so you need to press CTRL-C once you're sure your GPS connection is fine."
echo "Press enter to continue"
read ignore
cat `cat gps_interface`
