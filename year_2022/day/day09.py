#!/usr/bin/python

def correct_tail(head, tail):

	# Up/Down
	if abs(head[0] - tail[0]) > 1 and head[1] == tail[1]:
		if head[0] > tail[0]:
			tail = [tail[0] + 1, tail[1]]
		else:
			tail = [tail[0] - 1, tail[1]]

	# Left/Right
	elif abs(head[1] - tail[1]) > 1 and head[0] == tail[0]:
		if head[1] > tail[1]:
			tail = [tail[0], tail[1] + 1]
		else:
			tail = [tail[0], tail[1] - 1]

	# Diag
	elif abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
		if head[0] > tail[0]:
			if head[1] > tail[1]:
				tail = [tail[0] + 1, tail[1] + 1]
			else:
				tail = [tail[0] + 1, tail[1] - 1]
		else:
			if head[1] > tail[1]:
				tail = [tail[0] - 1, tail[1] + 1]
			else:
				tail = [tail[0] - 1, tail[1] - 1]

	return tail


def display_state(rope, size):
	for x in range(size):
		line = ''
		for y in range(size):
			found = False
			for z in range(len(rope)):
				if rope[z][0] == x and rope[z][1] == y:
					line += str(z)
					found = True
					break

			if not(found):
				line += '.'

		print(line)

def level1(input):
	#input = 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n'
	rope = [[0,0], [0,0]]
	positions = ['0,0']

	for line in input.strip().split('\n'):
		cmd = line.split(' ')
		for i in range(int(cmd[1])):

			if cmd[0] == 'U':
				rope[0][0] += 1
			elif cmd[0] == 'D':
				rope[0][0] -= 1
			elif cmd[0] == 'L':
				rope[0][1] -= 1
			else:
				rope[0][1] += 1

			rope[1] = correct_tail(rope[0], rope[1])
			str_tail = str(rope[1][0]) + ',' + str(rope[1][1])

			if not(str_tail in positions):
				positions.append(str_tail)

	return len(positions)

def level2(input):
	#input = 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20\n'
	rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
	positions = ['0,0']

	for line in input.strip().split('\n'):
		cmd = line.split(' ')
		for i in range(int(cmd[1])):

			if cmd[0] == 'U':
				rope[0][0] += 1
			elif cmd[0] == 'D':
				rope[0][0] -= 1
			elif cmd[0] == 'L':
				rope[0][1] -= 1
			else:
				rope[0][1] += 1

			for j in range(len(rope) - 1):
				rope[j + 1] = correct_tail(rope[j], rope[j + 1])

			str_tail = str(rope[-1][0]) + ',' + str(rope[-1][1])

			if not(str_tail in positions):
				positions.append(str_tail)

	return len(positions)