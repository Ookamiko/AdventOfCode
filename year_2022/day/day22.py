#!/usr/bin/python

import re as regex

def init_map(instructions):
	path = instructions.pop()
	instructions.pop()

	cmd_path = []
	for cmd in regex.findall(r'\d+[RL]?', path):
		num = regex.findall(r'\d+', cmd)
		cmd_path.append(int(num[0]))
		cmd_path.append(cmd.replace(num[0], ''))

	mapp = []
	start = [0, -1]
	max_row = 0
	for line in instructions:
		row = []
		for i in range(len(line)):
			char = line[i]
			row.append(char)
			if char == '.' and start[1] == -1:
				start[1] = i
		max_row = max(max_row, len(row))
		mapp.append(row)

	for i in range(len(mapp)):
		mapp[i] += ['@'] * (max_row - len(mapp[i]))

	return mapp, start, cmd_path

def get_new_pos(mapp, pos, rotation):
	new_pos = []
	if rotation == 0:
		new_pos = [pos[0], pos[1] + 1]
		if new_pos[1] >= len(mapp[0]) or mapp[new_pos[0]][new_pos[1]] == '@':
			new_pos[1] = 0
			while mapp[new_pos[0]][new_pos[1]] == '@':
				new_pos[1] += 1
	elif rotation == 1:
		new_pos = [pos[0] + 1, pos[1]]
		if new_pos[0] >= len(mapp) or mapp[new_pos[0]][new_pos[1]] == '@':
			new_pos[0] = 0
			while mapp[new_pos[0]][new_pos[1]] == '@':
				new_pos[0] += 1
	elif rotation == 2:
		new_pos = [pos[0], pos[1] - 1]
		if new_pos[1] < 0 or mapp[new_pos[0]][new_pos[1]] == '@':
			new_pos[1] = len(mapp[0]) - 1
			while mapp[new_pos[0]][new_pos[1]] == '@':
				new_pos[1] -= 1
	elif rotation == 3:
		new_pos = [pos[0] - 1, pos[1]]
		if new_pos[0] < 0 or mapp[new_pos[0]][new_pos[1]] == '@':
			new_pos[0] = len(mapp) - 1
			while mapp[new_pos[0]][new_pos[1]] == '@':
				new_pos[0] -= 1

	return new_pos

def correct_pos_cube(pos, rotation, def_cube, size_cube):
	start_face = 0
	for i in range(len(def_cube)):
		origin_face = def_cube[i]['origin']
		if pos[0] >= origin_face[0] and pos[0] < origin_face[0] + size_cube and pos[1] >= origin_face[1] and pos[1] < origin_face[1] + size_cube:
			start_face = i
			break

	destination = def_cube[start_face]['dest'][rotation]

	start_relative_pos = [pos[0] - def_cube[start_face]['origin'][0], pos[1] - def_cube[start_face]['origin'][1]]
	end_relative_pos = [0, 0]

	if destination['new_x'] == 'max':
		end_relative_pos[0] = size_cube - 1
	elif destination['new_x'] == 'x':
		end_relative_pos[0] = start_relative_pos[0]
	elif destination['new_x'] == '-x':
		end_relative_pos[0] = (size_cube - 1) - start_relative_pos[0]
	elif destination['new_x'] == 'y':
		end_relative_pos[0] = start_relative_pos[1]
	elif destination['new_x'] == '-y':
		end_relative_pos[0] = (size_cube - 1) - start_relative_pos[1]

	if destination['new_y'] == 'max':
		end_relative_pos[1] = size_cube - 1
	elif destination['new_y'] == 'x':
		end_relative_pos[1] = start_relative_pos[0]
	elif destination['new_y'] == '-x':
		end_relative_pos[1] = (size_cube - 1) - start_relative_pos[0]
	elif destination['new_y'] == 'y':
		end_relative_pos[1] = start_relative_pos[1]
	elif destination['new_y'] == '-y':
		end_relative_pos[1] = (size_cube - 1) - start_relative_pos[1]

	end_face = destination['face']
	new_pos = [def_cube[end_face]['origin'][0] + end_relative_pos[0], def_cube[end_face]['origin'][1] + end_relative_pos[1]]
	new_rotation = destination['new_rot']

	return new_pos, new_rotation


