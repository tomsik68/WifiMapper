# This script is part of WifiMapper project
# This setup script will setup OpenPandora mapper
# Usage: sh setup.sh <DESTINATION FOLDER>

# Variables
LINK="https://github.com/tomsik68/WifiMapper/archive/master.zip"
DEST=$1
MAPPER="openpandora"
# Make sure $DEST holds absolute path
if [[ $DEST != /* ]]; then
  DEST="`pwd`/$DEST"
fi
UTILS="dump-signal dump-spots get-wifi-interface iwlist-parser"

# Create environment dirs
mkdir $DEST
cd $DEST
mkdir "tmp"
# Download the newest version from github & unzip it
cd "tmp"
echo "Downloading latest version of WifiMapper from github..."
wget -q -O "repo.zip" $LINK
echo "Extracting repo.zip..."
unzip repo.zip
cd ..
# Copy all scripts from mapper
echo "Copying scripts..."
cp $DEST/tmp/WifiMapper-master/mappers/$MAPPER/* $DEST
echo "Copying utilities..."
# Copy files of needed utilities
for UTIL in $UTILS ; do
  echo "Copying $UTIL"
  if [ -e "$DEST/tmp/WifiMapper-master/utils/$UTIL/setup.sh" ]; then
    cd "$DEST/tmp/WifiMapper-master/utils/$UTIL/"
    echo "Running setup script for: $UTIL"
    sh setup.sh
    cd $DEST
  fi
  cp $DEST/tmp/WifiMapper-master/utils/$UTIL/* $DEST
done
#echo "Cleaning tmp dir.."
#rm -rf "$DEST/tmp"
echo "WifiMapper is now installed in $DEST !"
