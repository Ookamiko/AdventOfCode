#!/usr/bin/python

def asset(reg, a, b):

	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] = int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] = reg[b]

def add(reg, a, b):
	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] += int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] += reg[b]

def muli(reg, a, b):
	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] *= int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] *= reg[b]

def modulo(reg, a, b):
	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] = reg[a] % int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] = reg[a] % reg[b]

def level1(input):
	# Test value
	# input = 'set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2\n'
	cmds = input.strip().split('\n')
	index = 0
	reg = {}
	sound = 0

	while index >= 0 and index < len(cmds):
		cmd = cmds[index].split(' ')

		if len(cmd) == 2:
			if cmd[0] == 'snd':
				if cmd[1].isnumeric() or cmd[1][0] == '-':
					sound = int(cmd[1])
				else:
					if not(cmd[1] in reg.keys()):
						reg[cmd[1]] = 0

					sound = reg[cmd[1]]
			else:
				test = 0
				if cmd[1].isnumeric() or cmd[1][0] == '-':
					test = int(cmd[1])
				else:
					if not(cmd[1] in reg.keys()):
						reg[cmd[1]] = 0

					test = reg[cmd[1]]

				if test != 0:
					break

		else:
			if cmd[0] == 'set':
				asset(reg, cmd[1], cmd[2])
			elif cmd[0] == 'add':
				add(reg, cmd[1], cmd[2])
			elif cmd[0] == 'mul':
				muli(reg, cmd[1], cmd[2])
			elif cmd[0] == 'mod':
				modulo(reg, cmd[1], cmd[2])
			else:
				test = 0
				if cmd[1].isnumeric() or cmd[1][0] == '-':
					test = int(cmd[1])
				else:
					if not(cmd[1] in reg.keys()):
						reg[cmd[1]] = 0

					test = reg[cmd[1]]

				jump = 0
				if cmd[2].isnumeric() or cmd[2][0] == '-':
					jump = int(cmd[2])
				else:
					if not(cmd[2] in reg.keys()):
						reg[cmd[2]] = 0

					jump = reg[cmd[2]]

				if test > 0:
					index += jump - 1

		index += 1

	return sound

def level2(input):
	# Test value
	# input = 'set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2\n'
	cmds = input.strip().split('\n')
	tab_index = [0, 0]
	tab_reg = [{'p': 0}, {'p': 1}]
	value_send = [[], []]
	program = 1
	program_stop = -1
	result = 0

	while program_stop != 2:
		program_stop += 1
		program = (program + 1) % 2
		index = tab_index[program]
		reg = tab_reg[program]

		while index >= 0 and index < len(cmds):
			cmd = cmds[index].split(' ')

			if len(cmd) == 2:
				if cmd[0] == 'snd':
					program_stop = 0
					sound = 0
					if cmd[1].isnumeric() or cmd[1][0] == '-':
						sound = int(cmd[1])
					else:
						if not(cmd[1] in reg.keys()):
							reg[cmd[1]] = 0

						sound = reg[cmd[1]]

					value_send[(program + 1) % 2].append(sound)

					if program == 1:
						result += 1

				else:
					if len(value_send[program]) != 0:
						program_stop = 0
						if not(cmd[1] in reg.keys()):
							reg[cmd[1]] = 0

						reg[cmd[1]] = value_send[program].pop(0)
					else:
						break
			else:
				if cmd[0] == 'set':
					program_stop = 0
					asset(reg, cmd[1], cmd[2])
				elif cmd[0] == 'add':
					program_stop = 0
					add(reg, cmd[1], cmd[2])
				elif cmd[0] == 'mul':
					program_stop = 0
					muli(reg, cmd[1], cmd[2])
				elif cmd[0] == 'mod':
					program_stop = 0
					modulo(reg, cmd[1], cmd[2])
				else:
					program_stop = 0
					test = 0
					if cmd[1].isnumeric() or cmd[1][0] == '-':
						test = int(cmd[1])
					else:
						if not(cmd[1] in reg.keys()):
							reg[cmd[1]] = 0

						test = reg[cmd[1]]

					jump = 0
					if cmd[2].isnumeric() or cmd[2][0] == '-':
						jump = int(cmd[2])
					else:
						if not(cmd[2] in reg.keys()):
							reg[cmd[2]] = 0

						jump = reg[cmd[2]]

					if test > 0:
						index += jump - 1

			index += 1

		tab_index[program] = index

	return result