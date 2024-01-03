#!/usr/bin/python

import math, sys

def display_garden(garden, in_file=False):
	f = open('test.txt', 'w')
	for i in range(len(garden)):
		line = ''
		for j in range(len(garden[0])):
			if in_file:
				line += str(garden[i][j]) + '\t'
			else:
				line += str(garden[i][j]) + '\t'

		if in_file:
			f.write(line + '\n')
		else:
			print(line)

	f.close()

def count_even(garden):
	result = 0

	for i in range(len(garden)):
		for j in range(len(garden[i])):
			if garden[i][j] != '.' and garden[i][j] != '#' and garden[i][j] % 2 == 0:
				result += 1

	return result

def count_even_spe(garden, vert, hori):
	nbr_vert = len(garden) // vert
	nbr_hori = len(garden[0]) // hori
	result = []
	for x in range(nbr_vert):
		line = []
		for y in range(nbr_hori):
			tmp = 0
			for i in range(x * vert, (x + 1) * vert):
				for j in range(y * hori, (y + 1) * hori):
					if garden[i][j] != '.' and garden[i][j] != '#' and garden[i][j] % 2 == 0:
						tmp += 1

			line.append(tmp)

		result.append(line)

	return result

def count_odd(garden):
	result = 0

	for i in range(len(garden)):
		for j in range(len(garden[i])):
			if garden[i][j] != '.' and garden[i][j] != '#' and garden[i][j] % 2 != 0:
				result += 1

	return result

def count_odd_spe(garden, vert, hori):
	nbr_vert = len(garden) // vert
	nbr_hori = len(garden[0]) // hori
	result = []
	for x in range(nbr_vert):
		line = []
		for y in range(nbr_hori):
			tmp = 0
			for i in range(x * vert, (x + 1) * vert):
				for j in range(y * hori, (y + 1) * hori):
					if garden[i][j] != '.' and garden[i][j] != '#' and garden[i][j] % 2 != 0:
						tmp += 1

			line.append(tmp)

		result.append(line)

	return result

def make_step(garden, poss, step, max_step):
	print(step, len(poss))
	if step == max_step:
		return

	available_pos = []

	for str_pos in poss:
		pos = [int(x) for x in str_pos.split(',')]

		if pos[0] - 1 >= 0 and garden[pos[0] - 1][pos[1]] == '.':
			if not(str(pos[0] - 1) + ',' + str(pos[1]) in available_pos):
				garden[pos[0] - 1][pos[1]] = step + 1
				available_pos.append(str(pos[0] - 1) + ',' + str(pos[1]))

		if pos[0] + 1 < len(garden) and garden[pos[0] + 1][pos[1]] == '.':
			if not(str(pos[0] + 1) + ',' + str(pos[1]) in available_pos):
				garden[pos[0] + 1][pos[1]] = step + 1
				available_pos.append(str(pos[0] + 1) + ',' + str(pos[1]))

		if pos[1] - 1 >= 0 and garden[pos[0]][pos[1] - 1] == '.':
			if not(str(pos[0]) + ',' + str(pos[1] - 1) in available_pos):
				garden[pos[0]][pos[1] - 1] = step + 1
				available_pos.append(str(pos[0]) + ',' + str(pos[1] - 1))

		if pos[1] + 1 < len(garden[0]) and garden[pos[0]][pos[1] + 1] == '.':
			if not(str(pos[0]) + ',' + str(pos[1] + 1) in available_pos):
				garden[pos[0]][pos[1] + 1] = step + 1
				available_pos.append(str(pos[0]) + ',' + str(pos[1] + 1))

	if (len(available_pos) != 0):
		make_step(garden, available_pos, step + 1, max_step)

def level1(input):
	# Test value
	# input = '...........\n.....###.#.\n.###.##..#.\n..#.#...#..\n....#.#....\n.##..S####.\n.##..#...#.\n.......##..\n.##.#.####.\n.##..##.##.\n...........\n'
	# max_step = 6
	max_step = 64
	garden = []
	pos = []
	lines = input.strip().split('\n')

	for i in range(len(lines)):
		line = lines[i]
		garden.append([x for x in line])
		if 'S' in line:
			pos = [i, line.index('S')]
			garden[pos[0]][pos[1]] = 0

	make_step(garden, [str(pos[0]) + ',' + str(pos[1])], 0, max_step)

	display_garden(garden, True)

	return count_even(garden)

