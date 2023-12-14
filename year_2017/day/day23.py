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

def sub(reg, a, b):
	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] -= int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] -= reg[b]

def muli(reg, a, b):
	if not(a in reg.keys()):
		reg[a] = 0

	if b.isnumeric() or b[0] == '-':
		reg[a] *= int(b)
	else:
		if not(b in reg.keys()):
			reg[b] = 0

		reg[a] *= reg[b]

def perform_command(cmd, reg):
	change_index = 0

	if cmd[0] == 'set':
		asset(reg, cmd[1], cmd[2])
	elif cmd[0] == 'sub':
		sub(reg, cmd[1], cmd[2])
	elif cmd[0] == 'mul':
		muli(reg, cmd[1], cmd[2])
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

		if test != 0:
			change_index = jump - 1

	return change_index

def level1(input):
	cmds = input.strip().split('\n')
	index = 0
	reg = {}
	result = 0

	while index >= 0 and index < len(cmds):
		cmd = cmds[index].split(' ')
		if cmd[0] == 'mul':
			result += 1

		index += perform_command(cmd, reg) + 1

	return result

def is_prime(nbr):
	result = True
	factor = 2
	while (nbr / factor) >= factor:
		if nbr % factor == 0:
			result = False
			break
		factor += 1

	return result

def level2(input):
	# By analyzing the assembler code, the program check for all non-prime
	# number between two value (reg-b and reg-c)
	# reg-h is increment by one for each value for reg-b that is not a prime
	result = 0

	b = 108400
	c = 125400

	while b <= c:
		if not(is_prime(b)):
			result += 1
		b += 17

	return result