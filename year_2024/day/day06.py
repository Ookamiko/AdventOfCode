#!/usr/bin/python

import math

def level1(input):
	#input = '....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...\n'

	maps = [x for x in input.replace('\n', '')]
	size = int(math.sqrt(len(maps)))
	move = -size
	pos = maps.index('^')
	maps[pos] = 'X'
	valid = True

	while valid:
		if (pos + move < 0 or
			pos + move >= len(maps) or
			(move == -1 and pos % size == 0) or
			(move == 1 and pos % size == size - 1)
		):
			valid = False
		elif maps[pos + move] == '#':
			if move == -1:
				move = -size
			elif move == 1:
				move = size
			elif move == size:
				move = -1
			else:
				move = 1
		else:
			pos += move
			maps[pos] = 'X'

	return maps.count('X')

def level2(input):
	return "Not implemented"