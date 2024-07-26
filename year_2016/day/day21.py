#!/usr/bin/python

def swap(password, a, b):
	return password.replace(a, '0').replace(b, a).replace('0', b)

def reverse(password, start, end):
	return password[0:start] + password[start:end+1][::-1] + password[end+1:]

def move(password, start, end):
	array_pass = [x for x in password]
	letter = array_pass.pop(start)
	array_pass = array_pass[0:end] + [letter] + array_pass[end:]
	return ''.join(array_pass)

def rotate(password, step, left_rotation=True):
	step = step % len(password)
	if not(left_rotation):
		step = len(password) - step
	return password[step:] + password[:step]

def found_reverse_rotation(password, letter):
	tmp_password = password
	for i in range(len(password)):
		tmp_password = rotate(password, i + 1)
		index = tmp_password.index(letter)
		if rotate(tmp_password, index + 1 if index < 4 else index + 2, False) == password:
			break

	return tmp_password

def level1(input):
	#password = 'abcde'
	#input = 'swap position 4 with position 0\nswap letter d with letter b\nreverse positions 0 through 4\nrotate left 1 step\nmove position 1 to position 4\nmove position 3 to position 0\nrotate based on position of letter b\nrotate based on position of letter d\n'
	password = 'abcdefgh'

	for current in input.strip().split('\n'):
		cmd = current.split(' ')

		if cmd[0] == 'reverse':
			password = reverse(password, int(cmd[2]), int(cmd[4]))
		elif cmd[0] == 'move':
			password = move(password, int(cmd[2]), int(cmd[5]))
		elif cmd[0] == 'swap':
			if cmd[1] == 'position':
				password = swap(password, password[int(cmd[2])], password[int(cmd[5])])
			else:
				password = swap(password, cmd[2], cmd[5])
		elif cmd[0] == 'rotate':
			step = 0
			is_left = True
			if cmd[1] == 'based':
				tmp = [x for x in password].index(cmd[6])
				step = 1 + tmp + (1 if tmp >= 4 else 0)
				is_left = False
			elif cmd[1] == 'right':
				is_left = False
				step = int(cmd[2])
			else:
				step = int(cmd[2])
			password = rotate(password, step, is_left)

	return password

def level2(input):
	#password = 'decab'
	#input = 'swap position 4 with position 0\nswap letter d with letter b\nreverse positions 0 through 4\nrotate left 1 step\nmove position 1 to position 4\nmove position 3 to position 0\nrotate based on position of letter b\nrotate based on position of letter d\n'
	password = 'fbgdceah'

	for current in input.strip().split('\n')[::-1]:
		cmd = current.split(' ')

		if cmd[0] == 'reverse':
			password = reverse(password, int(cmd[2]), int(cmd[4]))
		elif cmd[0] == 'move':
			password = move(password, int(cmd[5]), int(cmd[2]))
		elif cmd[0] == 'swap':
			if cmd[1] == 'position':
				password = swap(password, password[int(cmd[2])], password[int(cmd[5])])
			else:
				password = swap(password, cmd[2], cmd[5])
		elif cmd[0] == 'rotate':
			step = 0
			is_left = True
			if cmd[1] == 'based':
				password = found_reverse_rotation(password, cmd[6])
			elif cmd[1] == 'right':
				step = int(cmd[2])
			else:
				is_left = False
				step = int(cmd[2])
			password = rotate(password, step, is_left)

	return password