#!/usr/bin/python

def level1(input):
	#input = '.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............\n'

	lines = input.strip().split('\n')

	cursors = set()
	cursors.add(lines[0].index('S'))
	result = 0

	for line in lines[1:]:
		new_cursors = set()

		for c in cursors:
			if line[c] == '^':
				result += 1

				if c != 0:
					new_cursors.add(c - 1)

				if c < len(lines[0]) - 1:
					new_cursors.add(c + 1)
			else:
				new_cursors.add(c)

		cursors = new_cursors

	return result

def level2(input):
	#input = '.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............\n'

	lines = input.strip().split('\n')

	start = lines[0].index('S')

	cursors = set()
	cursors.add(start)

	result = [0] * len(lines[0])
	result[start] += 1

	for line in lines[1:]:
		new_cursors = set()

		for c in cursors:
			if line[c] == '^':

				tmp_count = result[c]
				result[c] = 0

				if c != 0:
					result[c - 1] += tmp_count
					new_cursors.add(c - 1)

				if c < len(lines[0]) - 1:
					result[c + 1] += tmp_count
					new_cursors.add(c + 1)
			else:
				new_cursors.add(c)

		cursors = new_cursors

	return sum(result)