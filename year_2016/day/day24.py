#!/usr/bin/python

import sys

def init_map(instructions):
	hmap = []
	location = []

	for x in range(len(instructions)):
		row = []
		for y in range(len(instructions[x])):
			row.append({'char': instructions[x][y], 'step': sys.maxsize})
			if instructions[x][y] != '.' and instructions[x][y] != '#':
				row[y] = {'char': '.', 'step': sys.maxsize}
				location.append({'id': int(instructions[x][y]), 'pos': [x,y], 'dist': []})
		hmap.append(row)

	location.sort(key=lambda x: x['id'])

	for loc in location:
		loc['dist'] = [-1] * len(location)

	return hmap, location

def display_map(hmap):
	for row in hmap:
		line = ''
		for elem in row:
			line += elem['char']
		print(line)

def display_map_step(hmap, max_step):
	for row in hmap:
		line = ''
		for elem in row:
			if elem['char'] == '#':
				line += elem['char'] + '\t'
			else:
				line += str(elem['step'] % max_step) + '\t'

		print(line.strip())

def reset_map(hmap):
	for row in hmap:
		for elem in row:
			elem['step'] = sys.maxsize

def get_next_pos(hmap, pos, step):
	next_pos = [
		[pos[0] - 1, pos[1]],
		[pos[0] + 1, pos[1]],
		[pos[0], pos[1] - 1],
		[pos[0], pos[1] + 1],
	]

	good_pos = []

	for current in next_pos:
		if hmap[current[0]][current[1]]['char'] != '#' and hmap[current[0]][current[1]]['step'] > step:
			good_pos.append(current)

	return good_pos

def cartograph_map(hmap, pos, step, max_step):
	hmap[pos[0]][pos[1]]['step'] = step

	if step >= max_step:
		return -1

	next_pos = get_next_pos(hmap, pos, step + 1)

	for current in next_pos:
		cartograph_map(hmap, current, step + 1, max_step)

def permutation(array):
	result = []

	if len(array) == 1:
		result.append(array)
	else:
		for i in range(len(array)):
			for permut in permutation(array[:i] + array[i+1:]):
				result.append([array[i]] + permut)

	return result

def calc_min_path(location, all_permut):
	result = sys.maxsize

	for permut in all_permut:
		tmp = 0
		for i in range(len(permut) - 1):
			tmp += location[permut[i]]['dist'][permut[i + 1]]

		result = min(tmp, result)

	return result

def level1(input):
	sys.setrecursionlimit(100000)
	#input = '###########\n#0.1.....2#\n#.#######.#\n#4.......3#\n###########\n'
	hmap, location = init_map(input.strip().split('\n'))

	for i in range(len(location) - 1):
		base = location[i]
		reset_map(hmap)
		cartograph_map(hmap, base['pos'], 0, len(hmap) * len(hmap[0]))
		for j in range(i + 1, len(location)):
			target = location[j]
			min_step = hmap[target['pos'][0]][target['pos'][1]]['step']
			base['dist'][j] = min_step
			target['dist'][i] = min_step

	all_permut = []
	for permut in permutation([x['id'] for x in location[1:]]):
		all_permut.append([0] + permut)

	return calc_min_path(location, all_permut)

def level2(input):
	sys.setrecursionlimit(100000)
	#input = '###########\n#0.1.....2#\n#.#######.#\n#4.......3#\n###########\n'
	hmap, location = init_map(input.strip().split('\n'))

	for i in range(len(location) - 1):
		base = location[i]
		reset_map(hmap)
		cartograph_map(hmap, base['pos'], 0, len(hmap) * len(hmap[0]))
		for j in range(i + 1, len(location)):
			target = location[j]
			min_step = hmap[target['pos'][0]][target['pos'][1]]['step']
			base['dist'][j] = min_step
			target['dist'][i] = min_step

	all_permut = []
	for permut in permutation([x['id'] for x in location[1:]]):
		all_permut.append([0] + permut + [0])

	return calc_min_path(location, all_permut)