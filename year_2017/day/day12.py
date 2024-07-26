#!/usr/bin/python

import re as regex

def define_group(links, index, group=[]):
	group += [index]

	for new_index in links[index]:
		if new_index in group:
			continue

		define_group(links, new_index, group)

	return group

def level1(input):
	# Test value
	# input = '0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5\n'
	tmp = [x.split('<->')[1] for x in input.strip().split('\n')]
	links = []
	for current in tmp:
		links.append([int(x) for x in regex.findall(r'\d+', current)])

	return len(define_group(links, 0))

def level2(input):
	# Test value
	# input = '0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5\n'
	tmp = [x.split('<->')[1] for x in input.strip().split('\n')]
	links = []
	for current in tmp:
		links.append([int(x) for x in regex.findall(r'\d+', current)])

	found = []
	nbr_group = 0

	for i in range(len(links)):
		if i in found:
			continue

		found += define_group(links, i)
		nbr_group += 1

	return nbr_group