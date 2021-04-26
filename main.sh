#!/usr/bin/env bash

#Go into the programs directory
cd Programs

#Run Python scripts to generate LT-files
python3 GenerateForceField.py
python3 GenerateChain.py $1
python3 GenerateSystem.py $1 $2

#Run Moltemplate to generate data file
moltemplate.sh -nocheck -atom-style "angle" system.lt

cp system.data ../$3
