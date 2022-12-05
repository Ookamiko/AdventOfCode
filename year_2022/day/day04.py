#!/usr/bin/python

import re as regex

def level1(input):
	pairs = input.strip().split('\n')
	result = 0

	for pair in pairs:
		splits = [int(x) for x in regex.findall(r'\d+', pair)]

		if (splits[0] <= splits[2] and splits[1] >= splits[3]) or (splits[2] <= splits[0] and splits[3] >= splits[1]):
			result += 1

	return result

def level2(input):
	pairs = input.strip().split('\n')
	result = 0

	for pair in pairs:
		splits = [int(x) for x in regex.findall(r'\d+', pair)]

		if ((splits[0] >= splits[2] and splits[0] <= splits[3]) or
			(splits[1] >= splits[2] and splits[1] <= splits[3]) or
			(splits[2] >= splits[0] and splits[2] <= splits[1]) or
			(splits[3] >= splits[0] and splits[3] <= splits[1])
			):
			result += 1

	return result