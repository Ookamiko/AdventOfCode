#!/usr/bin/python

import re as regex

def level1(input):
	#input = '#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2\n'

	table = []
	for i in range(2000):
		table.append([0] * 2000)

	overlapping = 0

	for line in input.strip().split('\n'):
		s = [int(x) for x in regex.findall(r'(\d+)', line)]

		for i in range(s[1], s[1] + s[3]):
			for j in range(s[2], s[2] + s[4]):
				if (table[i][j] == 1):
					overlapping += 1
				table[i][j] += 1

	return overlapping

def level2(input):
	#input = '#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2\n'

	table = []
	for i in range(2000):
		table.append([0] * 2000)

	not_overlapping = []

	for line in input.strip().split('\n'):
		s = [int(x) for x in regex.findall(r'(\d+)', line)]

		not_overlapping.append(s[0])
		overlap_with = []

		for i in range(s[1], s[1] + s[3]):
			for j in range(s[2], s[2] + s[4]):
				if (table[i][j] != 0):
					overlap_with.append(table[i][j])
				table[i][j] = s[0]

		if len(overlap_with) > 0:
			not_overlapping.remove(s[0])
			for i in overlap_with:
				if i in not_overlapping:
					not_overlapping.remove(i)

	return not_overlapping[0]