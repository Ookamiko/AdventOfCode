#!/usr/bin/python

def level1(input):
	keypad = ['1','2','3','4','5','6','7','8','9']
	position = 4
	code = ''
	for line in input.strip().split('\n'):
		for command in line:
			if command == 'U':
				if position > 2:
					position -= 3
			elif command == 'D':
				if position < 6:
					position += 3
			elif command == 'L':
				if position % 3 > 0:
					position -= 1
			elif command == 'R':
				if position % 3 < 2:
					position += 1
		code += keypad[position]
	return code

def level2(input):
	keypad = ['.', '.', '1', '.', '.', '.', '2','3','4','.', '5','6','7','8','9', '.', 'A', 'B', 'C', '.', '.', '.', 'D', '.', '.']
	position = 10
	code = ''
	for line in input.strip().split('\n'):
		for command in line:
			if command == 'U':
				if position > 4 and keypad[position - 5] != '.':
					position -= 5
			elif command == 'D':
				if position < 20 and keypad[position + 5] != '.':
					position += 5
			elif command == 'L':
				if position % 5 > 0 and keypad[position - 1] != '.':
					position -= 1
			elif command == 'R':
				if position % 5 < 4 and keypad[position + 1] != '.':
					position += 1
		code += keypad[position]
	return code
	return "Not implemented"