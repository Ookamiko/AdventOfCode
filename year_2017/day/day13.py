#!/usr/bin/python

import re as regex

def is_caught(time, rang):
	cycle = (rang - 1) * 2
	return cycle > 0 and (time % cycle) == 0

def level1(input):
	# Test value
	# input = '0: 3\n1: 2\n4: 4\n6: 4\n'
	tmp = input.strip().split('\n')
	firewall = []
	for current in tmp:
		firewall.append([int(x) for x in regex.findall(r'\d+', current)])

	start = 0
	result = 0

	for layer in firewall:
		if is_caught(start + layer[0], layer[1]):
			result += layer[0] * layer[1]

	return result

def level2(input):
	# Test value
	# input = '0: 3\n1: 2\n4: 4\n6: 4\n'
	tmp = input.strip().split('\n')
	firewall = []
	for current in tmp:
		firewall.append([int(x) for x in regex.findall(r'\d+', current)])

	start = 0
	safe = False

	while not(safe):
		start += 1
		safe = True
		for layer in firewall:
			if is_caught(start + layer[0], layer[1]):
				safe = False
				break

	return start