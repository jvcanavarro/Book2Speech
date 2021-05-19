#!/bin/sh

tdir="../icdar2015/texts"
list="image_list"
monogram="../dicts/en_80k.txt"
bigram="../dicts/en_bi_242k.txt"


core="python ../book2speech/core.py"

cm="--correction-mode"
tm="--thresh-mode"
bm="--blur-mode"
trm="--transform-mode"

flags="--disable-tts --calculate-metrics --debug $trm=extended"

while read image
do
    text="$(basename $image .jpg).txt"
    echo $image

    cmd="$core -i $image -t $tdir/$text $flags"
    eval $cmd

    # Spell Checking

    cmd="$core -i $image -t $tdir/$text -m $monogram $cm=direct $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text -m $monogram $cm=segmentation $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text -m $monogram -b $bigram $cm=compound $flags"
    eval $cmd

    # Image Processing
    ## Threshold
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=global $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $tm=gaussian $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $tm=mean $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $flags"
    eval $cmd

    ## Blur
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=average $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $bm=gaussian $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $bm=median $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image $bm=bilateral $flags"
    eval $cmd

    ## Dewarp
    cmd="$core -i $image -t $tdir/$text --improve-image --dewarp $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image --dewarp --optimizer=Powell $flags"
    eval $cmd

    cmd="$core -i $image -t $tdir/$text --improve-image --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd

done < "$list"
