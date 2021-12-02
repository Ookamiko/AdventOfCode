#!/usr/bin/python

def level1(input):
	instructions = input.strip().split('\n')
	position = 0
	depth = 0
	for current in instructions:
		command = current.split(' ')[0]
		unit = int(current.split(' ')[1])
		if command == 'forward':
			position += unit
		elif command == 'down':
			depth += unit
		elif command == 'up':
			depth -= unit

	return position * depth

def level2(input):
	instructions = input.strip().split('\n')
	position = 0
	depth = 0
	aim = 0
	for current in instructions:
		command = current.split(' ')[0]
		unit = int(current.split(' ')[1])
		if command == 'forward':
			position += unit
			depth += aim * unit
		elif command == 'down':
			aim += unit
		elif command == 'up':
			aim -= unit

	return position * depth