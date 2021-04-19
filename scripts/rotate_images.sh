#!/bin/sh

for photo in *.jpg ; do convert $photo -rotate 90 $photo ; done
