## What is WifiMapper?

WifiMapper 'takes notes' of available wifi networks & information about them while you're on the go. **WifiMapper only scans for networks, it doesn't do any packet capture.**
Aside of wifi, it takes notes of your GPS-based position, so you can create a map of where approximately wifi networks are.

## Mappers & Renderers

This project is split up into mappers & renderers. 

+ **Mapper** is a script which runs on a portable device and its task is to take notes of wifi & GPS data.

+ **Renderer** is a program which runs on desktop/laptop and its task is to take the data from your device and visualize them for the user.

## Mappers

Mappers are currently available on following platforms:

+ Linux

## Renderers

Renderers currently available:

+ GeoJSON "renderer" (this only creates GeoJSON files from your measurements)

## Work-In-Progress

+ OpenLayers web (Renderer)

## Plans

+ Android (Mapper+Renderer)

## License

This project is under GNU GPLv3 license. See http://www.gnu.org/licenses/gpl.txt for more information.
