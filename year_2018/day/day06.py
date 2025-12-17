#!/usr/bin/python

import math
import sys

def get_closest_loc(locations, x, y):
	result = []
	min_found = math.inf

	for i in range(len(locations)):
		dist = abs(x - locations[i][0]) + abs(y - locations[i][1])

		if dist < min_found:
			min_found = dist
			result = [i]
		elif dist == min_found:
			result.append(i)

	return result

def get_dist_to_all_loc(locations, x, y):
	result = 0
	for i in range(len(locations)):
		result += abs(x - locations[i][0]) + abs(y - locations[i][1])

	return result

def count_safe_area_new(locations, start_x, start_y, max_allowed):
	to_test = [[start_x, start_y]]
	visited = [f'{start_x};{start_y}']
	result = 0

	while len(to_test) > 0:
		x, y = to_test.pop()

		if get_dist_to_all_loc(locations, x, y) < max_allowed:
			result += 1

			if not(f'{x+1};{y}' in visited):
				to_test.append([x+1,y])
				visited.append(f'{x+1};{y}')

			if not(f'{x-1};{y}' in visited):
				to_test.append([x-1,y])
				visited.append(f'{x-1};{y}')

			if not(f'{x};{y+1}' in visited):
				to_test.append([x,y+1])
				visited.append(f'{x};{y+1}')

			if not(f'{x};{y-1}' in visited):
				to_test.append([x,y-1])
				visited.append(f'{x};{y-1}')

	return result

def level1(input):
	#input = '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9\n'

	locations = []
	area_loc = []

	min_x = math.inf
	max_x = -math.inf
	min_y = math.inf
	max_y = -math.inf

	for location in input.strip().split('\n'):
		pos = [int(x.strip()) for x in location.split(',')]
		locations.append(pos)
		area_loc.append(0)

		min_x = min(min_x, pos[0])
		max_x = max(max_x, pos[0])
		min_y = min(min_y, pos[1])
		max_y = max(max_y, pos[1])

	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			close_loc = get_closest_loc(locations, x, y)

			if len(close_loc) == 1:
				loc = close_loc[0]

				if area_loc[loc] != -1:
					if (x == min_x or y == min_y or x == max_x or y == max_y):
						area_loc[loc] = -1
					else:
						area_loc[loc] += 1

	return max(area_loc)

def level2(input):
	#input = '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9\n'
	#max_allowed = 32

	max_allowed = 10000

	locations = []

	min_x = math.inf
	max_x = -math.inf
	min_y = math.inf
	max_y = -math.inf

	for location in input.strip().split('\n'):
		pos = [int(x.strip()) for x in location.split(',')]
		locations.append(pos)

		min_x = min(min_x, pos[0])
		max_x = max(max_x, pos[0])
		min_y = min(min_y, pos[1])
		max_y = max(max_y, pos[1])

	x = min_x + (max_x - min_x) // 2
	y = min_y + (max_y - min_y) // 2

	return count_safe_area_new(locations, x, y, max_allowed)