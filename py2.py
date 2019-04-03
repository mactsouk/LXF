#!/usr/bin/env python3
import os
import sys

if len(sys.argv) >= 2:
	directory = str(sys.argv[1])
else:
	print('Not enough arguments!')
	sys.exit(0)

total = 0

for root, dirs, files in os.walk(directory):
	for file in files:
		total = total + 1

print('Visited', total, 'files!')
