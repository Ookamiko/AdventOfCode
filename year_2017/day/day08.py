#!/usr/bin/python

import re as regex

def perform_program(cmds, mem):
	max_found = 0
	cmd_reg = r'^([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)$'
	for cmd in cmds:
		matches = regex.match(cmd_reg, cmd)

		if matches:
			groups = matches.groups()
			registre_modif = groups[0]
			modificator = groups[1]
			value_modif = int(groups[2])
			registre_test = groups[3]
			operand = groups[4]
			value_test = int(groups[5])

			if not(registre_modif in mem.keys()):
				mem[registre_modif] = 0

			if not(registre_test in mem.keys()):
				mem[registre_test] = 0

			perform_modif = False

			perform_modif = (
				(operand == '==' and mem[registre_test] == value_test) or
				(operand == '!=' and mem[registre_test] != value_test) or
				(operand == '<' and mem[registre_test] < value_test) or
				(operand == '<=' and mem[registre_test] <= value_test) or
				(operand == '>' and mem[registre_test] > value_test) or
				(operand == '>=' and mem[registre_test] >= value_test)
			)

			if perform_modif:
				if modificator == 'inc':
					mem[registre_modif] = mem[registre_modif] + value_modif
				else:
					mem[registre_modif] = mem[registre_modif] - value_modif

				max_found = max(max_found, mem[registre_modif])

	return max_found

def get_max_mem(mem):
	to_return = 0
	for reg in mem.keys():
		to_return = max(to_return, mem[reg])

	return to_return

def level1(input):
	# Test value
	# input = 'b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10\n'
	mem = {}
	perform_program(input.strip().split('\n'), mem)
	return get_max_mem(mem)

def level2(input):
	# Test value
	# input = 'b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10\n'
	mem = {}
	return perform_program(input.strip().split('\n'), mem)