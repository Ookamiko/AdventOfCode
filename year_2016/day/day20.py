#!/usr/bin/python

import re as regex

def init_range(lines):
	rang = []
	for line in lines:
		rang.append([int(x) for x in regex.findall(r'\d+', line)])

	return rang

def level1(input):
	#input = '5-8\n0-2\n4-7\n'
	rang = init_range(input.strip().split('\n'))
	rang.sort(key=lambda x: x[0])

	max_val = 0

	for test in rang:
		if test[0] <= max_val + 1:
			max_val = max(max_val, test[1])
		else:
			break

	return max_val + 1

def level2(input):
	#input = '5-8\n0-2\n4-7\n'
	rang = init_range(input.strip().split('\n'))
	rang.sort(key=lambda x: x[0])

	max_val = 0
	count = 0

	for test in rang:
		if test[0] > max_val + 1:
			count += test[0] - (max_val + 1)
		max_val = max(max_val, test[1])

	return count