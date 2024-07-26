#!/usr/bin/python

import sys

def init_blizzard(instructions):
	start = instructions[0].index('.')
	end = (len(instructions) - 1) * len(instructions[0]) + instructions[-1].index('.')

	blizzards = []
	modif_blizzards = []
	for x in range(1, len(instructions) - 1):
		for y in range(1, len(instructions[0]) - 1):
			char = instructions[x][y]
			if char == '.' or char == '#':
				continue
			blizzards.append(x * len(instructions[0]) + y)
			if char == '>':
				modif_blizzards.append(1)
			elif char == '<':
				modif_blizzards.append(-1)
			elif char == '^':
				modif_blizzards.append(-len(instructions[0]))
			else:
				modif_blizzards.append(len(instructions[0]))

	return start, end, blizzards, modif_blizzards, len(instructions), len(instructions[0])

def move_blizzards(blizzards, modif_blizzards, max_row, max_column, recurence=1):
	new_pos = []

	for blizzard in blizzards:
		new_pos.append(blizzard)

	for x in range(recurence):
		for i in range(len(new_pos)):
			tmp_pos = new_pos[i] + modif_blizzards[i]

			if tmp_pos % max_column == 0:
				tmp_pos += max_column - 2
			elif tmp_pos // max_column == 0:
				tmp_pos += max_column * (max_row - 2)
			elif tmp_pos > max_column * (max_row - 1):
				tmp_pos -= max_column * (max_row - 2)
			elif tmp_pos % max_column == max_column - 1:
				tmp_pos -= max_column - 2

			new_pos[i] = tmp_pos

	return new_pos

def get_new_pos(pos, end, max_row, max_column, start=1):
	tmp_pos = [pos - max_column, pos - 1, pos + 1, pos + max_column]
	new_pos = []

	for pos in tmp_pos:
		if (pos < max_column and pos != start) or (pos > max_column * (max_row - 1) and pos != end) or pos % max_column == 0 or pos % max_column == max_column - 1:
			continue
		new_pos.append(pos)

	return new_pos

def clean_seen(seen, min_found, max_row, max_column):
	less_than = min_found * 10 * max_row * max_column
	seen.sort()
	elem = seen.pop()
	while elem > less_than:
		elem = seen.pop()

	seen.append(elem)

def get_less_step(pos, end, step, max_step, blizzards, modif_blizzards, max_row, max_column, seen, total_step, start=0):
	if pos == end:
		return step
	elif step >= max_step - 1 or pos in blizzards or ((step * 10 * max_column * max_row) + pos) in seen:
		return -1

	seen.append((step * 10 * max_column * max_row) + pos)

	new_pos = get_new_pos(pos, end, max_row, max_column, start)
	new_pos.append(pos)
	new_pos.sort(reverse=pos < end)
	new_blizzards = move_blizzards(blizzards, modif_blizzards, max_row, max_column)
	min_found = max_step

	for current in new_pos:
		tmp_min = get_less_step(current, end, step + 1, min_found, new_blizzards, modif_blizzards, max_row, max_column, seen, total_step, start)
		if tmp_min != -1 and tmp_min < min_found:
			clean_seen(seen, min_found, max_row, max_column)
			min_found = tmp_min

	total_step[0] += 1
	if total_step[0] % 1000 == 0:
		print(str(step) + '\t' + str(min_found) + '\t' + str(len(seen)))

	return min_found

def level1(input):
	print('Exec long')
	sys.setrecursionlimit(10000)
	#input = '#.######\n#>>.<^<#\n#.<..<<#\n#>v.><>#\n#<^v^^>#\n######.#'
	start, end, blizzards, modif_blizzards, max_row, max_column = init_blizzard(input.strip().split('\n'))
	return get_less_step(start, end, 0, sys.maxsize, blizzards, modif_blizzards, max_row, max_column, [], [0])

def level2(input):
	print('Exec long')
	sys.setrecursionlimit(10000)
	#input = '#.######\n#>>.<^<#\n#.<..<<#\n#>v.><>#\n#<^v^^>#\n######.#'
	start, end, blizzards, modif_blizzards, max_row, max_column = init_blizzard(input.strip().split('\n'))
	print('First trip : start -> end')
	#start_end_1 = get_less_step(start, end, 0, sys.maxsize, blizzards, modif_blizzards, max_row, max_column, [], [0])
	start_end_1 = 230
	print('----')
	blizzards = move_blizzards(blizzards, modif_blizzards, max_row, max_column, start_end_1)
	print('Second trip : end -> start')
	end_start = get_less_step(end, start, 0, start_end_1 * 10, blizzards, modif_blizzards, max_row, max_column, [], [0], start)
	print('----')
	blizzards = move_blizzards(blizzards, modif_blizzards, max_row, max_column, end_start)
	print('Third trip : start -> end')
	start_end_2 = get_less_step(start, end, 0, start_end_1 * 2, blizzards, modif_blizzards, max_row, max_column, [], [0])
	print('----')
	return start_end_1 + start_end_2 + end_start