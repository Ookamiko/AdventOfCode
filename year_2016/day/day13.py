#!/usr/bin/python

import sys

def create_maze(magic_nb, max_nb, start_pos_x, start_pos_y):
	maze = []
	for y in range(max_nb):
		corridor = []
		for x in range(max_nb):
			if start_pos_x == x and start_pos_y == y:
				corridor.append('0')
				continue
			calc = x*x + 3*x + 2*x*y + y + y*y + magic_nb
			binary = format(calc, 'b')
			if binary.count('1') % 2 == 0:
				corridor.append('.')
			else:
				corridor.append('#')
		maze.append(corridor)

	return maze

def create_weighted_maze(magic_nb, max_nb, start_pos_x, start_pos_y):
	maze = []
	for y in range(max_nb):
		corridor = []
		for x in range(max_nb):
			if start_pos_x == x and start_pos_y == y:
				corridor.append(0)
				continue
			calc = x*x + 3*x + 2*x*y + y + y*y + magic_nb
			binary = format(calc, 'b')
			if binary.count('1') % 2 == 0:
				corridor.append(sys.maxsize)
			else:
				corridor.append(-1)
		maze.append(corridor)

	return maze

def update_maze(maze, x_current, y_current):
	maze_cpy = []
	for y in range(len(maze)):
		corridor = []
		for x in range(len(maze[y])):
			if x == x_current and y == y_current:
				corridor.append('0')
			else:
				corridor.append(maze[y][x])
		maze_cpy.append(corridor)

	return maze_cpy

def get_new_pos(maze, x_pos, y_pos):
	new_positions = []

	if x_pos - 1 >= 0 and maze[y_pos][x_pos - 1] == '.':
		new_positions.append([x_pos - 1, y_pos])
	if y_pos - 1 >= 0 and maze[y_pos - 1][x_pos] == '.':
		new_positions.append([x_pos, y_pos - 1])
	if x_pos + 1 < len(maze) and maze[y_pos][x_pos + 1] == '.':
		new_positions.append([x_pos + 1, y_pos])
	if y_pos + 1 < len(maze) and maze[y_pos + 1][x_pos] == '.':
		new_positions.append([x_pos, y_pos + 1])

	return new_positions

def get_new_pos_weigthed(maze, x_pos, y_pos, step):
	new_positions = []

	if x_pos - 1 >= 0 and maze[y_pos][x_pos - 1] > step:
		new_positions.append([x_pos - 1, y_pos])
	if y_pos - 1 >= 0 and maze[y_pos - 1][x_pos] > step:
		new_positions.append([x_pos, y_pos - 1])
	if x_pos + 1 < len(maze) and maze[y_pos][x_pos + 1] > step:
		new_positions.append([x_pos + 1, y_pos])
	if y_pos + 1 < len(maze) and maze[y_pos + 1][x_pos] > step:
		new_positions.append([x_pos, y_pos + 1])

	return new_positions

def find_fast_route(maze, x_pos, y_pos, x_to_found, y_to_found, step, max_step):
	if step >= max_step:
		return -1

	if x_to_found == x_pos and y_to_found == y_pos:
		return step

	new_positions = get_new_pos(maze, x_pos, y_pos)
	min_found = max_step

	for current in new_positions:
		tmp = find_fast_route(update_maze(maze, current[0], current[1]), current[0], current[1], x_to_found, y_to_found, step + 1, min_found)
		if tmp != -1:
			min_found = min(min_found, tmp)

	return min_found

def weighted_route(maze, x_pos, y_pos, step):
	maze[y_pos][x_pos] = step

	new_positions = get_new_pos_weigthed(maze, x_pos, y_pos, step)

	for current in new_positions:
		weighted_route(maze, current[0], current[1], step + 1)

def display_maze(maze):
	for current in maze:
		print('\t'.join([str(x) for x in current]))

def count_zone_at_most(maze, max_step):
	result = 0

	for corridor in maze:
		for zone in corridor:
			if zone >= 0 and zone <= max_step:
				result += 1

	return result

def level1(input):
	maze = create_maze(int(input.strip()), 50, 1, 1)
	#maze = create_maze(10, 10, 1, 1)
	result = find_fast_route(maze, 1, 1, 31, 39, 0, len(maze) * len(maze))
	return result

def level2(input):
	maze = create_weighted_maze(int(input.strip()), 100, 1, 1)
	#maze = create_weighted_maze(10, 10, 1, 1)
	weighted_route(maze, 1, 1, 0)
	return count_zone_at_most(maze, 50)