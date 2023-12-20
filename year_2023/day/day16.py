#!/usr/bin/python

def change_direction(direction, mirror):
	if mirror == '/':
		if direction[0] == 1:
			return [0, -1]
		elif direction[0] == -1:
			return [0, 1]
		elif direction[1] == 1:
			return [-1, 0]
		else:
			return [1, 0]
	else:
		if direction[0] == 1:
			return [0, 1]
		elif direction[0] == -1:
			return [0, -1]
		elif direction[1] == 1:
			return [1, 0]
		else:
			return [-1, 0]

def lightpath(maze, pos, direction, energize_map, direction_map):
	while True:
		if (pos[0] >= 0 and pos[0] < len(energize_map)
			and pos[1] >= 0 and pos[1] < len(energize_map[0])):
			energize_map[pos[0]][pos[1]] = '#'

			if abs(direction[0]) == 1:
				direction_map[pos[0]][pos[1]] = '|'
			else:
				direction_map[pos[0]][pos[1]] = '-'

		next_pos = [pos[0] + direction[0], pos[1] + direction[1]]

		if (next_pos[0] < 0 or next_pos[0] >= len(maze)
			or next_pos[1] < 0 or next_pos[1] >= len(maze[0])):
			# Go outside map
			break

		if (energize_map[next_pos[0]][next_pos[1]] == '#'
			and (
				(direction[0] != 0 and direction_map[next_pos[0]][next_pos[1]] == '|' and maze[next_pos[0]][next_pos[1]] == '.')
				or (direction[0] == 0 and direction_map[next_pos[0]][next_pos[1]] == '-' and maze[next_pos[0]][next_pos[1]] == '.')
				)
			):
			# Return on a light way already made
			break

		if maze[next_pos[0]][next_pos[1]] == '\\' or maze[next_pos[0]][next_pos[1]] == '/':
			direction = change_direction(direction, maze[next_pos[0]][next_pos[1]])
		elif maze[next_pos[0]][next_pos[1]] == '|' and direction[1] != 0:
			lightpath(maze, next_pos, [1, 0], energize_map, direction_map)
			lightpath(maze, next_pos, [-1, 0], energize_map, direction_map)
			break
		elif maze[next_pos[0]][next_pos[1]] == '-' and direction[0] != 0:
			lightpath(maze, next_pos, [0, 1], energize_map, direction_map)
			lightpath(maze, next_pos, [0, -1], energize_map, direction_map)
			break

		pos = next_pos

def display_maze(maze):
	for line in maze:
		print(''.join(line))

def level1(input):
	# Test value
	# input = '.|...\\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n.........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|....\n'
	maze = []
	energize_map = []
	direction_map = []
	for line in input.strip().split('\n'):
		energize_map.append(['.' for x in line])
		direction_map.append(['.' for x in line])
		maze.append([x for x in line])

	lightpath(maze, [0, -1], [0, 1], energize_map, direction_map)

	result = 0
	for line in energize_map:
		result += line.count('#')

	return result

def level2(input):
	# Test value
	# input = '.|...\\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n.........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|....\n'
	maze = []
	for line in input.strip().split('\n'):
		maze.append([x for x in line])

	result = 0

	for i in range(len(maze)):
		energize_map = []
		direction_map = []

		for line in maze:
			energize_map.append(['.' for x in line])
			direction_map.append(['.' for x in line])

		lightpath(maze, [i, -1], [0, 1], energize_map, direction_map)

		test_result = 0
		for line in energize_map:
			test_result += line.count('#')

		result = max(result, test_result)

		energize_map = []
		direction_map = []

		for line in maze:
			energize_map.append(['.' for x in line])
			direction_map.append(['.' for x in line])

		lightpath(maze, [i, len(maze[0])], [0, -1], energize_map, direction_map)

		test_result = 0
		for line in energize_map:
			test_result += line.count('#')

		result = max(result, test_result)

	for i in range(len(maze[0])):
		energize_map = []
		direction_map = []

		for line in maze:
			energize_map.append(['.' for x in line])
			direction_map.append(['.' for x in line])

		lightpath(maze, [-1, i], [1, 0], energize_map, direction_map)

		test_result = 0
		for line in energize_map:
			test_result += line.count('#')

		result = max(result, test_result)

		energize_map = []
		direction_map = []

		for line in maze:
			energize_map.append(['.' for x in line])
			direction_map.append(['.' for x in line])

		lightpath(maze, [len(maze), i], [-1, 0], energize_map, direction_map)

		test_result = 0
		for line in energize_map:
			test_result += line.count('#')

		result = max(result, test_result)

	return result