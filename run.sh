#!/bin/bash

if [ $# -eq 0 ]
then

    echo "Please supply image dir name"

    exit 1

fi


ABS_IMG_DIR="$(dirname $(readlink -e $1))/$(basename $1)"

mkdir -p out/

python3 augment.py $ABS_IMG_DIR