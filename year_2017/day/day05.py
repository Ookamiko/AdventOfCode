#!/usr/bin/python

def level1(input):
	jumps = [int(x) for x in input.strip().split('\n')]
	cursor = 0
	step = 0

	while cursor >= 0 and cursor < len(jumps):
		step += 1
		new_cursor = cursor + jumps[cursor]
		jumps[cursor] += 1
		cursor = new_cursor

	return step

def level2(input):
	jumps = [int(x) for x in input.strip().split('\n')]
	cursor = 0
	step = 0

	while cursor >= 0 and cursor < len(jumps):
		step += 1
		new_cursor = cursor + jumps[cursor]
		if jumps[cursor] >= 3:
			jumps[cursor] -= 1
		else:
			jumps[cursor] += 1
		cursor = new_cursor

	return step