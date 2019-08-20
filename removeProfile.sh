#!/bin/bash

profileName=$1
profileDir=/home/itsonlycole/.config/qutebrowser-$profileName
profileShortcut=/home/itsonlycole/.local/share/applications/qutebrowser-$profileName.desktop

rm -rf $profileDir
rm $profileShortcut
#Call Python Script to Remove Profile from profiles.XML/JSON
exec python3 removeProfileFromXML.py $profileName
