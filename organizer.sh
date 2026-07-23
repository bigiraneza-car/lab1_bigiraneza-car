#!/usr/bin/bash
#Check fi directory archive exists, if it does not create one.
if [ ! -d archive ]; then
	mkdir archive
fi

#timestamp generation
timestamp= $(date +%Y%m%d-%H%M%S)

#archiving the renamed grades+timestamp file.
new_name="grades_${timestamp}.csv"
mv grades.csv "archive/$new_name"
# workspace reset
touch grades.csv

#Logging
echo "$timestamp , original filename: grades.csv, archived new name: $new_name" >> organizer.log
