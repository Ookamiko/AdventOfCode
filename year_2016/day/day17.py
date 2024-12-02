#!/usr/bin/python

import hashlib, sys

def get_correct_next_path(x, y, hashe):
	next_path = []

	if x != 3 and ord(hashe[1]) > 97:
		next_path.append({'char': 'D', 'x': x+1, 'y': y})
	if y != 3 and ord(hashe[3]) > 97:
		next_path.append({'char': 'R', 'x': x, 'y': y+1})
	if x != 0 and ord(hashe[0]) > 97:
		next_path.append({'char': 'U', 'x': x-1, 'y': y})
	if y != 0 and ord(hashe[2]) > 97:
		next_path.append({'char': 'L', 'x': x, 'y': y-1})

	return next_path

def find_shortest_path(password, x, y, path, path_found):
	if len(path) >= len(path_found):
		return ''

	if x == 3 and y == 3:
		return path

	moves = get_correct_next_path(x, y, hashlib.md5((password + path).encode()).hexdigest()[0:4])

	for move in moves:
		tmp = find_shortest_path(password, move['x'], move['y'], path + move['char'], path_found)
		if tmp != '' and len(tmp) < len(path_found):
			path_found = tmp

	return path_found

def find_longest_path(password, x, y, path, path_found, max_path):
	if len(path) >= max_path:
		return ''

	if x == 3 and y == 3:
		return path

	moves = get_correct_next_path(x, y, hashlib.md5((password + path).encode()).hexdigest()[0:4])

	for move in moves:
		tmp = find_longest_path(password, move['x'], move['y'], path + move['char'], path_found, max_path)
		if tmp != '' and len(tmp) > len(path_found):
			path_found = tmp

	return path_found

def level1(input):
	password = input.strip()
	return find_shortest_path(password, 0, 0, '', ['U'] * 100)

def level2(input):
	password = input.strip()
	return len(find_longest_path(password, 0, 0, '', '', sys.maxsize))