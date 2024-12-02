#!/usr/bin/python

import array

def level1(input):
	lines = input.split('\n')
	result = 0
	for line in lines:
		if len(line) == 0:
			continue
		list_obj = line.split('x')
		size = sorted([int(list_obj[0]), int(list_obj[1]), int(list_obj[2])])
		result += 2 * (size[0] * size[1] + size[1] * size[2] + size[0] * size[2]) + size[0] * size[1]
	return str(result)

def level2(input):
	lines = input.split('\n')
	result = 0
	for line in lines:
		if len(line) == 0:
			continue
		list_obj = line.split('x')
		size = sorted([int(list_obj[0]), int(list_obj[1]), int(list_obj[2])])
		result += 2 * (size[0] + size[1]) + size[0] * size[1] * size[2]
	return str(result)