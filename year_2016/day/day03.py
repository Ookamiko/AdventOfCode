#!/usr/bin/python

import re as regex

def level1(input):
	possibleTriangle = 0
	reg = r'\d+'
	for line in input.strip().split('\n'):
		numbers = [int(value) for value in regex.findall(reg, line)]
		numbers.sort()
		if numbers[2] < numbers[1] + numbers[0]:
			possibleTriangle += 1

	return possibleTriangle

def level2(input):
	possibleTriangle = 0
	reg = r'\d+'
	allNumbers = [int(value) for value in regex.findall(reg, input)]
	tmp = [[], [], []]
	for i in range(len(allNumbers)):
		tmp[i % 3].append(allNumbers[i])
	final = tmp[0] + tmp[1] + tmp[2]
	for i in range(0, len(final), 3):
		numbers = final[i:i+3]
		numbers.sort()
		if numbers[2] < numbers[1] + numbers[0]:
			possibleTriangle += 1

	return possibleTriangle