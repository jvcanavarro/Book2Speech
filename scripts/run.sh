#!/bin/sh

list="image_list"

while read image
do
    text="$(basename $image .jpg).txt"
    cmd="python ../book2speech/core.py -i $image -t ../icdar2015/texts/$text --transform-mode=extended --lang=eng --disable-tts --calculate-metrics -v --improve-image --blur-mode=gaussian --dewarp --optimizer=l-bfgs-b"
    echo -e "\n"$cmd
    eval $cmd

done < "$list"