def get_new_pos_cube(mapp, pos, rotation, def_cube, size_cube):
	new_pos = []
	new_rotation = rotation
	if rotation == 0:
		new_pos = [pos[0], pos[1] + 1]
	elif rotation == 1:
		new_pos = [pos[0] + 1, pos[1]]
	elif rotation == 2:
		new_pos = [pos[0], pos[1] - 1]
	elif rotation == 3:
		new_pos = [pos[0] - 1, pos[1]]

	if new_pos[0] < 0 or new_pos[0] >= len(mapp) or new_pos[1] < 0 or new_pos[1] >= len(mapp[0]) or mapp[new_pos[0]][new_pos[1]] == '@':
		new_pos, new_rotation = correct_pos_cube(pos, rotation, def_cube, size_cube)

	return new_pos, new_rotation

def execute_path(mapp, start, path):
	rotation = 0
	pos = start
	for i in range(0, len(path), 2):
		move = path[i]
		for j in range(move):
			if rotation == 0:
				mapp[pos[0]][pos[1]] = '>'
			elif rotation == 1:
				mapp[pos[0]][pos[1]] = 'v'
			elif rotation == 2:
				mapp[pos[0]][pos[1]] = '<'
			elif rotation == 3:
				mapp[pos[0]][pos[1]] = '^'

			new_pos = get_new_pos(mapp, pos, rotation)
			if mapp[new_pos[0]][new_pos[1]] == '#':
				break;
			pos = new_pos

		if path[i + 1] == 'R':
			rotation = (rotation + 1) % 4
		elif path[i + 1] == 'L':
			rotation = (rotation + 3) % 4
		else:
			print(path[i], path[i + 1])


	return pos, rotation

def execute_path_cube(mapp, start, path, def_cube, size_cube):
	rotation = 0
	pos = start
	for i in range(0, len(path), 2):
		move = path[i]
		for j in range(move):
			if rotation == 0:
				mapp[pos[0]][pos[1]] = '>'
			elif rotation == 1:
				mapp[pos[0]][pos[1]] = 'v'
			elif rotation == 2:
				mapp[pos[0]][pos[1]] = '<'
			elif rotation == 3:
				mapp[pos[0]][pos[1]] = '^'

			new_pos, new_rotation = get_new_pos_cube(mapp, pos, rotation, def_cube, size_cube)
			if mapp[new_pos[0]][new_pos[1]] == '#':
				break;
			pos = new_pos
			rotation = new_rotation

		if path[i + 1] == 'R':
			rotation = (rotation + 1) % 4
		elif path[i + 1] == 'L':
			rotation = (rotation + 3) % 4


	return pos, rotation

def display_map(mapp):
	for line in mapp:
		print(''.join(line))

def level1(input):
	#input = '        ...#\n        .#..\n        #...\n        ....\n...#.......#\n........#...\n..#....#....\n..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.\n\n10R5L5R10L4R5L5\n'
	mapp, start, cmd_path = init_map(input.replace(' ', '@').strip().split('\n'))
	final_pos, rotation = execute_path(mapp, start, cmd_path)
	return 1000 * (final_pos[0] + 1) + 4 * (final_pos[1] + 1) + rotation

