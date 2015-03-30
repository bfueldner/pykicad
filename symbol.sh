#!/bin/bash

# TODO: Generate controller like symbols another way
# TODO; How to generate this logic gatter stuff?

. config
. $SCRIPT_DIR/tools.sh

#rm -rf $FOOTPRINT_PATH
#mkdir $FOOTPRINT_PATH

for CSV_FILE in $DATA_DIR/symbol/*.csv
do
	if [ -f $CSV_FILE ]
	then
		echo "File: $CSV_FILE"

		LIBRARY_NAME=$(basename -s .csv "$CSV_FILE")
		echo "Library name: $LIBRARY_NAME"
	#	mkdir $SYMBOL_DIR/$LIBRARY_NAME

		echo "$SYMBOL_START"

		COLUMN=()
		SYMBOL_COUNT=0
		ERROR_COUNT=0
		FIRST_LINE=1

		while read -r LINE && [[ -n $LINE ]]
		do
			if [ $FIRST_LINE -ne "1" ]
			then
				eval "declare -a DATA=($(echo $LINE | awk -v FPAT='[^,]*|(\"[^\"]+\")' '{ for (i = 1; i <= NF; i++) { gsub("^\"|\"$","",$i); printf("\"%s\" ", $i) } }'))"
		
				SYMBOL=${DATA[0]}
				SYMBOL_FILE=$DATA_DIR/$SYMBOL.lib
				if [ -f $SYMBOL_FILE ]
				then
					SYM=$(head -n -2 $SYMBOL_FILE | tail -n +3 -)

					INDEX=0
					for COL in ${COLUMN[*]}
					do
						echo ${COL^^*} $INDEX ${DATA[$INDEX]}
						SYM="${SYM//\$${COL^^*}/${DATA[$INDEX]}}"
						INDEX=$((INDEX+1))
					done
					echo "$SYM"

				# TODO: Generate meta file with description and keywords!

					SYMBOL_COUNT=$((SYMBOL_COUNT+1))
				else
					ERROR_COUNT=$((ERROR_COUNT+1))
				fi
			else
				eval "declare -a COLUMN=($(echo $LINE | awk -v FPAT='[^,]*|(\"[^\"]+\")' '{ for (i = 1; i <= NF; i++) { gsub("^\"|\"$","",$i); printf("\"%s\" ", $i) } }'))"
				echo ${COLUMN[*]^^*}
			fi
			FIRST_LINE=0
		done < $CSV_FILE
		echo "$SYMBOL_END"

		echo ""
		echo "$SYMBOL_COUNT symbols created"
		if [ $ERROR_COUNT -ne 0 ]
		then
			echo "Error generating $ERROR_COUNT symbols"
		fi
	fi
done

