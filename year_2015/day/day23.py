#!/usr/bin/python

import re as regex

def ExecuteProgram(instructions, register):
	i = 0
	reg = r'([a-z]{3}) ((\+?(-?\d+))|(a|b))(, \+?(-?\d+))?'
	while i >= 0 and i < len(instructions):
		print(instructions[i])
		matches = regex.match(reg, instructions[i])
		if matches:
			groups = matches.groups()
			command = groups[0]

			if command == 'hlf':
				reg_name = groups[1]
				register[reg_name] = int(register[reg_name] / 2)

			elif command == 'tpl':
				reg_name = groups[1]
				register[reg_name] *= 3

			elif command == 'inc':
				reg_name = groups[1]
				register[reg_name] += 1

			elif command == 'jmp':
				offset = int(groups[3])
				i += offset - 1

			elif command == 'jie':
				reg_name = groups[1]
				offset = int(groups[6])
				if register[reg_name] % 2 == 0:
					i += offset - 1

			elif command == 'jio':
				reg_name = groups[1]
				offset = int(groups[6])
				if register[reg_name] == 1:
					i += offset - 1

		i += 1



def level1(input):
	instructions = input.strip().split('\n')
	register = {'a': 0, 'b': 0}
	ExecuteProgram(instructions, register)
	print(register)
	return register['b']

def level2(input):
	instructions = input.strip().split('\n')
	register = {'a': 1, 'b': 0}
	ExecuteProgram(instructions, register)
	print(register)
	return register['b']