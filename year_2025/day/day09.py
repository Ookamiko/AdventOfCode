#!/usr/bin/python

import math

DIR_UP = 1
DIR_DOWN = DIR_UP * -1
DIR_RIGHT = 2
DIR_LEFT = DIR_RIGHT * -1

def get_bigest_rect(pos):
	result = 0

	for i in range(len(pos) - 1):
		for j in range(i + 1, len(pos)):

			area = (abs(pos[i][0] - pos[j][0]) + 1) * (abs(pos[i][1] - pos[j][1]) + 1)

			result = max(result, area)

	return result

def get_bigest_rect_v2(pos, borders):
	result = 0

	for i in range(len(pos) - 1):
		for j in range(i + 1, len(pos)):
			# Line vert
			if pos[i][0] == pos[j][0]:
				if do_cross_borders([pos[i], pos[j]], borders['h']):
					continue
			# Line hor
			elif pos[i][1] == pos[j][1]:
				if do_cross_borders([pos[i], pos[j]], borders['v']):
					continue
			else:
				# Test hor segment
				h_segs = [
					[[pos[i][0], pos[i][1]], [pos[j][0], pos[i][1]]],
					[[pos[i][0], pos[j][1]], [pos[j][0], pos[j][1]]]
				]

				v_segs = [
					[[pos[i][0], pos[i][1]], [pos[i][0], pos[j][1]]],
					[[pos[j][0], pos[i][1]], [pos[j][0], pos[j][1]]]
				]

				if (do_cross_borders(h_segs[0], borders['v']) or
					do_cross_borders(h_segs[1], borders['v']) or
					do_cross_borders(v_segs[0], borders['h']) or
					do_cross_borders(v_segs[1], borders['h'])):
					continue

			area = (abs(pos[i][0] - pos[j][0]) + 1) * (abs(pos[i][1] - pos[j][1]) + 1)

			result = max(result, area)

	return result

