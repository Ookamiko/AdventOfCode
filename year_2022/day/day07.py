#!/usr/bin/python

import sys

def create_tree(instructions, cursor, name_folder):
	folder = {'size': 0, 'name': name_folder, 'dirs': []}
	is_ls = True

	while True and cursor < len(instructions):
		cmd = instructions[cursor].split(' ')

		if is_ls:

			if cmd[0] == '$':
				is_ls = False

				if cmd[2] == '..':
					break
				else:
					new_folder, cursor = create_tree(instructions, cursor + 2, cmd[2])
					folder['dirs'].append(new_folder)
					folder['size'] += new_folder['size']

			elif cmd[0] != 'dir':
				folder['size'] += int(cmd[0])

		else:
			if cmd[2] == '..':
				break
			else:
				new_folder, cursor = create_tree(instructions, cursor + 2, cmd[2])
				folder['dirs'].append(new_folder)
				folder['size'] += new_folder['size']

		cursor += 1

	return folder, cursor

def sum_size_less_than(folder, max_value):
	value = 0

	if folder['size'] <= max_value:
		value += folder['size']

	for current in folder['dirs']:
		value += sum_size_less_than(current, max_value)

	return value

def less_size_found_to_free_space(folder, minimum_value):
	value = sys.maxsize

	if folder['size'] >= minimum_value:
		value = folder['size']

	for current in folder['dirs']:
		value = min(value, less_size_found_to_free_space(current, minimum_value))

	return value

def level1(input):
	#input = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n'
	instructions = input.strip().split('\n')

	tree, cursor = create_tree(instructions, 2, '/')

	return sum_size_less_than(tree, 100000)

def level2(input):
	#input = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n'
	instructions = input.strip().split('\n')

	tree, cursor = create_tree(instructions, 2, '/')
	size_needed = 30000000
	size_total = 70000000

	return less_size_found_to_free_space(tree, size_needed - (size_total - tree['size']))