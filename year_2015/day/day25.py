#!/usr/bin/python

import re as regex

def level1(input):
	code = 20151125
	numbers = [int(value) for value in regex.findall(r'\d+', input)]
	occurence = ((numbers[0] + numbers[1] - 1) * (numbers[0] + numbers[1] - 2)) // 2 + numbers[1]
	print("Occurence 1:\t" + str(code))
	for i in range(2, occurence + 1):
		code = (code * 252533) % 33554393
		print("Occurence " + str(i) + ":\t" + str(code))
	return code

def level2(input):
	return "Done"