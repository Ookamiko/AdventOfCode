#!/usr/bin/python

import math

def display_table(table):
	for current in table:
		print(''.join(current))

def tilt_north(table, max_index):
	made_move = False
	for i in range(1, max_index):
		for j in range(len(table[0])):
			if table[i][j] == 'O' and table[i - 1][j] == '.':
				table[i - 1][j] = 'O'
				table[i][j] = '.'
				made_move = True

	return made_move

def tilt_south(table, max_index):
	made_move = False
	for i in range(len(table) - 2, max_index, -1):
		for j in range(len(table[0])):
			if table[i][j] == 'O' and table[i + 1][j] == '.':
				table[i + 1][j] = 'O'
				table[i][j] = '.'
				made_move = True

	return made_move

def tilt_west(table, max_index):
	made_move = False
	for j in range(1, max_index):
		for i in range(len(table)):
			if table[i][j] == 'O' and table[i][j - 1] == '.':
				table[i][j - 1] = 'O'
				table[i][j] = '.'
				made_move = True

	return made_move

def tilt_east(table, max_index):
	made_move = False
	for j in range(len(table[0]) - 2, max_index, -1):
		for i in range(len(table)):
			if table[i][j] == 'O' and table[i][j + 1] == '.':
				table[i][j + 1] = 'O'
				table[i][j] = '.'
				made_move = True

	return made_move

def make_cycle(table):
	offset = 0
	while tilt_north(table, len(table) - offset):
		offset += 1

	offset = 0
	while tilt_west(table, len(table[0]) - offset):
		offset += 1

	offset = -1
	while tilt_south(table, offset):
		offset += 1

	offset = -1
	while tilt_east(table, offset):
		offset += 1

def stringify_table(table):
	result = ''
	for line in table:
		result += ''.join(line)

	return result

def calc_weight(table):
	result = 0
	for i in range(len(table)):
		for j in range(len(table[0])):
			if table[i][j] == 'O':
				result += len(table) - i

	return result

def level1(input):
	# Test value
	# input = 'O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....\n'
	table = []
	for line in input.strip().split('\n'):
		table.append([x for x in line])

	offset = 0
	while tilt_north(table, len(table) - offset):
		offset += 1

	return calc_weight(table)

def level2(input):
	# Test value
	# input = 'O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....\n'
	table = []
	nbr_cycle = 1000000000
	for line in input.strip().split('\n'):
		table.append([x for x in line])

	found = [stringify_table(table)]
	display_table(table)

	start_index = 0
	step = 0

	for i in range(nbr_cycle):
		make_cycle(table)
		table_string = stringify_table(table)
		if table_string in found:
			start_index = found.index(table_string)
			step = (i + 1) - start_index
			break
		found.append(table_string)

	muli = math.floor((nbr_cycle - start_index) / step)
	max_index = start_index + step * muli

	for i in range(nbr_cycle - max_index):
		make_cycle(table)

	return calc_weight(table)