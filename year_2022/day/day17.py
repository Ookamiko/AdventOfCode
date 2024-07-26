#!/usr/bin/python

def init_cave(height_cave):
	cave = []
	for i in range(height_cave):
		cave.append(['.'] * 7)

	return cave

def display_cave(cave):
	for row in cave[::-1]:
		if '#' in row:
			print(''.join(row))

def display_solid_floor(cave):
	for i in range(len(cave)):
		if not('.' in cave[i]):
			print(i)

def place_rock(cave, rock, pos):
	for offset in rock:
		cave[pos[1] + offset[1]][pos[0] + offset[0]] = '#'

def get_max_height(pos, rock):
	max_height = 0
	for offset in rock:
		max_height = max(max_height, pos[1] + offset[1])

	return max_height

def move_gaz(cave, pos, rock, go_left):
	new_pos = [(pos[0] - 1) if go_left else (pos[0] + 1), pos[1]]
	valid = True
	for offset in rock:
		if new_pos[0] < 0 or new_pos[0] + offset[0] >= len(cave[0]) or cave[new_pos[1] + offset[1]][new_pos[0] + offset[0]] == '#':
			valid = False
			break

	return new_pos if valid else pos

def can_go_down(cave, pos, rock):
	new_pos = [pos[0], pos[1] - 1]
	valid = True

	for offset in rock:
		if new_pos[1] < 0 or cave[new_pos[1] + offset[1]][new_pos[0] + offset[0]] == '#':
			valid = False
			break

	return valid

def find_solid_floor(cave):
	cursor = 0
	for i in range(len(cave) - 1, 0, -1):
		if not('.' in cave[i]):
			cursor = i
			break

	return cursor

def level1(input):
	#input = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
	height_cave = 750
	nbr_rock = 2022
	falling_rock = [[[0,0],[1,0],[2,0],[3,0]],[[0,1],[1,0],[1,1],[1,2],[2,1]],[[0,0],[1,0],[2,0],[2,1],[2,2]],[[0,0],[0,1],[0,2],[0,3]],[[0,0],[0,1],[1,0],[1,1]]]
	cmd_gaz = input.strip()
	cursor_gaz = 0
	max_height = 0
	offset_height = 0
	cave = init_cave(height_cave)
	saved_cfg = ['0|0|']
	saved_floor_cfg = [0]
	saved_id_rock_cfg = [0]
	found_config = False
	o = 0

	while o < nbr_rock:
		pos = [2, max_height + 3 - offset_height]
		rock = falling_rock[o % 5]
		finish = False

		while not(finish):
			pos = move_gaz(cave, pos, rock, cmd_gaz[cursor_gaz] == '<')
			cursor_gaz += 1
			if cursor_gaz >= len(cmd_gaz):
				cursor_gaz = 0

			if can_go_down(cave, pos, rock):
				pos[1] -= 1
			else:
				place_rock(cave, rock, pos)
				finish = True
				max_height = max(max_height, get_max_height(pos, rock) + 1 + offset_height)

		solid_floor = find_solid_floor(cave)
		if solid_floor != 0:
			offset_height += solid_floor + 1
			new_cave = init_cave(height_cave)
			state_cave = ''
			for i in range(solid_floor + 1, len(cave)):
				if not('#' in cave[i]):
					break
				new_cave[i - (solid_floor + 1)] = cave[i]
				state_cave += ''.join(cave[i])

			cave = new_cave
			config = str(o % 5) + '|' + str(cursor_gaz) + '|' + state_cave
			if config in saved_cfg and not(found_config):
				found_config = True
				ind = saved_cfg.index(config)
				past_rock = saved_id_rock_cfg[ind]
				past_floor = saved_floor_cfg[ind]
				current_rock = o
				current_floor = offset_height
				diff_rock = current_rock - past_rock
				diff_floor = current_floor - past_floor

				rest_rock = nbr_rock - past_rock
				occurence = rest_rock // diff_rock
				max_height += diff_floor * (occurence - 1)
				offset_height += diff_floor * (occurence - 1)
				o += diff_rock * (occurence - 1)
			else:
				saved_cfg.append(config)
				saved_floor_cfg.append(offset_height)
				saved_id_rock_cfg.append(o)

		o += 1

	return max_height

def level2(input):
	#input = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
	height_cave = 750
	nbr_rock = 1000000000000
	falling_rock = [[[0,0],[1,0],[2,0],[3,0]],[[0,1],[1,0],[1,1],[1,2],[2,1]],[[0,0],[1,0],[2,0],[2,1],[2,2]],[[0,0],[0,1],[0,2],[0,3]],[[0,0],[0,1],[1,0],[1,1]]]
	cmd_gaz = input.strip()
	cursor_gaz = 0
	max_height = 0
	offset_height = 0
	cave = init_cave(height_cave)
	saved_cfg = ['0|0|']
	saved_floor_cfg = [0]
	saved_id_rock_cfg = [0]
	found_config = False
	o = 0

	while o < nbr_rock:
		print(o)
		pos = [2, max_height + 3 - offset_height]
		rock = falling_rock[o % 5]
		finish = False

		while not(finish):
			pos = move_gaz(cave, pos, rock, cmd_gaz[cursor_gaz] == '<')
			cursor_gaz += 1
			if cursor_gaz >= len(cmd_gaz):
				cursor_gaz = 0

			if can_go_down(cave, pos, rock):
				pos[1] -= 1
			else:
				place_rock(cave, rock, pos)
				finish = True
				max_height = max(max_height, get_max_height(pos, rock) + 1 + offset_height)

		solid_floor = find_solid_floor(cave)
		if solid_floor != 0:
			offset_height += solid_floor + 1
			new_cave = init_cave(height_cave)
			state_cave = ''
			for i in range(solid_floor + 1, len(cave)):
				if not('#' in cave[i]):
					break
				new_cave[i - (solid_floor + 1)] = cave[i]
				state_cave += ''.join(cave[i])

			cave = new_cave
			config = str(o % 5) + '|' + str(cursor_gaz) + '|' + state_cave
			if config in saved_cfg and not(found_config):
				found_config = True
				ind = saved_cfg.index(config)
				past_rock = saved_id_rock_cfg[ind]
				past_floor = saved_floor_cfg[ind]
				current_rock = o
				current_floor = offset_height
				diff_rock = current_rock - past_rock
				diff_floor = current_floor - past_floor

				rest_rock = nbr_rock - past_rock
				occurence = rest_rock // diff_rock
				max_height += diff_floor * (occurence - 1)
				offset_height += diff_floor * (occurence - 1)
				o += diff_rock * (occurence - 1)
			else:
				saved_cfg.append(config)
				saved_floor_cfg.append(offset_height)
				saved_id_rock_cfg.append(o)

		o += 1

	return max_height