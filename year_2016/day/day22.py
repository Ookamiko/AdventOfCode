#!/usr/bin/python

import re as regex
import sys

def init_grid(instructions):
	grid = []
	x = 0
	row = []
	for line in instructions:
		numbers = [int(x) for x in regex.findall(r'\d+', line)]

		if numbers[0] != x:
			grid.append(row)
			row = []
			x = numbers[0]

		row.append({'size': numbers[2], 'used': numbers[3], 'avail': numbers[4]})

	grid.append(row)

	return grid

def init_grid_minimum(instructions):
	grid = []
	x = 0
	row = []
	start = []
	for line in instructions:
		numbers = [int(x) for x in regex.findall(r'\d+', line)]

		if numbers[0] != x:
			grid.append(row)
			row = []
			x = numbers[0]

		if numbers[3] == 0:
			start = [numbers[0], numbers[1]]
			row.append({'char': '.', 'step': 0})
		else:
			row.append({'char': '.' if numbers[3] <= 80 and numbers[2] >= 80 else '#', 'step': sys.maxsize})

	grid.append(row)

	return grid, start, [x - 1, 0]


def get_viable_pairs(grid):
	pairs = []

	for i in range(len(grid) * len(grid[0])):
		x1 = i // len(grid[0])
		y1 = i % len(grid[0])

		for j in range(len(grid) * len(grid[0])):
			x2 = j // len(grid[0])
			y2 = j % len(grid[0])

			if grid[x1][y1]['used'] == 0 or i == j:
				continue

			if grid[x1][y1]['used'] <= grid[x2][y2]['avail']:
				pairs.append([grid[x1][y1], grid[x2][y2]])

	return pairs

def get_target(grid, data_pos):
	if data_pos[0] == 0:
		return [0, data_pos[1] - 1]
	elif grid[data_pos[0] - 1][data_pos[1]]['size'] < 100:
		return [data_pos[0] - 1, data_pos[1]]

def get_start_pos(grid):
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			if grid[x][y]['used'] == 0:
				return [x, y]

def find_less_step(grid, pos, data_pos, step, max_step):
	if step >= max_step:
		return -1

	if data_pos[0] == 0 and data_pos[1] == 0:
		return step

	target_pos = get_target(grid, data_pos)
	next_pos = get_next_pos(grid, pos, step)

def display_grid(grid, target):
	for x in range(len(grid)):
		line = ''
		for y in range(len(grid[0])):
			if x == target[0] and y == target[1]:
				line += '+'
			else:
				line += grid[x][y]['char']
		print(line)

def get_next_pos(grid, pos, step):
	next_pos = []

	if pos[0] - 1 >= 0:
		next_pos.append([pos[0] - 1, pos[1]])
	if pos[0] + 1 < len(grid):
		next_pos.append([pos[0] + 1, pos[1]])
	if pos[1] - 1 >= 0:
		next_pos.append([pos[0], pos[1] - 1])
	if pos[1] + 1 < len(grid[0]):
		next_pos.append([pos[0], pos[1] + 1])

	good_pos = []

	for current in next_pos:
		if grid[current[0]][current[1]]['char'] != '.' or grid[current[0]][current[1]]['step'] <= step:
			continue

		good_pos.append(current)
		grid[current[0]][current[1]]['step'] = step

	return good_pos

def dist(pos, target):
	return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

def find_less_step(grid, pos, target, step, max_step):
	if step >= max_step:
		return -1

	if pos[0] == target[0] and pos[1] == target[1]:
		return step

	next_pos = get_next_pos(grid, pos, step + 1)
	next_pos.sort(key=lambda x: dist(x, target))

	min_found = max_step

	for current in next_pos:
		tmp_min = find_less_step(grid, current, target, step + 1, min_found)
		if tmp_min != -1:
			min_found = min(min_found, tmp_min)

	return min_found

def level1(input):
	grid = init_grid(input.strip().split('\n')[2:])
	viable_pairs = get_viable_pairs(grid)
	return len(viable_pairs)

def level2(input):
	grid, start_pos, target = init_grid_minimum(input.strip().split('\n')[2:])
	min_step = find_less_step(grid, start_pos, target, 0, len(grid) * len(grid[0]))
	return min_step + 1 + (len(grid) - 2) * 5