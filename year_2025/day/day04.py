#!/usr/bin/python

def nbr_paper_around(table, x, y):
	around = ''

	if x > 0:
		around += table[x - 1][y]
		if y > 0:
			around += table[x - 1][y - 1]
		if y < len(table[x - 1]) - 1:
			around += table[x - 1][y + 1]

	if x < len(table) - 1:
		around += table[x + 1][y]
		if y > 0:
			around += table[x + 1][y - 1]
		if y < len(table[x + 1]) - 1:
			around += table[x + 1][y + 1]

	if y > 0:
		around += table[x][y - 1]
	if y < len(table[x]) - 1:
		around += table[x][y + 1]

	return around.count('@')

def level1(input):
	#input = '..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.\n'
	result = 0

	lines = input.strip().split('\n')

	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if lines[i][j] == '@' and nbr_paper_around(lines, i, j) < 4:
				result += 1

	return result

def level2(input):
	#input = '..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.\n'
	result = 0

	lines = input.strip().split('\n')

	finish = False

	while not(finish):
		finish = True
		new_lines = []

		for i in range(len(lines)):
			new_line = ''

			for j in range(len(lines[0])):

				if lines[i][j] == '@' and nbr_paper_around(lines, i, j) < 4:
					result += 1
					finish = False
					new_line += '.'
				else:
					new_line += lines[i][j]

			new_lines.append(new_line)

		lines = new_lines

	return result