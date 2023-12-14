#!/usr/bin/python

def get_horizontal_reflexion(table):
	result = -1

	for i in range(1, len(table)):
		found = True
		for j in range(min(len(table[:i]), len(table[i:]))):
			if table[i + j] != table[i - (1 * (j + 1))]:
				found = False
				break

		if found:
			result = i
			break

	return result

def exactly_one_difference(line1, line2):
	one_diff = False
	for i in range(len(line1)):
		if line1[i] != line2[i]:
			if one_diff:
				one_diff = False
				break
			else:
				one_diff = True

	return one_diff

def get_horizontal_reflexion_with_smudge(table):
	result = -1

	for i in range(1, len(table)):
		smudge = False
		found = True
		for j in range(min(len(table[:i]), len(table[i:]))):
			if table[i + j] != table[i - (1 * (j + 1))]:
				if smudge:
					found = False
					break
				elif exactly_one_difference(table[i + j], table[i - (1 * (j + 1))]):
					smudge = True
				else:
					found = False
					break

		if found and smudge:
			result = i
			break

	return result

def invert_table(table):
	result = []

	for i in range(len(table[0])):
		line = ''
		for j in range(len(table)):
			line += table[j][i]

		result.append(line)

	return result

def level1(input):
	# Test value
	# input = '#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#\n'
	result = 0
	for part in input.strip().split('\n\n'):
		current = part.split('\n')

		index_reflexion = get_horizontal_reflexion(current)
		muli = 100

		if index_reflexion == -1:
			current = invert_table(current)
			index_reflexion = get_horizontal_reflexion(current)
			muli = 1

		result += index_reflexion * muli

	return result

def level2(input):
	# Test value
	# input = '#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#\n'
	result = 0
	for part in input.strip().split('\n\n'):
		current = part.split('\n')

		index_reflexion = get_horizontal_reflexion_with_smudge(current)
		muli = 100

		if index_reflexion == -1:
			current = invert_table(current)
			index_reflexion = get_horizontal_reflexion_with_smudge(current)
			muli = 1

		result += index_reflexion * muli

	return result