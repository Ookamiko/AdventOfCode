#!/usr/bin/python
import re as regex

def level1(input):
	#input = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n'
	left = []
	right = []
	for line in input.strip().split('\n'):
		matches = regex.match(r'(\d+)\s+(\d+)', line)
		if matches:
			left.append(int(matches.groups()[0]))
			right.append(int(matches.groups()[1]))

	left.sort()
	right.sort()
	total = 0

	for i in range(min(len(left), len(right))):
		total += abs(left[i] - right[i])

	return total

def level2(input):
	#input = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n'
	left = []
	right = []
	for line in input.strip().split('\n'):
		matches = regex.match(r'(\d+)\s+(\d+)', line)
		if matches:
			left.append(int(matches.groups()[0]))
			right.append(int(matches.groups()[1]))

	numbers = list(set(left))
	total = 0

	for test in numbers:
		total += test * left.count(test) * right.count(test)

	return total