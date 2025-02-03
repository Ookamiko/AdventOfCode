#!/usr/bin/python

def nbr_xmas(table, max_x, max_y, x, y):
	total = 0

	allowed_pos = []
	if x - 3 >= 0:
		allowed_pos.append([(x, y), (x-1, y), (x-2, y), (x-3, y)])
		if y - 3 >= 0:
			allowed_pos.append([(x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)])

		if y + 3 < max_y:
			allowed_pos.append([(x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3)])

	if x + 3 < max_y:
		allowed_pos.append([(x, y), (x+1, y), (x+2, y), (x+3, y)])

		if y - 3 >= 0:
			allowed_pos.append([(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)])

		if y + 3 < max_y:
			allowed_pos.append([(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)])

	if y - 3 >= 0:
		allowed_pos.append([(x, y), (x, y-1), (x, y-2), (x, y-3)])

	if y + 3 < max_y:
		allowed_pos.append([(x, y), (x, y+1), (x, y+2), (x, y+3)])

	for allowed in allowed_pos:
		pos1 = allowed[0]
		letter1 = table[pos1[0]][pos1[1]]
		pos2 = allowed[1]
		letter2 = table[pos2[0]][pos2[1]]
		pos3 = allowed[2]
		letter3 = table[pos3[0]][pos3[1]]
		pos4 = allowed[3]
		letter4 = table[pos4[0]][pos4[1]]

		text = letter1 + letter2 + letter3 + letter4
		if text == 'XMAS':
			total += 1

	return total

def nbr_x_mas(table, max_x, max_y, x, y):
	if (x - 1 < 0 or x + 1 >= max_x or
		y - 1 < 0 or y + 1 >= max_y):
		return 0

	letter1 = table[x-1][y-1]
	letter2 = table[x+1][y+1]

	if (letter1 == letter2 or
		not(letter1 in ['M','S']) or
		not(letter2 in ['M','S'])
		):
		return 0

	letter1 = table[x-1][y+1]
	letter2 = table[x+1][y-1]

	if (letter1 == letter2 or
		not(letter1 in ['M','S']) or
		not(letter2 in ['M','S'])
		):
		return 0

	return 1

def level1(input):
	#input = 'MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX\n'

	table = input.strip().split('\n')
	max_x = len(table)
	max_y = len(table[0])
	result = 0

	for x in range(max_x):
		for y in range(max_y):
			if table[x][y] == 'X':
				result += nbr_xmas(table, max_x, max_y, x, y)

	return result

def level2(input):
	#input = 'MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX\n'

	table = input.strip().split('\n')
	max_x = len(table)
	max_y = len(table[0])
	result = 0

	for x in range(max_x):
		for y in range(max_y):
			if table[x][y] == 'A':
				result += nbr_x_mas(table, max_x, max_y, x, y)

	return result