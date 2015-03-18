#!/bin/bash

. ../config
. tools.sh

# Generate all footprints from CSV table

DATA_PATH=$(pwd)/data
echo $DATA_PATH


#input=$1
#delimiter=$2

#if [ -z "$input" ];
#then
#	echo "Input file must be passed as an argument!"
#	exit 98
#fi

#if ! [ -f $input ] || ! [ -e $input ];
#then
#	echo "Input file '"$input"' doesn't exist!"
#	exit 99
#fi

rm -rf $FOOTPRINT_PATH
mkdir $FOOTPRINT_PATH

#cd $DATA_PATH
for CSV_FILE in ../data/footprint/*.csv
do
	echo $CSV_FILE

	LIBRARY=$(basename -s .csv $CSV_FILE)
	mkdir $FOOTPRINT_PATH/$LIBRARY

	SKIP_FIRST_LINE=1
	while read -r line && [[ -n $line ]]
	do
		if [ $SKIP_FIRST_LINE -ne "1" ]
		then
			eval "declare -a data=($(echo $line | awk -v FPAT='[^,]*|(\"[^\"]+\")' '{ for (i = 1; i <= NF; i++) { gsub("^\"|\"$","",$i); printf("\"%s\" ", $i) } }'))"
		
			# Generate footprint according to first column
			# TODO: Check, if 3d footprint file exists
			eval "footprint_${data[0]} ${data[1]} ${data[3]} ${data[4]} ${data[5]} ${data[6]} ${data[7]}" > $FOOTPRINT_PATH/$LIBRARY/${data[1]}$FOOTPRINT_EXTENSION
		fi
		SKIP_FIRST_LINE=0
	done < $CSV_FILE
done

