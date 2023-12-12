#!/usr/bin/python

import math

def get_next_direction(pipe, cdir, nbr_char):
	if pipe == '|' or pipe == '-':
		return cdir
	if cdir == nbr_char:
		if pipe == 'J':
			return -1
		else:
			return 1
	if cdir == nbr_char * -1:
		if pipe == '7':
			return -1
		else:
			return 1
	if cdir == 1:
		if pipe == '7':
			return nbr_char
		else:
			return nbr_char * -1
	if cdir == -1:
		if pipe == 'F':
			return nbr_char
		else:
			return nbr_char * -1

def display_maze(maze, nbr_char):
	for i in range(int(len(maze) / nbr_char)):
		print(''.join(maze[i * nbr_char:(i + 1) * nbr_char]))

def level1(input):
	# Test value
	# input = '7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ\n'
	lines = input.strip().split('\n')
	nbr_char = len(lines[0])
	maze = ''.join(lines)
	index = maze.index('S')
	direction = 0

	if (index % nbr_char != nbr_char - 1 and
		(maze[index + 1] == '-' or maze[index + 1] == 'J' or maze[index + 1] == '7')):
		direction = 1
	elif (index % nbr_char != 0 and
		(maze[index - 1] == '-' or maze[index - 1] == 'L' or maze[index + 1] == 'F')):
		direction = -1
	elif (index - nbr_char >= 0 and
		(maze[index - nbr_char] == '|' or maze[index - nbr_char] == '7' or maze[index - nbr_char] == 'F')):
		direction = nbr_char * -1
	elif (index + nbr_char < len(maze) and
		(maze[index + nbr_char] == '|' or maze[index + nbr_char] == 'J' or maze[index + nbr_char] == 'L')):
		direction = nbr_char

	nbr_pipe = 0
	next_pipe = ''

	while next_pipe != 'S':
		index += direction
		next_pipe = maze[index]
		direction = get_next_direction(next_pipe, direction, nbr_char)
		nbr_pipe += 1

	return math.floor(nbr_pipe / 2)

def level2(input):
	# Test value
	# input = 'FF7FSF7F7F7F7F7F---7\nL|LJ||||||||||||F--J\nFL-7LJLJ||||||LJL-77\nF--JF--7||LJLJ7F7FJ-\nL---JF-JLJ.||-FJLJJ7\n|F|F-JF---7F7-L7L|7|\n|FFJF7L7F-JF7|JL---7\n7-L-JL7||F7|L7F-7F7|\nL.L7LFJ|||||FJL7||LJ\nL7JLJL-JLJLJL--JLJ.L\n'
	lines = input.strip().split('\n')
	nbr_char = len(lines[0])
	maze = [x for x in ''.join(lines)]
	index = maze.index('S')
	start_index = index
	direction = 0

	# display_maze(maze, nbr_char)

	if (index % nbr_char != nbr_char - 1 and
		(maze[index + 1] == '-' or maze[index + 1] == 'J' or maze[index + 1] == '7')):
		direction = 1
	elif (index % nbr_char != 0 and
		(maze[index - 1] == '-' or maze[index - 1] == 'L' or maze[index + 1] == 'F')):
		direction = -1
	elif (index - nbr_char >= 0 and
		(maze[index - nbr_char] == '|' or maze[index - nbr_char] == '7' or maze[index - nbr_char] == 'F')):
		direction = nbr_char * -1
	elif (index + nbr_char < len(maze) and
		(maze[index + nbr_char] == '|' or maze[index + nbr_char] == 'J' or maze[index + nbr_char] == 'L')):
		direction = nbr_char

	start_direction = direction
	last_direction = direction
	next_pipe = ''

	while next_pipe != 'S':
		if maze[index] != '-' and maze[index] != 'S':
			if maze[index] == '7':
				maze[index] = 'D'
			elif maze[index] == 'L':
				maze[index] = 'U'
			elif maze[index] == 'F':
				maze[index] = 'D'
			elif maze[index] == 'J':
				maze[index] = 'U'
			else:
				maze[index] = '*'
		elif maze[index] != 'S':
			maze[index] = '~'
		last_direction = direction
		index += direction
		next_pipe = maze[index]
		direction = get_next_direction(next_pipe, direction, nbr_char)

	if start_direction == last_direction:
		if abs(start_direction) == nbr_char:
			maze[start_index] = '*'
		else:
			maze[start_index] = '~'
	elif start_direction == nbr_char or last_direction == -1 * nbr_char:
		maze[start_index] = 'D'
	elif start_direction == -1 * nbr_char or last_direction == nbr_char:
		maze[start_index] = 'U'

	# print('-------')
	# display_maze(maze, nbr_char)

	for i in range(int(len(maze) / nbr_char)):
		char = 'O'
		last_turn = ''
		for j in range(nbr_char):
			maze_char = maze[i * nbr_char + j]
			if maze_char == '*':
				if char == 'O':
					char = 'I'
				else:
					char = 'O'
			elif maze_char == 'U' or maze_char == 'D':
				if last_turn == '':
					last_turn = maze_char
				else:
					if last_turn != maze_char:
						if char == 'O':
							char = 'I'
						else:
							char = 'O'
					last_turn = ''
			elif maze[i * nbr_char + j] != '~':
				maze[i * nbr_char + j] = char

	# print('-------')
	# display_maze(maze, nbr_char)

	return maze.count('I')