# This script is part of WifiMapper project
# This setup script will setup Linux mapper
# Usage: sh setup.sh <DESTINATION FOLDER> [download]

# Variables
LINK="https://codeload.github.com/tomsik68/WifiMapper/zip/master"
DEST=$1
# Mapper to install
MAPPER="linux"
# Make sure $DEST holds absolute path
if [[ $DEST != /* ]]; then
  DEST=`pwd`/$DEST
fi
UTILS="dump-signal dump-spots get-wifi-interface iwlist-parser coordinates-dump"

# Create environment dirs
mkdir $DEST
REPODIR=$(pwd)/../..
if [ $2 == "download" ] ; then
  mkdir "$DEST/tmp"
  # Download the newest version from github & unzip it
  cd "$DEST/tmp"
  echo "Downloading latest version of WifiMapper from github..."
  curl -k -o "repo.zip" $LINK
  echo "Extracting repo.zip..."
  unzip repo.zip
  REPODIR="${DEST}/tmp/WifiMapper-master"
fi
# Copy all scripts from mapper
echo "Copying scripts..."
cp $REPODIR/mappers/$MAPPER/* $DEST
echo "Copying utilities..."
# Copy files of needed utilities
for UTIL in $UTILS ; do
  echo "Copying $UTIL"
  if [ -e "$REPODIR/utils/$UTIL/setup.sh" ]; then
    cd $REPODIR/utils/$UTIL/
    echo "Running setup script for: $UTIL"
    sh setup.sh
  fi
  cp $REPODIR/utils/$UTIL/* $DEST
done
if [ $2 == "download" ] ; then
  echo "Cleaning tmp dir.."
  rm -rf "$DEST/tmp"
fi
echo "WifiMapper is now installed in $DEST !"
