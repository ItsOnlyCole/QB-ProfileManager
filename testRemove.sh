#!/bin/bash

profiles[0]="evenCoolerProfile2"
profiles[1]="profile3MyDood"
profiles[2]="weFinnaBeDoneWithThis"
profiles[3]="nanobii"

for profile in "${profiles[@]}"
do
    exec bash removeProfile.sh $profile &
    echo "removed profile: " + $profile
done  
