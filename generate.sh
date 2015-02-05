#!/bin/bash

DATA_PATH=$(pwd)/data
echo $DATA_PATH

skip_1st_line=1
while IFS=, read library generator name
do
	if test $skip_1st_line != "1"
	then
		echo $library $generator $name
	#	echo $name \| $pad_width \| $pad_height $pad_distance $package_width $package_height
	#	build/footprint -t soic -n $name -c $count -w $package_width -h $package_height -x $pad_width -y $pad_height -d $pad_distance -r $row_distance
	fi
	skip_1st_line=0
done < $DATA_PATH/library.csv
