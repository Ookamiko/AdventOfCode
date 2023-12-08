#!/usr/bin/python

import math

def flip_horizontal(design):
	to_return = ''
	if len(design) == 4:
		to_return = design[2:] + design[:2]
	else:
		to_return = design[6:] + design[3:6] + design[:3]

	return to_return

def flip_vertical(design):
	to_return = ''
	if len(design) == 4:
		tmp_1 = design[:2]
		tmp_2 = design[2:]
		to_return = tmp_1[::-1] + tmp_2[::-1]
	else:
		tmp_1 = design[:3]
		tmp_2 = design[3:6]
		tmp_3 = design[6:]
		to_return = tmp_1[::-1] + tmp_2[::-1] + tmp_3[::-1]

	return to_return

def rotate_clockwise(design):
	to_return = ''
	if len(design) == 4:
		tmp_1 = design[::2]
		tmp_2 = design[1::2]
		to_return = tmp_1[::-1] + tmp_2[::-1]
	else:
		tmp_1 = design[::3]
		tmp_2 = design[1::3]
		tmp_3 = design[2::3]
		to_return = tmp_1[::-1] + tmp_2[::-1] + tmp_3[::-1]

	return to_return

def display_design(design):
	size = int(math.sqrt(len(design)))

	for i in range(size):
		print(design[size * i: size * (i + 1)])

def get_all_permutation(design):
	work = design
	to_return = []

	for i in range(4):
		to_return.append(work)
		to_return.append(flip_horizontal(work))
		to_return.append(flip_vertical(work))
		work = rotate_clockwise(work)

	return list(set(to_return))

def divide_display(display):
	size = int(math.sqrt(len(display)))
	jump = 0

	if size % 2 == 0:
		jump = 2
	else:
		jump = 3

	to_return = []

	for i in range(size // jump):
		for j in range(size // jump):
			index = (i * size + j) * jump
			square = display[index:index + jump] # First line
			index += size
			square += display[index:index + jump] # Second line
			if jump == 3:
				index += size
				square += display[index:index + jump]

			to_return.append(square)

	return to_return

def reassemble_display(separations):
	size = int(math.sqrt(len(separations)))
	internal_size = int(math.sqrt(len(separations[0])))
	result = ''

	for i in range(size):
		sub_tab = separations[size * i:size * (i + 1)]
		for j in range(internal_size):
			index = j * internal_size
			for tab in sub_tab:
				result += tab[index:index + internal_size]

	return result

def level1(input):
	# Test value
	# input = '../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#\n'
	display = '.#...####'
	map_book = {}

	for current in input.strip().split('\n'):
		tmp = current.split(' => ')
		for permut in get_all_permutation(tmp[0].replace('/', '')):
			map_book[permut] = tmp[1].replace('/', '')

	for x in range(5):
		separations = divide_display(display)

		for i in range(len(separations)):
			separations[i] = map_book[separations[i]]

		display = reassemble_display(separations)

	display_design(display)
	return display.count('#')

def level2(input):
	# Test value
	# input = '../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#\n'
	display = '.#...####'
	map_book = {}

	for current in input.strip().split('\n'):
		tmp = current.split(' => ')
		for permut in get_all_permutation(tmp[0].replace('/', '')):
			map_book[permut] = tmp[1].replace('/', '')

	for x in range(18):
		separations = divide_display(display)

		for i in range(len(separations)):
			separations[i] = map_book[separations[i]]

		display = reassemble_display(separations)

	display_design(display)
	return display.count('#')