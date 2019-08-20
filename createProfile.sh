#!/bin/bash

profileName=$1 #String
copyConfig=$2 #Boolean
configDir=/home/itsonlycole/.config/qutebrowser-
baseQuteBrowserDir=/home/itsonlycole/.config/qutebrowser

mkdir $configDir$profileName

if [ -z "$copyConfig" ]
then
    copyConfig="False"
fi
if [ $copyConfig = "True" ]
then
    mkdir $configDir$profileName/config
    cp $baseQuteBrowserDir/config.py $configDir$profileName/config/config.py
elif [ $copyConfig = "true" ]
then
    mkdir $configDir$profileName/config
    cp $baseQuteBrowserDir/config.py $configDir$profileName/config/config.py
fi

exec python3 createShortcut.py $profileName &
exec python3 addProfileToXML.py $profileName &
