#!/usr/bin/python

import math

def display_board(board):
	min_y = 0
	max_y = 0
	min_x = 0
	max_x = 0

	for key in board.keys():
		tmp = [int(x) for x in key.split(',')]
		min_y = min(tmp[0], min_y)
		max_y = max(tmp[0], max_y)
		min_x = min(tmp[1], min_x)
		max_x = max(tmp[1], max_x)

	for i in range(min_y, max_y + 1):
		line = ''
		for j in range(min_x, max_x + 1):
			key = str(i) + ',' + str(j)
			if key in board.keys():
				line += board[key]
			else:
				line += '.'
			line += ' '
		print(line)

def turn_left(direction):
	if direction[0] == 0:
		if direction[1] == 1:
			return [-1, 0]
		else:
			return [1, 0]
	else:
		if direction[0] == 1:
			return [0, 1]
		else:
			return [0, -1]

def turn_right(direction):
	if direction[0] == 0:
		if direction[1] == 1:
			return [1, 0]
		else:
			return [-1, 0]
	else:
		if direction[0] == 1:
			return [0, -1]
		else:
			return [0, 1]

def flip(direction):
	if direction[0] == 0:
		return [0, direction[1] * -1]
	else:
		return [direction[0] * -1, 0]

def level1(input):
	# Test value
	# input = '..#\n#..\n...\n'
	lines = input.strip().split('\n')
	board = {}
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			board[str(i) + ',' + str(j)] = lines[i][j]

	pos = [math.floor(len(lines) / 2), math.floor(len(lines[0]) / 2)]
	direction = [-1, 0]

	result = 0

	for i in range(10000):
		key = str(pos[0]) + ',' + str(pos[1])
		if not(key in board.keys()):
			board[key] = '.'

		if board[key] == '.':
			direction = turn_left(direction)
			board[key] = '#'
			result += 1
		else:
			direction = turn_right(direction)
			board[key] = '.'

		pos[0] += direction[0]
		pos[1] += direction[1]

	return result

def level2(input):
	# Test value
	# input = '..#\n#..\n...\n'
	lines = input.strip().split('\n')
	board = {}
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			board[str(i) + ',' + str(j)] = lines[i][j]

	pos = [math.floor(len(lines) / 2), math.floor(len(lines[0]) / 2)]
	direction = [-1, 0]

	result = 0

	for i in range(10000000):
		key = str(pos[0]) + ',' + str(pos[1])
		if not(key in board.keys()):
			board[key] = '.'

		if board[key] == '.':
			direction = turn_left(direction)
			board[key] = 'W'
		elif board[key] == 'W':
			board[key] = '#'
			result += 1
		elif board[key] == '#':
			direction = turn_right(direction)
			board[key] = 'F'
		else:
			direction = flip(direction)
			board[key] = '.'

		pos[0] += direction[0]
		pos[1] += direction[1]

	return result