#!/bin/bash
searchstring="@"
while read -r line; do
	temp=${line#*$searchstring}
	ssh-keyscan -H $temp >> ~/.ssh/known_hosts
done < pssh_hosts_files
