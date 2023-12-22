#!/usr/bin/python

import math

def index_terrain(pos):
	return str(pos[0]) + '/' + str(pos[1])

def start_pos(cmds):
	min_vert = 0
	max_vert = 0
	min_hori = 0
	max_hori = 0
	vert = 0
	hori = 0
	for cmd in cmds:
		tmp = cmd.split(' ')
		direction = tmp[0]
		step = int(tmp[1])

		if direction == 'U':
			vert -= step
			min_vert = min(min_vert, vert)
		elif direction == 'R':
			hori += step
			max_hori = max(max_hori, hori)
		elif direction == 'D':
			vert += step
			max_vert = max(max_vert, vert)
		else:
			hori -= step
			min_hori = min(min_hori, hori)

	return [abs(min_vert), abs(min_hori)], (max_vert - min_vert + 1), (max_hori - min_hori + 1)

def start_pos_hexa(cmds):
	min_vert = 0
	max_vert = 0
	min_hori = 0
	max_hori = 0
	vert = 0
	hori = 0
	for cmd in cmds:
		step, direction = convert_hexa(cmd.split(' ')[2])

		if direction == 'U':
			vert -= step
			min_vert = min(min_vert, vert)
		elif direction == 'R':
			hori += step
			max_hori = max(max_hori, hori)
		elif direction == 'D':
			vert += step
			max_vert = max(max_vert, vert)
		else:
			hori -= step
			min_hori = min(min_hori, hori)

	return [abs(min_vert), abs(min_hori)], (max_vert - min_vert + 1), (max_hori - min_hori + 1)

def convert_hexa(hexa):
	hexa = hexa.replace('(', '').replace(')', '').replace('#', '')
	direction = ''

	if hexa[-1] == '0':
		direction = 'R'
	elif hexa[-1] == '1':
		direction = 'D'
	elif hexa[-1] == '2':
		direction = 'L'
	else:
		direction = 'U'

	return int(hexa[:-1], 16), direction

def display_terrain(terrain):
	for line in terrain:
		print(''.join(line))

def count_holes(terrain):
	result = 0
	for line in terrain:
		result += line.count('#')

	return result

def level1(input):
	# Test value
	# input = 'R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)\n'
	cmds = input.strip().split('\n')
	pos, max_x, max_y = start_pos(cmds)

	char = '#'
	last_direction = ''
	terrain = {}
	index_edge = []

	for i in range(max_x):
		index_edge.append([])

	for cmd in cmds:
		tmp = cmd.split(' ')
		tmp_dir = tmp[0]
		step = int(tmp[1])
		direction = []

		if tmp_dir == 'U':
			direction = [-1, 0]
			terrain[index_terrain(pos)] = 'U'
			index_edge[pos[0]].append(pos[1])
			char = '#'
		elif tmp_dir == 'R':
			direction = [0, 1]
			char = '-'
		elif tmp_dir == 'D':
			direction = [1, 0]
			terrain[index_terrain(pos)] = 'D'
			index_edge[pos[0]].append(pos[1])
			char = '#'
		else:
			direction = [0, -1]
			char = '-'

		if last_direction == 'U':
			terrain[index_terrain(pos)] = 'D'
			index_edge[pos[0]].append(pos[1])
		elif last_direction == 'D':
			terrain[index_terrain(pos)] = 'U'
			index_edge[pos[0]].append(pos[1])

		last_direction = tmp_dir

		if char == '-':
			pos[1] += direction[1] * step
		else:
			for i in range(step):
				pos[0] += direction[0]
				pos[1] += direction[1]
				terrain[index_terrain(pos)] = char
				index_edge[pos[0]].append(pos[1])


	if last_direction == 'U':
		terrain[index_terrain(pos)] = 'D'
		index_edge[pos[0]].append(pos[1])
	elif last_direction == 'D':
		terrain[index_terrain(pos)] = 'U'
		index_edge[pos[0]].append(pos[1])

	for i in range(len(index_edge)):
		index_edge[i] = sorted(list(set(index_edge[i])))

	result = 0

	for i in range(max_x):
		compt = False
		last_turn = ''
		already_compt = False
		for x in range(len(index_edge[i]) - 1):
			j = index_edge[i][x]
			j_sup = index_edge[i][x + 1]

			terrain_char = terrain[index_terrain([i, j])]
			if terrain_char == '#':
				compt = not(compt)
			elif terrain_char == 'U' or terrain_char == 'D':
				if last_turn == '':
					last_turn = terrain_char
				else:
					if last_turn != terrain_char:
						compt = not(compt)
					last_turn = ''

			if compt or last_turn != '':
				result += (j_sup - j)
				if not(already_compt):
					result += 1
					already_compt = True
			else:
				already_compt = False

	return result

