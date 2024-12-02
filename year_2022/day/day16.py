#!/usr/bin/python

import re as regex
import sys

def init_tunnel(instructions):
	tunnel = {}
	usefull = []

	for line in instructions:
		numbers = [int(x) for x in regex.findall(r'\d+', line)]
		valve = regex.findall(r'[A-Z]{2}', line)

		tunnel[valve[0]] = {'rate': numbers[0], 'access': valve[1:], 'dist': {}}
		if numbers[0] != 0:
			usefull.append(valve[0])

	return tunnel, usefull

def get_min_distance_to(pos, end, tunnel, step=0, max_step=sys.maxsize, seen=[]):
	if step >= max_step:
		return -1

	if pos == end:
		return step

	min_found = max_step

	for new_pos in tunnel[pos]['access']:
		if new_pos in seen:
			continue
		tmp_min = get_min_distance_to(new_pos, end, tunnel, step + 1, min_found, seen + [pos])
		if tmp_min != -1:
			min_found = min(tmp_min, min_found)

	return min_found

def get_next_pos(tunnel, pos, usefull, opened, step, max_step):
	next_pos = []

	for current in usefull:
		if current == pos:
			continue

		dist = tunnel[pos]['dist'][current]

		if not(current in opened) and max_step > step + dist + 1:
			next_pos.append(current)

	return next_pos

def get_max_released(pos, tunnel, step, max_step, usefull, rate=0, released=0, opened=[]):
	if step >= max_step:
		return -1

	max_released = released + rate * (max_step - step)

	next_pos = get_next_pos(tunnel, pos, usefull, opened, step, max_step)

	for current in next_pos:
		dist = tunnel[pos]['dist'][current]
		new_released = released + rate * (dist + 1)
		new_rate = rate + tunnel[current]['rate']
		tmp_released = get_max_released(current, tunnel, step + dist + 1, max_step, usefull, new_rate, new_released, opened + [current])
		max_released = max(max_released, tmp_released)

	return max_released

def get_all_path_possible(tunnel, pos, step, max_step, usefull, restrict=[]):
	result = []

	if len(usefull) == 1:
		if step + tunnel[pos]['dist'][usefull[0]] + 1 < max_step and not(usefull[0] in restrict):
			return [usefull]
		else:
			return []

	for i in range(len(usefull)):
		current = usefull[i]
		next_step = step + tunnel[pos]['dist'][current] + 1
		if next_step < max_step and not(current in restrict):
			result.append([current])
			for modulation in get_all_path_possible(tunnel, current, next_step, max_step, usefull[:i] + usefull[i+1:], restrict):
				result.append([current] + modulation)

	return result

def calcul_gaz_release(tunnel, start_pos, path, max_step):
	rate = 0
	step = 0
	released = 0
	current_pos = start_pos

	for next_pos in path:
		aug_step = tunnel[current_pos]['dist'][next_pos] + 1
		step += aug_step
		released += rate * aug_step
		rate += tunnel[next_pos]['rate']
		current_pos = next_pos

	released += rate * (max_step - step)

	return released

def level1(input):
	input = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\nValve BB has flow rate=13; tunnels lead to valves CC, AA\nValve CC has flow rate=2; tunnels lead to valves DD, BB\nValve DD has flow rate=20; tunnels lead to valves CC, AA, EE\nValve EE has flow rate=3; tunnels lead to valves FF, DD\nValve FF has flow rate=0; tunnels lead to valves EE, GG\nValve GG has flow rate=0; tunnels lead to valves FF, HH\nValve HH has flow rate=22; tunnel leads to valve GG\nValve II has flow rate=0; tunnels lead to valves AA, JJ\nValve JJ has flow rate=21; tunnel leads to valve II\n'
	tunnel, usefull = init_tunnel(input.strip().split('\n'))
	current_pos = 'AA'

	for start in usefull + [current_pos]:
		for end in usefull:
			if start == end:
				continue
			tunnel[start]['dist'][end] = get_min_distance_to(start, end, tunnel)

	modulations = get_all_path_possible(tunnel, current_pos, 0, 30, usefull)

	max_released = 0
	for path in modulations:
		max_released = max(max_released, calcul_gaz_release(tunnel, current_pos, path, 30))

	return max_released

def level2(input):
	print('Exec long')
	#input = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\nValve BB has flow rate=13; tunnels lead to valves CC, AA\nValve CC has flow rate=2; tunnels lead to valves DD, BB\nValve DD has flow rate=20; tunnels lead to valves CC, AA, EE\nValve EE has flow rate=3; tunnels lead to valves FF, DD\nValve FF has flow rate=0; tunnels lead to valves EE, GG\nValve GG has flow rate=0; tunnels lead to valves FF, HH\nValve HH has flow rate=22; tunnel leads to valve GG\nValve II has flow rate=0; tunnels lead to valves AA, JJ\nValve JJ has flow rate=21; tunnel leads to valve II\n'
	tunnel, usefull = init_tunnel(input.strip().split('\n'))
	start_pos = 'AA'

	for start in usefull + [start_pos]:
		for end in usefull:
			if start == end:
				continue
			tunnel[start]['dist'][end] = get_min_distance_to(start, end, tunnel)

	modulations_self = get_all_path_possible(tunnel, start_pos, 0, 26, usefull)

	print("max modulation " + str(len(modulations_self)))

	max_released = 0
	count = 0

	for path_self in modulations_self:
		count += 1
		released_self = calcul_gaz_release(tunnel, start_pos, path_self, 26)
		print('modulation ' + str(count) + ' - ' + str(max_released))
		for path_eleph in get_all_path_possible(tunnel, start_pos, 0, 26, usefull, path_self):
			released_eleph = calcul_gaz_release(tunnel, start_pos, path_eleph, 26)

			max_released = max(max_released, released_eleph + released_self)


	return max_released