#!/usr/bin/python

import re as regex

def get_next_number(nbrs):
	next_diff = []
	all_zero = True

	for i in range(len(nbrs) - 1):
		next_diff.append(nbrs[i + 1] - nbrs[i])
		all_zero &= next_diff[-1] == 0

	digit = 0

	if not(all_zero):
		digit = get_next_number(next_diff)

	return nbrs[-1] + digit

def get_previous_number(nbrs):
	next_diff = []
	all_zero = True

	for i in range(len(nbrs) - 1):
		next_diff.append(nbrs[i + 1] - nbrs[i])
		all_zero &= next_diff[-1] == 0

	digit = 0

	if not(all_zero):
		digit = get_previous_number(next_diff)

	return nbrs[0] - digit

def level1(input):
	# Test value
	# input = '0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45\n'
	result = 0
	for line in input.strip().split('\n'):
		nbrs = [int(x) for x in regex.findall(r'-?\d+', line)]
		result += get_next_number(nbrs)

	return result

def level2(input):
	# Test value
	# input = '0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45\n'
	result = 0
	for line in input.strip().split('\n'):
		nbrs = [int(x) for x in regex.findall(r'-?\d+', line)]
		result += get_previous_number(nbrs)

	return result