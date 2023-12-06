#!/usr/bin/python

import re as regex

def level1(input):
	# Test value
	# input = 'Time:      7  15   30\nDistance:  9  40  200\n'
	tmp = input.strip().split('\n')
	time = [int(x) for x in regex.findall(r'\d+', tmp[0])]
	record = [int(x) for x in regex.findall(r'\d+', tmp[1])]
	result = 1

	for i in range(len(time)):
		current_time = time[i]
		current_record = record[i]
		index_found = 0

		for j in range(current_time + 1):
			if current_record < j * (current_time - j):
				index_found = j
				break

		result *= current_time - (index_found * 2) + 1

	return result

def level2(input):
	# Test value
	# input = 'Time:      7  15   30\nDistance:  9  40  200\n'
	tmp = input.strip().split('\n')
	time = int(''.join(regex.findall(r'\d+', tmp[0])))
	record = int(''.join(regex.findall(r'\d+', tmp[1])))

	index_found = 0

	for j in range(time + 1):
		if record < j * (time - j):
			index_found = j
			break

	return time - (index_found * 2) + 1