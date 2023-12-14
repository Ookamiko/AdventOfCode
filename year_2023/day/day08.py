#!/usr/bin/python

import re as regex
import math

def get_recursivite(maps, way, pos, end):
	result = []
	for current in pos:
		test_pos = current
		step = 0
		while not(test_pos in end):
			test_pos = maps[test_pos][way[step % len(way)]]
			step += 1

		result.append(step)

	return result


def level1(input):
	# Test value
	# input = 'LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)\n'
	tmp = input.strip().split('\n')
	way = tmp[0]
	maps = {}
	pos = 'AAA'
	end = 'ZZZ'
	ends = []
	step = 0

	for current in tmp[2:]:
		tmp_zone = regex.findall(r'[A-Z]+', current)
		maps[tmp_zone[0]] = {'L': tmp_zone[1], 'R': tmp_zone[2]}

	while pos != end:
		pos = maps[pos][way[step % len(way)]]
		step += 1

	return step

def get_ppcm(values):
	ppcm = 0
	values.sort()
	test = values[::-1]
	to_reach = test.pop(0)
	to_reach_add = to_reach
	while len(test) > 0:
		to_test = test.pop(0)
		to_test_add = to_test
		while to_test != to_reach:
			if to_test < to_reach:
				diff = to_reach - to_test
				to_test += to_test_add * math.ceil(diff / to_test_add)
			else:
				to_reach += to_reach_add

		print(to_reach)
		to_reach_add = to_reach

	return to_reach

def level2(input):
	# Test value
	# input = 'LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)\n'
	tmp = input.strip().split('\n')
	way = tmp[0]
	maps = {}
	pos = []
	ends = []
	step = 0

	for current in tmp[2:]:
		tmp_zone = regex.findall(r'[0-9A-Z]+', current)
		maps[tmp_zone[0]] = {'L': tmp_zone[1], 'R': tmp_zone[2]}

		if tmp_zone[0][2] == 'A':
			pos.append(tmp_zone[0])
		elif tmp_zone[0][2] == 'Z':
			ends.append(tmp_zone[0])

	recursivites = get_recursivite(maps, way, ['DNA', 'HNA', 'AAA', 'LMA', 'VGA', 'LLA'], ends)

	return get_ppcm(recursivites)