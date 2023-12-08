#!/usr/bin/python

def level1(input):
	# Test value
	# input = '     |          \n     |  +--+    \n     A  |  C    \n F---|--|-E---+ \n     |  |  |  D \n     +B-+  +--+ \n'
	lines = input.split('\n')
	nbr_char = len(lines[0])
	index = lines[0].index('|')
	direction = nbr_char
	maze = ''.join(lines[:len(lines) - 1])
	path = []

	result = ''

	while maze[index] != ' ':
		char = maze[index]
		path.append(char)

		if char == '+':
			if direction == 1 or direction == -1:
				if index - nbr_char > 0 and maze[index - nbr_char] != ' ':
					direction = nbr_char * -1
				else:
					direction = nbr_char
			else:
				if index % nbr_char != 0 and maze[index - 1] != ' ':
					direction = -1
				else:
					direction = 1

		elif char != '|' and char != '-':
			result += char

		index += direction

	return result

def level2(input):
	# Test value
	# input = '     |          \n     |  +--+    \n     A  |  C    \n F---|--|-E---+ \n     |  |  |  D \n     +B-+  +--+ \n'
	lines = input.split('\n')
	nbr_char = len(lines[0])
	index = lines[0].index('|')
	direction = nbr_char
	maze = ''.join(lines[:len(lines) - 1])
	path = []

	while maze[index] != ' ':
		char = maze[index]
		path.append(char)

		if char == '+':
			if direction == 1 or direction == -1:
				if index - nbr_char > 0 and maze[index - nbr_char] != ' ':
					direction = nbr_char * -1
				else:
					direction = nbr_char
			else:
				if index % nbr_char != 0 and maze[index - 1] != ' ':
					direction = -1
				else:
					direction = 1

		index += direction

	return len(path)