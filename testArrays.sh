#!/bin/bash

read -r -p "Enter Variables: " -a testArray

for var in ${testArray[@]}; do
    echo $var
done