def define_borders(corners, min_x):

	# search start position (min_x, lesser_y)
	for i in range(len(corners) - 1):
		if corners[i][0] == min_x:
			break

	start_index = 0

	if i == 0:
		if corners[0][0] == corners[1][0]:
			if corners[0][1] < corners[1][1]:
				start_index = 0
			else:
				start_index = 1
		elif corners[0][1] < corners[-1][1]:
			start_index = 0
		else:
			start_index = len(corners) - 1
	else:
		if corners[i][1] < corners[i + 1][1]:
			start_index = i
		else:
			start_index = i + 1

	# determine rotation of corners (clockwise or counter clockwise)

	d_from = 0

	if corners[start_index][0] == corners[start_index-1][0]:
		if corners[start_index][1] < corners[start_index-1][1]:
			d_from = DIR_DOWN
		else:
			d_from = DIR_UP
	else:
		d_from = DIR_RIGHT

	d_to = 0

	if start_index == len(corners) - 1:
		if corners[start_index][0] == corners[0][0]:
			if corners[start_index][1] < corners[0][1]:
				d_to = DIR_DOWN
			else:
				d_to = DIR_UP
		else:
			d_to = DIR_RIGHT
	elif corners[start_index][0] == corners[start_index + 1][0]:
		if corners[start_index][1] < corners[start_index + 1][1]:
			d_to = DIR_DOWN
		else:
			d_to = DIR_UP
	else:
		d_to = DIR_RIGHT

	is_clockwise = d_from == DIR_DOWN or d_to == DIR_UP

	# Define first "from"

	if corners[0][0] == corners[-1][0]:
		if corners[0][1] < corners[-1][1]:
			d_from = DIR_DOWN
		else:
			d_from = DIR_UP
	elif corners[0][0] < corners[-1][0]:
		d_from = DIR_RIGHT
	else:
		d_from = DIR_LEFT

	# Define all "border" segment
	borders = {"h": [], "v": []}

	c_pos = None
	first_pos = []

	for i in range(len(corners)):
		c = corners[i]
		n = corners[(i + 1) % len(corners)]
		n_pos = []

		if c[0] == n[0]:
			if c[1] < n[1]:
				d_to = DIR_DOWN
			else:
				d_to = DIR_UP
		elif c[0] < n[0]:
			d_to = DIR_RIGHT
		else:
			d_to = DIR_LEFT

		if is_clockwise:
			if d_from == DIR_UP:
				if d_to == DIR_RIGHT:
					n_pos = [c[0] + 1, c[1] - 1]
				else:
					n_pos = [c[0] + 1, c[1] + 1]
			elif d_from == DIR_DOWN:
				if d_to == DIR_RIGHT:
					n_pos = [c[0] - 1, c[1] - 1]
				else:
					n_pos = [c[0] - 1, c[1] + 1]
			elif d_from == DIR_LEFT:
				if d_to == DIR_DOWN:
					n_pos = [c[0] + 1, c[1] - 1]
				else:
					n_pos = [c[0] - 1, c[1] - 1]
			else:
				if d_to == DIR_DOWN:
					n_pos = [c[0] + 1, c[1] + 1]
				else:
					n_pos = [c[0] - 1, c[1] + 1]
		else:
			if d_from == DIR_UP:
				if d_to == DIR_RIGHT:
					n_pos = [c[0] - 1, c[1] + 1]
				else:
					n_pos = [c[0] - 1, c[1] - 1]
			elif d_from == DIR_DOWN:
				if d_to == DIR_RIGHT:
					n_pos = [c[0] + 1, c[1] + 1]
				else:
					n_pos = [c[0] + 1, c[1] - 1]
			elif d_from == DIR_LEFT:
				if d_to == DIR_DOWN:
					n_pos = [c[0] - 1, c[1] + 1]
				else:
					n_pos = [c[0] + 1, c[1] + 1]
			else:
				if d_to == DIR_DOWN:
					n_pos = [c[0] - 1, c[1] - 1]
				else:
					n_pos = [c[0] + 1, c[1] - 1]

		if c_pos != None:
			if c_pos[0] == n_pos[0]:
				if c_pos[1] < n_pos[1]:
					borders['v'].append([c_pos, n_pos])
				else:
					borders['v'].append([n_pos, c_pos])
			elif c_pos[0] < n_pos[0]:
				borders['h'].append([c_pos, n_pos])
			else:
				borders['h'].append([n_pos, c_pos])
		else:
			first_pos = [n_pos[0], n_pos[1]]

		c_pos = [n_pos[0], n_pos[1]]
		d_from = d_to * -1

	if c_pos[0] == first_pos[0]:
		if c_pos[1] < first_pos[1]:
			borders['v'].append([c_pos, first_pos])
		else:
			borders['v'].append([first_pos, c_pos])
	elif c_pos[0] < first_pos[0]:
		borders['h'].append([c_pos, first_pos])
	else:
		borders['h'].append([first_pos, c_pos])

	# sort border from low to high id
	borders['h'] = sorted(borders['h'], key=lambda x: x[0][1])
	borders['v'] = sorted(borders['v'], key=lambda x: x[0][0])

	return borders

def do_cross_borders(line, borders):
	check_v = 0
	min_v = 0
	max_v = 0

	same_i = 0
	diff_i = 0

	if line[0][0] == line[1][0]:
		check_v = line[0][0]
		min_v = min(line[0][1], line[1][1])
		max_v = max(line[0][1], line[1][1])
		same_i = 0
		diff_i = 1
	else:
		check_v = line[0][1]
		min_v = min(line[0][0], line[1][0])
		max_v = max(line[0][0], line[1][0])
		same_i = 1
		diff_i = 0

	for current in borders:
		if current[0][diff_i] < min_v:
			continue
		elif current[0][diff_i] > max_v:
			break

		patron_dist = abs(current[0][same_i] - current[1][same_i])
		test_dist = abs(current[0][same_i] - check_v) + abs(current[1][same_i] - check_v)

		if test_dist == patron_dist:
			return True

	return False


def level1(input):
	#input = '7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3\n'

	red_lights = []

	for n_pos in input.strip().split('\n'):
		red_lights.append([int(x) for x in n_pos.split(',')])

	return get_bigest_rect(red_lights)

def level2(input):
	#input = '7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3\n'

	red_lights = []

	min_x = math.inf

	for n_pos in input.strip().split('\n'):
		c = [int(x) for x in n_pos.split(',')]
		red_lights.append(c)
		min_x = min(min_x, c[0])

	borders = define_borders(red_lights, min_x)

	return get_bigest_rect_v2(red_lights, borders)