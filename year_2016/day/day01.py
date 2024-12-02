#!/usr/bin/python

import re as regex

def AlreadySeen(positionSeen, position):
	for x,y in positionSeen:
		if x == position[0] and y == position[1]:
			return True
	return False

def level1(input):
	compass = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':0, 'y':-1}, {'x':1, 'y':0}]
	posCompass = 0
	x = 0
	y = 0
	reg = r'(R|L)(\d+)'
	for current in input.strip().split(', '):
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			if groups[0] == 'R':
				posCompass = (posCompass + 1) % 4
			else:
				posCompass = (posCompass + 4 - 1) % 4

			x += compass[posCompass]['x'] * int(groups[1])
			y += compass[posCompass]['y'] * int(groups[1])

	return abs(x) + abs(y)

def level2(input):
	compass = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':0, 'y':-1}, {'x':1, 'y':0}]
	posCompass = 0
	x = 0
	y = 0
	positionSeen = [[x,y]]
	reg = r'(R|L)(\d+)'
	for current in input.strip().split(', '):
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			if groups[0] == 'R':
				posCompass = (posCompass + 1) % 4
			else:
				posCompass = (posCompass + 4 - 1) % 4

			for i in range(int(groups[1])):
				x += compass[posCompass]['x']
				y += compass[posCompass]['y']
				if AlreadySeen(positionSeen, [x,y]):
					return abs(x) + abs(y)
				else:
					positionSeen.append([x,y])

	return "Not Found"