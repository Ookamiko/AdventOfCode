#!/usr/bin/python

import sys, random

def init_base(is_level_1):
	table1 = [
		['gen-Pro', 'mic-Pro'],
		['gen-Cob', 'gen-Cur', 'gen-Rut', 'gen-Plu'],
		['mic-Cob', 'mic-Cur', 'mic-Rut', 'mic-Plu'],
		[],
	]

	table2 = [
		['gen-Pro', 'mic-Pro', 'gen-Ele', 'mic-Ele', 'gen-Dil', 'mic-Dil'],
		['gen-Cob', 'gen-Cur', 'gen-Rut', 'gen-Plu'],
		['mic-Cob', 'mic-Cur', 'mic-Rut', 'mic-Plu'],
		[],
	]

#	table1 = [
#		['mic-H', 'mic-L'],
#		['gen-H'],
#		['gen-L'],
#		[]
#	]
#	table2 = [
#		['mic-H', 'mic-L', 'gen-E', 'mic-E', 'gen-D', 'mic-D'],
#		['gen-H'],
#		['gen-L'],
#		[]
#	]
	return table1 if is_level_1 else table2

def stringify_state(table, pos_elev):
	string = ''
	for i in range(len(table)):
		table[i].sort()
		string += str(i) + ''.join(table[i])

	return string + '-E' + str(pos_elev)

def is_final_state(table):
	return len(table[0]) == 0 and len(table[1]) == 0 and len(table[2]) == 0

def is_state_already_seen(table, all_states, step, position_elev):
	current_state = stringify_state(table, position_elev)
	result = False
	if current_state in all_states[0]:
		index = all_states[0].index(current_state)
		if step >= all_states[1][index]:
			result = True
		else:
			all_states[1][index] = step
	else:
		all_states[0].append(current_state)
		all_states[1].append(step)

	return result

def is_state_valid(table):
	valid = True
	for floor in table:
		gen = []
		mic = []
		for element in floor:
			splits = element.split('-')
			if (splits[0] == 'gen'):
				gen.append(splits[1])
			else:
				mic.append(splits[1])

		if len(gen) != 0:
			for micro in mic:
				if not(micro in gen):
					valid = False
					break

		if not(valid):
			break

	return valid

def remove_unused_states(all_states, max_step):
	new_table = []

	new_table.append([])
	new_table.append([])

	for i in range(len(all_states[0])):
		if all_states[1][i] <= max_step - 2:
			new_table[0].append(all_states[0][i])
			new_table[1].append(all_states[1][i])

	return new_table

def copy_state(table):
	new_table = []

	for floor in table:
		new_floor = []
		for elem in floor:
			new_floor.append(elem)

		new_table.append(new_floor)

	return new_table

def get_all_moveable(table, position):
	moveable = []

	for i in range(len(table[position])):
		moveable.append([table[position][i]])
		for j in range(i + 1, len(table[position])):
			split1 = table[position][i].split('-')
			split2 = table[position][j].split('-')

			if (split1[0] != split2[0] and split1[1] != split2[1]):
				continue
			moveable.append([table[position][i], table[position][j]])

	random.shuffle(moveable)
	return moveable

def get_all_new_valid_state(table, position, all_states, step):
	moveable = get_all_moveable(table, position)
	can_go_down = False
	for i in range(position):
		if len(table[i]) != 0:
			can_go_down = True
			break

	new_state = []

	for move in moveable:
		if position != len(table) - 1:
			tmp_state = copy_state(table)
			for elem in move:
				tmp_state[position].remove(elem)
				tmp_state[position + 1].append(elem)

			if is_state_valid(tmp_state) and not(is_state_already_seen(tmp_state, all_states, step + 1, position + 1)):
				new_state.append({'table': tmp_state, 'pos': position+1})

		if can_go_down:
			bypass = False
			tmp_state = copy_state(table)
			for elem in move:
				tmp_state[position].remove(elem)
				tmp_state[position - 1].append(elem)

			if is_state_valid(tmp_state) and not(is_state_already_seen(tmp_state, all_states, step + 1, position - 1)):
				new_state.append({'table': tmp_state, 'pos': position-1})

	return new_state

def find_less_movement(table, position, all_states, step, max_step, current_path, found_path):
	if step >= max_step:
		return -1, found_path, all_states

	new_states = get_all_new_valid_state(table, position, all_states, step)

	if len(new_states) == 0:
		return -1, found_path, all_states

	# Pre check
	for current in new_states:
		string_state = stringify_state(current['table'], current['pos'])
		if is_final_state(current['table']):
			found_path = current_path + [string_state]
			return len(found_path) - 1, found_path, remove_unused_states(all_states, len(found_path) - 1)
		elif string_state in found_path:
			index = found_path.index(string_state)
			if step < index:
				found_path = current_path + [string_state] + found_path[index + 1:]
				return len(found_path) - 1, found_path, remove_unused_states(all_states, len(found_path) - 1)

	if len(found_path) != 0 and step >= max_step - 3:
		return -1, found_path, all_states

	min_found = max_step

	for current in new_states:
		tmp_step, found_path, all_states = find_less_movement(current['table'], current['pos'], all_states, step + 1, min_found, current_path + [stringify_state(current['table'], current['pos'])], found_path)
		if tmp_step != -1:
			min_found = min(min_found, tmp_step)

	print(str(min_found) + '-' + str(step) + '-' + str(len(all_states[0])) + "-" + str(sum(all_states[1])))
	return min_found, found_path, all_states

def level1(input):
	print("Solution finder is too long")
	table = init_base(True)
	all_states = [[stringify_state(table, 0)], [0]]
	found_path = []
	test, found_path, all_states = find_less_movement(table, 0, all_states, 0, 50, [all_states[0][0]], found_path)
	return test

def level2(input):
	print("Solution finder is too long")
	table = init_base(False)
	all_states = [[stringify_state(table, 0)], [0]]
	found_path = []
	test, found_path, all_states = find_less_movement(table, 0, all_states, 0, 75, [all_states[0][0]], found_path)
	return test