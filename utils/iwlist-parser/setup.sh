# This script is part of WifiMapper project
# This is a setup script for iwlistparse2 utility
echo "-- Downloading iwlistparse2.py..."
curl -k -o "iwlistparse2.py" "https://python-parser-for-iwlist-improved.googlecode.com/files/iwlistparse2.py"
echo "-- Applying patches to iwlistparse2..."
patch "iwlistparse2.py" < iwlistparse_patches
echo "-- Cleaning patch file, so it doesn't scare people..."
rm iwlist_patches
rm notice.md
echo "-- Done!"
