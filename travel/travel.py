#Problem        : Travel to the West
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.readlines()

pair_count = data[0]
data=data[1:]

paths_by_orig = {}
paths_by_dest = {}
routes = {}

for pair in data:
	pair=pair.rstrip("\n")
	(orig, dest) = pair.split(" ")	
	if orig not in paths_by_orig:
		paths_by_orig[orig]=[dest]
	else:
		paths_by_orig[orig].append(dest)

	if dest not in paths_by_dest:
		paths_by_dest[dest]=[orig]
	else:
		paths_by_dest[dest].append(orig)

	routes[pair]=[pair]

still_working=True
while still_working:
	for orig in paths_by_orig:
		for dest in paths_by_dest:
			pair = orig + " " + dest
			if pair in routes:
				continue

			
print(paths_by_orig)
print(routes)
