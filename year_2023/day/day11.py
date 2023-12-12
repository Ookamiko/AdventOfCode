#!/usr/bin/python

def expand_vertical(univers):
	result = []
	for line in univers:
		if not('#' in line):
			result.append(['.'] * len(line))

		result.append(line)

	return result

def expand_horizontal(univers):
	result = []
	indexes = []
	for i in range(len(univers[0])):
		indexes.append(i)

	for line in univers:
		to_remove = []
		for test in indexes:
			if line[test] == '#':
				to_remove.append(test)

		for index in to_remove:
			indexes.remove(index)

	for line in univers:
		offset = 0
		new_line = []
		for to_add in indexes:
			new_line += line[offset:to_add] + (['.'] * muli)
			offset = to_add

		new_line += line[offset:]
		result.append(new_line)

	return result

def expand_univers(univers):
	univers = expand_vertical(univers, muli)

	univers = expand_horizontal(univers, muli)

	return univers

def find_empty(univers):
	hori = []
	verti = []

	for i in range(len(univers[0])):
		verti.append(i)

	for i in range(len(univers)):
		if not('#' in univers[i]):
			hori.append(i)

		to_remove = []
		for test in verti:
			if univers[i][test] == '#':
				to_remove.append(test)

		for index in to_remove:
			verti.remove(index)

	return [hori, verti]

def get_coord_galaxy(univers):
	coords = []

	for i in range(len(univers)):
		for j in range(len(univers[i])):
			if univers[i][j] == '#':
				coords.append([i, j])

	return coords

def calc_dist(start, end):
	return abs(end[0] - start[0]) + abs(end[1] - start[1])

def calc_dist_advance(start, end, coords_empty, muli):
	base = abs(end[0] - start[0]) + abs(end[1] - start[1])

	min_x = min(start[0], end[0])
	max_x = max(start[0], end[0])
	min_y = min(start[1], end[1])
	max_y = max(start[1], end[1])

	factor = 0

	for x in coords_empty[0]:
		if x > min_x and x < max_x:
			factor += 1

	for y in coords_empty[1]:
		if y > min_y and y < max_y:
			factor += 1

	return base + factor * muli

def display_univers(univers):
	for line in univers:
		print(''.join(line))

def level1(input):
	# Test value
	# input = '...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....\n'
	lines = input.strip().split('\n')
	univers = []
	for line in lines:
		univers.append([x for x in line])

	univers = expand_univers(univers)
	coords_gal = get_coord_galaxy(univers)

	result = 0

	for i in range(len(coords_gal)):
		start = coords_gal[i]
		for end in coords_gal[i + 1:]:
			result += calc_dist(start, end)

	return result

def level2(input):
	# Test value
	# input = '...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....\n'
	lines = input.strip().split('\n')
	univers = []
	for line in lines:
		univers.append([x for x in line])

	coords_empty = find_empty(univers)
	coords_gal = get_coord_galaxy(univers)

	result = 0

	for i in range(len(coords_gal)):
		start = coords_gal[i]
		for end in coords_gal[i + 1:]:
			result += calc_dist_advance(start, end, coords_empty, 999999)

	return result