#!/usr/bin/env bash

progname=`basename $0`
log_file="$1"

# check log file supplied is valid
if [[ ! -r $log_file ]]; then
	cat <<END

Parses ssh log file and strips off the IP address.

Example:

	$progname log_file 

END

  exit 1
fi

# takes ip from ssh logger and strips the ip 
for line in $(cut -d'-' -f6 "$log_file" | cut -d' ' -f2 | sort | uniq)
do
	echo $line | sed -E 's/\[|\]//g' >> 
done
