#Problem        : Lannisters of Justice
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys
import re

# in priority order
global token_list
token_list = ['-','/','+','*']

def evaluate(tokens):
        """Return the result of parsing the expression tree in tokens
        """
	global token_list

        #print("Parsing 1: ",tokens)
        if isinstance(tokens[0], list):
                l_arg = evaluate(tokens[0])
        else:
                tokens[0]=re.sub("~","-",tokens[0])
                l_arg = int(tokens[0])

        # unwrap if it was just a nested list
        if len(tokens)==1:
                return l_arg

        #print("Parsing 2: ",tokens)
        if isinstance(tokens[2], list):
                r_arg = evaluate(tokens[2])
        else:
                tokens[2]=re.sub("~","-",tokens[2])
                r_arg = int(tokens[2])

        op = tokens[1]

        #print("op: ",op)
        assert(op in token_list)

        if op == "-":
                return l_arg - r_arg

        if op == "+":
                return l_arg + r_arg

        if op == "*":
                return l_arg * r_arg

        if op == "/":
                return l_arg / r_arg

        assert(False and ("Invalid operator: "+op))

def handle_negative_numbers(tokens):
	"""If any '-' operators follow another operator, treat them as negation."""
	global token_list
	result = []
	skip = False
	#print('hnn tokens: ', tokens)
	for token_index in range(0, len(tokens)):
		#print('hnn loop result', result)
		if skip:
			skip = False
			continue

		token = tokens[token_index]
		if token!="-":
			result.append(token)
			continue

		if token_index>0 and tokens[token_index-1] not in token_list:
			result.append(token)
			continue

		result.append(['-1', '*', tokens[token_index+1]])
		skip = True

	#print('hnn result: ', result)
	return result
		
def main():
	data = sys.stdin.readlines()

	expr = data[0].rstrip("\n ")
	(expr, foo) = re.subn("([-+/*]|^)-","\\1~",expr)
	#print("expr: ", expr)

	if len(expr)==0:
		print("0")
		sys.exit(0)

	tokens = re.split('([-+*/])', expr)

	#print(expr)

	#print(tokens)

	#print("Pre-parsing, tokens: ", tokens)

	for operator in token_list:
		for token_index in range(0, len(tokens)-1):
			if token_index>len(tokens)-1:
				break
			token = tokens[token_index]
			if token is list or token != operator:
				continue
			#print("Before: ",tokens)
			tokens=tokens[:token_index-1] + [ [tokens[token_index-1], token, tokens[token_index + 1] ] ] + (tokens[token_index+2:] if token_index+2!=len(tokens) else [])
			#print("After: ", tokens)

	tokens=handle_negative_numbers(tokens)
	print(evaluate(tokens))

if __name__ == "__main__":
	main()
