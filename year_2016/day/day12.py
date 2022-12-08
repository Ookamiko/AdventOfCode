#!/usr/bin/python

def level1(input):
	instructions = input.strip().split('\n')
	cursor = 0
	register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
	letter_reg = ['a', 'b', 'c', 'd']
	while cursor < len(instructions):
		splits = instructions[cursor].split(' ')
		if splits[0] == 'cpy':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])
			register[splits[2]] = value
		elif splits[0] == 'inc':
			register[splits[1]] += 1
		elif splits[0] == 'dec':
			register[splits[1]] -= 1
		elif splits[0] == 'jnz':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])

			if value != 0:
				cursor += int(splits[2]) - 1

		cursor += 1

	return register['a']

def level2(input):
	instructions = input.strip().split('\n')
	cursor = 0
	register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
	letter_reg = ['a', 'b', 'c', 'd']
	while cursor < len(instructions):
		splits = instructions[cursor].split(' ')
		if splits[0] == 'cpy':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])
			register[splits[2]] = value
		elif splits[0] == 'inc':
			register[splits[1]] += 1
		elif splits[0] == 'dec':
			register[splits[1]] -= 1
		elif splits[0] == 'jnz':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])

			if value != 0:
				cursor += int(splits[2]) - 1

		cursor += 1

	return register['a']