def level2(input):
	# Test value
	# input = 'R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)\n'
	print('Exec long')
	print('Init step')
	cmds = input.strip().split('\n')
	pos, max_x, max_y = start_pos_hexa(cmds)

	char = '#'
	last_direction = ''
	terrain = {}
	index_edge = []

	for i in range(max_x):
		index_edge.append([])

	print('Perform edge')
	tenth = math.floor(len(cmds) / 10)
	percent = 0

	for i in range(len(cmds)):
		if i % tenth == 0:
			print(str(percent * 10) + '% executed')
			percent += 1
		cmd = cmds[i]
		step, tmp_dir = convert_hexa(cmd.split(' ')[2])
		direction = []

		if tmp_dir == 'U':
			direction = [-1, 0]
			terrain[index_terrain(pos)] = 'U'
			index_edge[pos[0]].append(pos[1])
			char = '#'
		elif tmp_dir == 'R':
			direction = [0, 1]
			char = '-'
		elif tmp_dir == 'D':
			direction = [1, 0]
			terrain[index_terrain(pos)] = 'D'
			index_edge[pos[0]].append(pos[1])
			char = '#'
		else:
			direction = [0, -1]
			char = '-'

		if last_direction == 'U':
			terrain[index_terrain(pos)] = 'D'
			index_edge[pos[0]].append(pos[1])
		elif last_direction == 'D':
			terrain[index_terrain(pos)] = 'U'
			index_edge[pos[0]].append(pos[1])

		last_direction = tmp_dir

		if char == '-':
			pos[1] += direction[1] * step
		else:
			for i in range(step):
				pos[0] += direction[0]
				pos[1] += direction[1]
				terrain[index_terrain(pos)] = char
				index_edge[pos[0]].append(pos[1])


	if last_direction == 'U':
		terrain[index_terrain(pos)] = 'D'
		index_edge[pos[0]].append(pos[1])
	elif last_direction == 'D':
		terrain[index_terrain(pos)] = 'U'
		index_edge[pos[0]].append(pos[1])

	print('------')
	print('Sort index edge')

	for i in range(len(index_edge)):
		index_edge[i] = sorted(list(set(index_edge[i])))

	result = 0

	print('Calcul lake size on ' + str(max_x) + ' lines')
	tenth = math.floor(max_x / 10)
	percent = 0

	for i in range(max_x):
		if i % tenth == 0:
			print(str(percent * 10) + '% executed')
			percent += 1
		compt = False
		last_turn = ''
		already_compt = False
		for x in range(len(index_edge[i]) - 1):
			j = index_edge[i][x]
			j_sup = index_edge[i][x + 1]

			terrain_char = terrain[index_terrain([i, j])]
			if terrain_char == '#':
				compt = not(compt)
			elif terrain_char == 'U' or terrain_char == 'D':
				if last_turn == '':
					last_turn = terrain_char
				else:
					if last_turn != terrain_char:
						compt = not(compt)
					last_turn = ''

			if compt or last_turn != '':
				result += (j_sup - j)
				if not(already_compt):
					result += 1
					already_compt = True
			else:
				already_compt = False

	return result