#!/usr/bin/python

import sys

def init_elf(maps, muli_x, muli_y):
	elfs_pos = []
	for x in range(len(maps)):
		for y in range(len(maps[0])):
			if maps[x][y] == '#':
				elfs_pos.append(x * muli_x + y + muli_y)

	return elfs_pos

def perform_round(elfs_pos, rules, muli_x):
	tmp_elfs_pos = []

	# Propose
	for elf_pos in elfs_pos:
		around = [elf_pos - (muli_x + 1), elf_pos - muli_x, elf_pos - (muli_x - 1), elf_pos - 1, elf_pos + 1, elf_pos + (muli_x - 1), elf_pos + muli_x, elf_pos + (muli_x + 1)]
		found = False
		for pos in around:
			if pos in elfs_pos:
				found = True
				break

		if not(found):
			tmp_elfs_pos.append(elf_pos)
			continue

		append = False
		for rule in rules:
			to_check = [elf_pos + rule[0], elf_pos + rule[1], elf_pos + rule[2]]
			found = False
			for pos in to_check:
				if pos in elfs_pos:
					found = True
					break

			if not(found):
				tmp_elfs_pos.append(elf_pos + rule[1])
				append = True
				break

		if not(append):
			tmp_elfs_pos.append(elf_pos)

	new_elfs_pos = []

	for i in range(len(tmp_elfs_pos)):
		pos = tmp_elfs_pos[i]
		if not(pos in (tmp_elfs_pos[:i] + tmp_elfs_pos[i+1:])):
			new_elfs_pos.append(pos)
		else:
			new_elfs_pos.append(elfs_pos[i])

	move = False

	for i in range(len(new_elfs_pos)):
		if new_elfs_pos[i] != elfs_pos[i]:
			move = True
			break

	return new_elfs_pos, move

def calc_empty_space(elfs_pos, muli_x):
	min_x = sys.maxsize
	min_y = sys.maxsize
	max_x = -sys.maxsize
	max_y = -sys.maxsize

	for elf_pos in elfs_pos:
		x = elf_pos // muli_x
		y = elf_pos % muli_x

		min_x = min(x, min_x)
		min_y = min(y, min_y)
		max_x = max(x, max_x)
		max_y = max(y, max_y)

	rect_surf = (max_x - min_x + 1) * (max_y - min_y + 1)

	return rect_surf - len(elfs_pos)

def level1(input):
	muli_x = 1000
	rules = [[-muli_x - 1, -muli_x, -muli_x + 1], [muli_x - 1, muli_x, muli_x + 1], [-muli_x - 1, -1, muli_x - 1], [-muli_x + 1, 1, muli_x + 1]]
	step = 10

	#input = '....#..\n..###.#\n#...#.#\n.#...##\n#.###..\n##.#.##\n.#..#..\n'
	elfs_pos = init_elf(input.strip().split('\n'), muli_x, step * 2)

	for i in range(step):
		elfs_pos, move = perform_round(elfs_pos, rules[i % len(rules):] + rules[:i % len(rules)], muli_x)

	return calc_empty_space(elfs_pos, muli_x)

def level2(input):
	muli_x = 100000
	rules = [[-muli_x - 1, -muli_x, -muli_x + 1], [muli_x - 1, muli_x, muli_x + 1], [-muli_x - 1, -1, muli_x - 1], [-muli_x + 1, 1, muli_x + 1]]
	muli_y = 1000

	#input = '....#..\n..###.#\n#...#.#\n.#...##\n#.###..\n##.#.##\n.#..#..\n'
	elfs_pos = init_elf(input.strip().split('\n'), muli_x, muli_y)
	move = True
	step = 0

	while move:
		elfs_pos, move = perform_round(elfs_pos, rules[step % len(rules):] + rules[:step % len(rules)], muli_x)
		step += 1

	return step