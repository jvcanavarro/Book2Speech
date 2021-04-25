#!/bin/sh

N=30
# ls ../icdar2015/images/ | sort -R | tail -$N > images_list
find ../icdar2015/images -type f | sort -R | tail -$N > image_list
# find ../icdar2015/images -type f | sort -R > image_list
