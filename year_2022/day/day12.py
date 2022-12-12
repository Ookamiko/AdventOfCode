#!/usr/bin/python

import sys

def init_map(lines):
	start = []
	end = []
	hmap = []
	for line in lines:
		row = [{'elev': x, 'step': sys.maxsize} for x in line]
		if 'S' in [x for x in line]:
			start = [len(hmap), [x for x in line].index('S')]
		if 'E' in [x for x in line]:
			end = [len(hmap), [x for x in line].index('E')]
		hmap.append(row)

	hmap[start[0]][start[1]]['elev'] = 'a'
	hmap[end[0]][end[1]]['elev'] = 'z'

	return hmap, start, end

def update_map(hmap, current_pos, step):
	new_map = []
	for x in range(len(hmap)):
		row = []
		for y in range(len(hmap[x])):
			row.append(hmap[x][y])
		new_map.append(row)
	new_map[current_pos[0]][current_pos[1]] = '.'

	return new_map

def position_value(hmap, position, end):
	dist = (abs(position[0] - end[0]) + abs(position[1] - end[1]))
	value = 1 / (dist if dist != 0 else 1)
	return value + (1000 * ord(hmap[position[0]][position[1]]['elev']))

def get_next_pos(hmap, cur_pos, end, step):
	tmp_pos = []
	max_elev = ord(hmap[cur_pos[0]][cur_pos[1]]['elev']) + 1

	# Priorize top over bottom
	tmp_pos.append([cur_pos[0] + 1, cur_pos[1]])
	tmp_pos.append([cur_pos[0], cur_pos[1] - 1])
	tmp_pos.append([cur_pos[0], cur_pos[1] + 1])
	tmp_pos.append([cur_pos[0] - 1, cur_pos[1]])

	good_pos = []

	for test in tmp_pos:
		if test[0] < 0 or test[0] >= len(hmap) or test[1] < 0 or test[1] >= len(hmap[0]) or hmap[test[0]][test[1]] == '.':
			continue

		if ord(hmap[test[0]][test[1]]['elev']) <= max_elev and step < hmap[test[0]][test[1]]['step']:
			good_pos.append(test)

	good_pos.sort(reverse=True, key=lambda x: position_value(hmap, x, end))

	return good_pos

def display_map(hmap):
	for line in hmap:
		str_line = ''
		for pos in line:
			if pos['step'] < sys.maxsize:
				str_line += '.'
			else:
				str_line += pos['elev']
		print(str_line)

def find_shortest_path(hmap, current_pos, end, step, max_step):
	if step >= max_step - (abs(current_pos[0] - end[0]) + abs(current_pos[1] - end[1])):
		return -1

	if current_pos[0] == end[0] and current_pos[1] == end[1]:
		return step

	hmap[current_pos[0]][current_pos[1]]['step'] = step

	next_pos = get_next_pos(hmap, current_pos, end, step + 1)

	min_found = max_step

	for pos in next_pos:
		tmp_min = find_shortest_path(hmap, pos, end, step + 1, min_found)
		if tmp_min != -1:
			min_found = min(min_found, tmp_min)

	return min_found

def level1(input):
	sys.setrecursionlimit(10000)
	#input = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi\n'
	hmap, start, end = init_map(input.strip().split('\n'))
	max_step = len(hmap) * len(hmap[0])
	min_found = find_shortest_path(hmap, start, end, 0, max_step)
	return min_found

def level2(input):
	sys.setrecursionlimit(10000)
	#input = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi\n'
	hmap, start, end = init_map(input.strip().split('\n'))
	min_found = len(hmap) * len(hmap[0])
	for x in range(len(hmap)):
		for y in range(len(hmap[0])):
			if hmap[x][y]['elev'] == 'a':
				min_found = min(min_found, find_shortest_path(hmap, [x,y], end, 0, min_found))
				print(min_found)

	return min_found