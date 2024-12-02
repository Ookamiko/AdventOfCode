#!/usr/bin/python

import re as regex

def top_arrangement(stacks):
	result = ''

	for stack in stacks:
		result += stack.pop()

	return result

def init_stacks():
	return [
	['R','G','J','B','T','V','Z'],
	['J','R','V','L'],
	['S','Q','F'],
	['Z','H','N','L','F','V','Q','G'],
	['R','Q','T','J','C','S','M','W'],
	['S','W','T','C','H','F'],
	['D','Z','C','V','F','N','J'],
	['L','G','Z','D','W','R','F','Q'],
	['J','B','W','V','P']
	]

def level1(input):
	instructions = input.strip().split('\n')[10:]
	stacks = init_stacks()

	for current in instructions:
		numbers = [int(x) for x in regex.findall(r'\d+', current)]

		for i in range(numbers[0]):
			crate = stacks[numbers[1] - 1].pop()
			stacks[numbers[2] - 1].append(crate)

	return top_arrangement(stacks)

def level2(input):
	instructions = input.strip().split('\n')[10:]
	stacks = init_stacks()

	for current in instructions:
		numbers = [int(x) for x in regex.findall(r'\d+', current)]

		nb_to_keep = len(stacks[numbers[1] - 1]) - numbers[0]
		crates = stacks[numbers[1] - 1][nb_to_keep:]
		stacks[numbers[2] - 1] += crates
		stacks[numbers[1] - 1] = stacks[numbers[1] - 1][:nb_to_keep]

	return top_arrangement(stacks)