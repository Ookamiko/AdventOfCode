#!/usr/bin/python

def stringify_reg(register, letter_reg, clock):
	result = str(clock) + '|'
	for letter in letter_reg:
		result += letter + ':' + str(register[letter]) + ','

	result.strip(',')
	return result

def compute_cmd(cmds, register, letter_reg):
	clock = 1
	save_reg = []
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

		elif splits[0] == 'mul':
			value = register[splits[2]] * register[splits[3]]
			register[splits[1]] += value
			register[splits[2]] = 0
			register[splits[3]] = 0
			cursor += int(splits[4]) - 1

		elif splits[0] == 'out':
			value = register[splits[1]]
			if (value == 0 and clock == 1) or (value == 1 and clock == 0):
				clock = value
				tmp_string = stringify_reg(register, letter_reg, clock)
				if tmp_string in save_reg:
					return True
				else:
					save_reg.append(tmp_string)
			else:
				return False

		cursor += 1

def level1(input):
	input = 'cpy a d\ncpy 4 c\ncpy 643 b\nmul d c b 5\ndec b\njnz b -2\ndec c\njnz c -5\ncpy d a\njnz 0 0\ncpy a b\ncpy 0 a\ncpy 2 c\njnz b 2\njnz 1 6\ndec b\ndec c\njnz c -4\ninc a\njnz 1 -7\ncpy 2 b\njnz c 2\njnz 1 4\ndec b\ndec c\njnz 1 -4\njnz 0 0\nout b\njnz a -19\njnz 1 -21\n'
	instructions = input.strip().split('\n')
	test = 0
	register = {'a': test, 'b': 0, 'c': 0, 'd': 0}
	letter_reg = ['a', 'b', 'c', 'd']
	while not(compute_cmd(instructions, register, letter_reg)):
		test += 1
		register = {'a': test, 'b': 0, 'c': 0, 'd': 0}

	return test

def level2(input):
	return "Done"