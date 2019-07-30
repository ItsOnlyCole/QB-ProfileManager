#!/bin/bash

profileName=$1
profileDir=~/.config/qutebrowser-$profileName
profileShortcut=~/.local/share/applications/qutebrowser-$profileName.desktop

rm -rf $profileDir
rm $profileShortcut
#Call Python Script to Remove Profile from profiles.XML/JSON
