#!/bin/bash
bash
echo "Please enter the first job number to be run:"
read first
echo "Please enter the last job number to be run:"
read last

if [$first -gt $last]; then
	echo "Error: Values out of order. Now exiting. "
	exit 1
fi

for ((i=$first;i<=$last;i++)); do
	echo "Running Job #$i"
	job -a -b -c -i ANCinput$i.job &
	wait %1
done

echo "All jobs successfully run."