#!/bin/bash

profileName=$1 #String
copyConfig=$2 #Boolean
configDir=~/.config/qutebrowser-
baseQuteBrowserDir=~/.config/qutebrowser

mkdir $configDir$profileName
exec python3 createShortcut.py $profileName

if [ !$copyConfig ]
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
    
#Call Python Script to Add Profile to profiles.xml/json
