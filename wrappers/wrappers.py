#Problem        : Wrapper's Delight
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys
import re

data = sys.stdin.readlines()

width=int(data[0])

text=data[1]
(text, foo)=re.subn("~","\n ",text)
text=text.rstrip(" \n")

words=text.split(" ")

line=""
sep=""
while words:
	if len(line)+len(sep)+len(words[0].rstrip("\n")) > width:
		print(line)
		line=""
		sep=""

	line+=sep+words[0]

	sep=" "

	if re.search("\n",words[0]):
		print(line.rstrip("\n"))
		line=""
		sep=""

	words=words[1:]

print(line.rstrip("\n"))
	
