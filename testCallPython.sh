#!/bin/bash

profileName="My Cool Profile"

echo $profileName

exec python3 createShortcut.py $profileName