def level2(input):
	# max_step = 501
	max_step = 26501365
	tmp_garden = []
	pos = []
	lines = input.strip().split('\n')

	for i in range(len(lines)):
		line = lines[i]
		tmp_garden.append([x for x in line])
		if 'S' in line:
			pos = [i, line.index('S')]
			tmp_garden[pos[0]][pos[1]] = '.'

	extend_vert = 0
	if max_step % len(tmp_garden) < len(tmp_garden) // 2:
		extend_vert = (max_step // len(tmp_garden)) * 2 + 1
	else:
		extend_vert = math.ceil(max_step / len(tmp_garden)) * 2 + 1

	extend_hori = 0
	if max_step % len(tmp_garden[0]) < len(tmp_garden[0]) // 2:
		extend_hori = (max_step // len(tmp_garden[0])) * 2 + 1
	else:
		extend_hori = math.ceil(max_step / len(tmp_garden[0])) * 2 + 1

	garden = []
	result = 0

	for i in range(2):
		for x in range(len(tmp_garden)):
			garden.append([x for x in ''.join(tmp_garden[x])])

	pos[0] = pos[0] + len(tmp_garden)
	garden[pos[0]][pos[1]] = 0

	make_step(garden, [str(pos[0]) + ',' + str(pos[1])], 0, max_step)

	count_center = count_odd(garden[len(tmp_garden):])
	count_out_center = count_odd(garden[:len(tmp_garden)])

	diamond_size = (extend_vert - 1) // 2 - 2

	if diamond_size % 2 == 0:
		times_center = diamond_size + 1
		for i in range(diamond_size, 0, -1):
			times_center += i * 2

		times_out_center = diamond_size
		for i in range(diamond_size - 1, 0, -1):
			times_out_center += i * 2
	else:
		times_center = diamond_size
		for i in range(diamond_size - 1, 0, -1):
			times_center += i * 2

		times_out_center = diamond_size + 1
		for i in range(diamond_size, 0, -1):
			times_out_center += i * 2

	result = count_center * times_center + count_out_center * times_out_center

	# Double Up
	garden = []
	for i in range(2):
		for x in range(len(tmp_garden)):
			garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + 1
	tmp_pos = [len(garden) - 1, len(garden[0]) // 2]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += count_odd(garden)

	# Double Down
	garden = []
	for i in range(2):
		for x in range(len(tmp_garden)):
			garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + 1
	tmp_pos = [0, len(garden[0]) // 2]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += count_odd(garden)

	# Double Left
	garden = []
	for x in range(len(tmp_garden)):
		line = ''
		for i in range(2):
			line += ''.join(tmp_garden[x])

		garden.append([x for x in line])

	step = diamond_size * len(tmp_garden[0]) + len(tmp_garden[0]) // 2 + 1
	tmp_pos = [len(garden) // 2, len(garden[0]) - 1]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += count_odd(garden)

	# Double Right
	garden = []
	for x in range(len(tmp_garden)):
		line = ''
		for i in range(2):
			line += ''.join(tmp_garden[x])

		garden.append([x for x in line])

	step = diamond_size * len(tmp_garden[0]) + len(tmp_garden[0]) // 2 + 1
	tmp_pos = [len(garden) // 2, 0]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += count_odd(garden)

	# Up Left Level 1
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = (diamond_size - 1) * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [len(garden) - 1, len(tmp_garden) - 1]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += diamond_size * count_odd(garden)

	# Up Left Level 2
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [len(garden) - 1, len(tmp_garden) - 1]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += (diamond_size + 1) * count_odd(garden)

	# Up Right Level 1
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = (diamond_size - 1) * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [len(garden) - 1, 0]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += diamond_size * count_odd(garden)

	# Up Right Level 2
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [len(garden) - 1, 0]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += (diamond_size + 1) * count_odd(garden)

	# Down Left Level 1
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = (diamond_size - 1) * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [0, len(tmp_garden) - 1]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += diamond_size * count_odd(garden)

	# Down Left Level 2
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [0, len(tmp_garden) - 1]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += (diamond_size + 1) * count_odd(garden)

	# Down Right Level 1
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = (diamond_size - 1) * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [0, 0]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += diamond_size * count_odd(garden)

	# Down Right Level 2
	garden = []
	for x in range(len(tmp_garden)):
		garden.append([x for x in ''.join(tmp_garden[x])])

	step = diamond_size * len(tmp_garden) + len(tmp_garden) // 2 + len(tmp_garden[0]) // 2 + 2
	tmp_pos = [0, 0]
	garden[tmp_pos[0]][tmp_pos[1]] = step
	make_step(garden, [str(tmp_pos[0]) + ',' + str(tmp_pos[1])], step, max_step)

	result += (diamond_size + 1) * count_odd(garden)

	return result