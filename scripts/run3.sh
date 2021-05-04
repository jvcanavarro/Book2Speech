#!/bin/sh

tdir="../icdar2015/texts"
list="image_list"

core="python ../book2speech/core.py"

trm="--transform-mode"
tm="--thresh-mode"
bm="--blur-mode"

flags="--disable-tts --calculate-metrics --debug $trm=extended"

while read image
do
    text="$(basename $image .jpg).txt"
    echo $image

    # Thresh + Blur
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=gaussian $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=median $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=gaussian $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=median $flags"
    eval $cmd


    # Thresh + Dewarp
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd


    # Blur + Dewarp
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=gaussian --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=gaussian --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=gaussian --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=median --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=median --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $bm=median --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd


    # Thresh + Blur + Dewarp
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=gaussian --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=gaussian --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=gaussian --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=median --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=median --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=simple $bm=median --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=gaussian --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=gaussian --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=gaussian --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=median --dewarp $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=median --dewarp --optimizer=Powell $flags"
    eval $cmd
    cmd="$core -i $image -t $tdir/$text --improve-image $tm=otsu $bm=median --dewarp --optimizer=L-BFGS-B $flags"
    eval $cmd

done < "$list"
