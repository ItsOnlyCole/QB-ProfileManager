#!/bin/bash

profileName=$1 #String
copyConfig=$2 #Boolean
configFolder=~/.config/qutebrowser-
baseQuteBrowserDir=~/.config/qutebrowser

mkdir $configcut$profileName
#Call Python Script to Create Shorcut

if [ !$copyConfig ]
then
    copyConfig="False"
fi
if [ $copyConfig = "True" ]
then
    mkdir $configcut$profileName/config
    cp $baseQuteBrowserDir/config.py $configcut$profileName/config/config.py
elif [ $copyConfig = "true" ]
then
    mkdir $configcut$profileName/config
    cp $baseQuteBrowserDir/config.py $configcut$profileName/config/config.py
fi
    
#Call Python Script to Add Profile to profiles.xml/json
