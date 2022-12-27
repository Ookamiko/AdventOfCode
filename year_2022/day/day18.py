#!/usr/bin/python

import re as regex
import sys

def init_cube(size):
	cube = []
	for i in range(size):
		tmp = []
		for j in range(size):
			tmp.append([False] * size)
		cube.append(tmp)
	return cube

def stringify_coord(coord):
	return coord[0] + coord[1] * 100 + coord[2] * 10000

def can_go_to_extern(cube, pos, seen, can_access_extern):
	if pos[0] == 0 or pos[0] == len(cube) - 1 or pos[1] == 0 or pos[1] == len(cube) - 1 or pos[2] == 0 or pos[2] == len(cube) - 1:
		return True

	result = False

	for next_pos in get_all_adjacent_pos(pos[0], pos[1], pos[2], len(cube)):
		tmp_string = stringify_coord(next_pos)
		if tmp_string in seen or cube[next_pos[0]][next_pos[1]][next_pos[2]]:
			continue

		if tmp_string in can_access_extern:
			result = True
			break

		seen.append(tmp_string)
		if can_go_to_extern(cube, next_pos, seen, can_access_extern):
			result = True
			break

	return result

def get_all_adjacent_pos(x, y, z, size):
	all_pos = []
	if x - 1 >= 0:
		all_pos.append([x - 1, y, z])
	if y - 1 >= 0:
		all_pos.append([x, y - 1, z])
	if z - 1 >= 0:
		all_pos.append([x, y, z - 1])
	if x + 1 < size:
		all_pos.append([x + 1, y, z])
	if y + 1 < size:
		all_pos.append([x, y + 1, z])
	if z + 1 < size:
		all_pos.append([x, y, z + 1])

	return all_pos

def level1(input):
	#input = '2,2,2\n1,2,2\n3,2,2\n2,1,2\n2,3,2\n2,2,1\n2,2,3\n2,2,4\n2,2,6\n1,2,5\n3,2,5\n2,1,5\n2,3,5\n'
	size = 25
	cube = init_cube(size)
	total_face = 0

	for drop in input.strip().split('\n'):
		x, y, z = [int(x) for x in regex.findall(r'\d+', drop)]
		face = 6
		for xn, yn, zn in get_all_adjacent_pos(x, y, z, size):
			if cube[xn][yn][zn]:
				face -= 2

		total_face += face
		cube[x][y][z] = True

	return total_face

def level2(input):
	sys.setrecursionlimit(10000)
	#input = '2,2,2\n1,2,2\n3,2,2\n2,1,2\n2,3,2\n2,2,1\n2,2,3\n2,2,4\n2,2,6\n1,2,5\n3,2,5\n2,1,5\n2,3,5\n'
	size = 25
	cube = init_cube(size)

	for drop in input.strip().split('\n'):
		x, y, z = [int(x) + 1 for x in regex.findall(r'\d+', drop)]
		cube[x][y][z] = True

	all_blank = []
	for x in range(size):
		for y in range(size):
			for z in range(size):
				if cube[x][y][z]:
					continue

				for xn, yn, zn in get_all_adjacent_pos(x, y, z, size):
					if cube[xn][yn][zn]:
						all_blank.append([x, y, z])
						break

	result = 0
	can_access_extern = []

	for i in range(len(all_blank)):
		pos = all_blank[i]
		print(str(i) + '\t/' + str(len(all_blank)))
		tmp_string = stringify_coord(pos)
		if can_go_to_extern(cube, pos, [tmp_string], can_access_extern):
			can_access_extern.append(tmp_string)
			for adjacent in get_all_adjacent_pos(pos[0], pos[1], pos[2], size):
				if cube[adjacent[0]][adjacent[1]][adjacent[2]]:
					result += 1

	return result