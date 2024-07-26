#!/usr/bin/python

def reduce_cave(cave, min_y, max_y, max_x, start_y, need_floor=False):
	new_cave = []

	if need_floor:
		size_floor = (max_x + 2) * 2 + 1
		middle = start_y
		min_y = middle - size_floor//2
		max_y = middle + size_floor//2

	for x in range(0, max_x + 1):
		row = []
		for y in range(min_y, max_y + 1):
			row.append(cave[x][y])
		new_cave.append(row)

	if need_floor:
		new_cave.append(['.'] * len(new_cave[0]))
		new_cave.append(['#'] * len(new_cave[0]))

	return new_cave, start_y - min_y

def init_cave(instructions, start_y, need_floor=False):
	cave = []
	min_y = 1000
	max_y = 0
	max_x = 0
	for i in range(1000):
		row = ['.'] * 1000
		cave.append(row)

	for line in instructions:
		sections = [x.strip() for x in line.split('->')]
		for i in range(len(sections) - 1):
			tmp1 = [int(x) for x in sections[i].split(',')]
			tmp2 = [int(x) for x in sections[i + 1].split(',')]

			start = []
			end = []

			if tmp1[0] < tmp2[0] or tmp1[1] < tmp2[1]:
				start = tmp1
				end = tmp2
			else:
				start = tmp2
				end = tmp1

			for x in range(start[1], end[1] + 1):
				for y in range(start[0], end[0] + 1):
					min_y = min(y, min_y)
					max_y = max(y, max_y)
					max_x = max(x, max_x)
					cave[x][y] = '#'

	cave[0][start_y] = '+'
	return reduce_cave(cave, min_y, max_y, max_x, start_y, need_floor)

def display_cave(cave):
	for row in cave:
		print(''.join(row))

def sand_fall(cave, start_y):
	y = start_y
	finish = True
	for x in range(len(cave) - 1):
		if y < 0 or y >= len(cave[0]):
			break

		below = []
		if y - 1 < 0:
			below = ['.', cave[x + 1][y], cave[x + 1][y + 1]]
		elif y + 1 >= len(cave[0]):
			below = [cave[x + 1][y - 1], cave[x + 1][y], '.']
		else:
			below = [cave[x + 1][y - 1], cave[x + 1][y], cave[x + 1][y + 1]]

		if below[1] != '.':
			if below[0] == '.':
				y -= 1
			elif below[2] == '.':
				y += 1
			else:
				cave[x][y] = 'o'
				finish = False
				break

	return finish

def sand_fall_infinite(cave, start_y):
	y = start_y
	finish = True
	for x in range(len(cave) - 1):
		if y < 0 or y >= len(cave[0]):
			break

		below = []
		if y - 1 < 0:
			below = ['.', cave[x + 1][y], cave[x + 1][y + 1]]
		elif y + 1 >= len(cave[0]):
			below = [cave[x + 1][y - 1], cave[x + 1][y], '.']
		else:
			below = [cave[x + 1][y - 1], cave[x + 1][y], cave[x + 1][y + 1]]

		if below[1] != '.':
			if below[0] == '.':
				y -= 1
			elif below[2] == '.':
				y += 1
			else:
				cave[x][y] = 'o'
				finish = x == 0 and y == start_y
				break

	return finish

def count_sand(cave):
	count = 0
	for row in cave:
		count += row.count('o')

	return count

def level1(input):
	#input = '498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9\n'
	cave, start = init_cave(input.strip().split('\n'), 500)
	finish = False
	while not(finish):
		finish = sand_fall(cave, start)

	return count_sand(cave)

def level2(input):
	#input = '498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9\n'
	cave, start = init_cave(input.strip().split('\n'), 500, need_floor=True)
	finish = False
	while not(finish):
		finish = sand_fall_infinite(cave, start)

	return count_sand(cave)