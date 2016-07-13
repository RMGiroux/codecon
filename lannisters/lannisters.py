#Problem        : Lannisters of Justice
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys
import re

def parse(tokens):
	"""Return the result of parsing the expression tree in tokens
	"""

	#print("Parsing 1: ",tokens)
	if isinstance(tokens[0], list):
		l_arg = parse(tokens[0])
	else:
		l_arg = int(tokens[0])

	# unwrap if just a nested list
	if len(tokens)==1 and isinstance(tokens[0], list):
		return parse(tokens[0])

	#print("Parsing 2: ",tokens)
	if isinstance(tokens[2], list):
		r_arg = parse(tokens[2])
	else:
		r_arg = int(tokens[2])

	op = tokens[1]

	#print("op: ",op)
	assert(op in ['-','+','*','/'])

	if op == "-":
		return l_arg - r_arg

	if op == "+":
		return l_arg + r_arg

	if op == "*":
		return l_arg * r_arg

	if op == "/":
		return l_arg / r_arg

	assert(False and ("Invalid operator: "+op))

data = sys.stdin.readlines()

expr = data[0].rstrip("\n")

tokens = re.split('([-+*/])', expr)

#print(expr)

#print(tokens)

for operator in ['-', '/', '+', '*']:
	for token_index in range(0, len(tokens)-1):
		if token_index>len(tokens)-1:
			break
		token = tokens[token_index]
		if token is list or token != operator:
			continue
		#print("Before: ",tokens)
		tokens=tokens[:token_index-1] + [ [tokens[token_index-1], token, tokens[token_index + 1] ] ] + (tokens[token_index+2:] if token_index+2!=len(tokens) else [])
		#print("After: ", tokens)

print(parse(tokens))