def level2(input):
#	input = '        ...#\n        .#..\n        #...\n        ....\n...#.......#\n........#...\n..#....#....\n..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.\n\n10R5L5R10L4R5L5\n'
#	def_cube = [{'origin': [4, 8],'dest': [{'face': 3,'new_rot': 1,'new_x': '0','new_y': '-x'},{'face': 4,'new_rot': 1,'new_x': '0','new_y': 'y'},{'face': 2,'new_rot': 2,'new_x': 'x','new_y': 'max'},{'face': 1,'new_rot': 3,'new_x': 'max','new_y': 'y'},]},{'origin': [0, 8],'dest': [{'face': 3,'new_rot': 2,'new_x': '-x','new_y': 'max'},{'face': 0,'new_rot': 1,'new_x': '0','new_y': 'y'},{'face': 2,'new_rot': 1,'new_x': '0','new_y': 'x'},{'face': 5,'new_rot': 1,'new_x': '0','new_y': '-y'},]},{'origin': [4, 4],'dest': [{'face': 0,'new_rot': 0,'new_x': 'x','new_y': '0'},{'face': 4,'new_rot': 0,'new_x': '-y','new_y': '0'},{'face': 5,'new_rot': 2,'new_x': 'x','new_y': 'max'},{'face': 1,'new_rot': 0,'new_x': 'y','new_y': '0'},]},{'origin': [8, 12],'dest': [{'face': 1,'new_rot': 2,'new_x': '-x','new_y': 'max'},{'face': 5,'new_rot': 0,'new_x': 'y','new_y': '0'},{'face': 4,'new_rot': 2,'new_x': 'x','new_y': 'max'},{'face': 0,'new_rot': 2,'new_x': '-y','new_y': 'max'},]},{'origin': [8, 8],'dest': [{'face': 3,'new_rot': 0,'new_x': 'x','new_y': '0'},{'face': 5,'new_rot': 3,'new_x': 'max','new_y': '-y'},{'face': 2,'new_rot': 3,'new_x': 'max','new_y': '-x'},{'face': 0,'new_rot': 3,'new_x': 'max','new_y': 'y'},]},{'origin': [4, 0],'dest': [{'face': 2,'new_rot': 0,'new_x': 'x','new_y': '0'},{'face': 4,'new_rot': 3,'new_x': 'max','new_y': '-y'},{'face': 3,'new_rot': 3,'new_x': 'max','new_y': '-x'},{'face': 1,'new_rot': 1,'new_x': '0','new_y': '-y'},]}]
#	size_cube = 4
	def_cube = [{'origin': [0, 50],'dest': [{'face': 2},{'face': 1},{'face': 3,'new_rot': 0,'new_x': '-x','new_y': '0'},{'face': 4,'new_rot': 0,'new_x': 'y','new_y': '0'},]},{'origin': [50, 50],'dest': [{'face': 2,'new_rot': 3,'new_x': 'max','new_y': 'x'},{'face': 5,},{'face': 3,'new_rot': 1,'new_x': '0','new_y': 'x'},{'face': 0},]},{'origin': [0, 100],'dest': [{'face': 5,'new_rot': 2,'new_x': '-x','new_y': 'max'},{'face': 1,'new_rot': 2,'new_x': 'y','new_y': 'max'},{'face': 0,},{'face': 4,'new_rot': 3,'new_x': 'max','new_y': 'y'},]},{'origin': [100, 0],'dest': [{'face': 5},{'face': 4},{'face': 0,'new_rot': 0,'new_x': '-x','new_y': '0'},{'face': 1,'new_rot': 0,'new_x': 'y','new_y': '0'},]},{'origin': [150, 0],'dest': [{'face': 5,'new_rot': 3,'new_x': 'max','new_y': 'x'},{'face': 2,'new_rot': 1,'new_x': '0','new_y': 'y'},{'face': 0,'new_rot': 1,'new_x': '0','new_y': 'x'},{'face': 3},]},{'origin': [100, 50],'dest': [{'face': 2,'new_rot': 2,'new_x': '-x','new_y': 'max'},{'face': 4,'new_rot': 2,'new_x': 'y','new_y': 'max'},{'face': 3},{'face': 1},]}]
	size_cube = 50

	mapp, start, cmd_path = init_map(input.replace(' ', '@').strip().split('\n'))
	final_pos, rotation = execute_path_cube(mapp, start, cmd_path, def_cube, size_cube)
	return 1000 * (final_pos[0] + 1) + 4 * (final_pos[1] + 1) + rotation