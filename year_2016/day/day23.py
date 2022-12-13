#!/usr/bin/python

def compute_cmd(cmds, register, letter_reg):
	cursor = 0
	while cursor < len(cmds):
		splits = cmds[cursor].split(' ')
		if splits[0] == 'cpy':
			if not(splits[2] in letter_reg):
				# Invalid command
				cursor += 1
				continue
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])
			register[splits[2]] = value
		elif splits[0] == 'inc':
			if not(splits[1] in letter_reg):
				# Invalid command
				cursor += 1
				continue
			register[splits[1]] += 1
		elif splits[0] == 'dec':
			if not(splits[1] in letter_reg):
				# Invalid command
				cursor += 1
				continue
			register[splits[1]] -= 1
		elif splits[0] == 'jnz':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])

			value_jump = 0
			if splits[2] in letter_reg:
				value_jump = register[splits[2]]
			else:
				value_jump = int(splits[2])

			if value != 0:
				cursor += int(value_jump) - 1

		elif splits[0] == 'tgl':
			value = 0
			if splits[1] in letter_reg:
				value = register[splits[1]]
			else:
				value = int(splits[1])

			tmp_cursor = cursor + value
			if tmp_cursor >= len(cmds):
				# Invalid toggle
				cursor += 1
				continue

			to_change = cmds[tmp_cursor].split(' ')
			new_cmd = ''

			if len(to_change) == 2:
				if to_change[0] == 'inc':
					new_cmd = 'dec ' + to_change[1]
				else:
					new_cmd = 'inc ' + to_change[1]
			elif len(to_change) == 3:
				if to_change[0] == 'jnz':
					new_cmd = 'cpy ' + to_change[1] + ' ' + to_change[2]
				else:
					new_cmd = 'jnz ' + to_change[1] + ' ' + to_change[2]

			if new_cmd != '':
				cmds[tmp_cursor] = new_cmd

		elif splits[0] == 'muli':
			value = register[splits[2]] * register[splits[3]]
			register[splits[1]] += value
			register[splits[2]] = 0
			register[splits[3]] = 0
			cursor += int(splits[4]) - 1

		cursor += 1

def level1(input):
	#input = 'cpy 2 a\ntgl a\ntgl a\ntgl a\ncpy 1 a\ndec a\ndec a\n'
	input = 'cpy a b\ndec b\ncpy a d\ncpy 0 a\ncpy b c\nmuli a c d 5\ndec c\njnz c -2\ndec d\njnz d -5\ndec b\ncpy b c\ncpy c d\ndec d\ninc c\njnz d -2\ntgl c\ncpy -16 c\njnz 1 c\ncpy 96 c\njnz 95 d\ninc a\ninc d\njnz d -2\ninc c\njnz c -5\n'
	instructions = input.strip().split('\n')
	register = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
	letter_reg = ['a', 'b', 'c', 'd']
	compute_cmd(instructions, register, letter_reg)
	return register['a']

def level2(input):
	input = 'cpy a b\ndec b\ncpy a d\ncpy 0 a\ncpy b c\nmuli a c d 5\ndec c\njnz c -2\ndec d\njnz d -5\ndec b\ncpy b c\ncpy c d\ndec d\ninc c\njnz d -2\ntgl c\ncpy -16 c\njnz 1 c\ncpy 96 c\njnz 95 d\ninc a\ninc d\njnz d -2\ninc c\njnz c -5\n'
	instructions = input.strip().split('\n')
	register = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
	letter_reg = ['a', 'b', 'c', 'd']
	compute_cmd(instructions, register, letter_reg)
	return register['a']