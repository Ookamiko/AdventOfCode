#!/usr/bin/python

import re as regex

def level1(input):
	# Test value
	# input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n'
	valid = {'red': 12, 'green': 13, 'blue': 14}
	games = input.strip().split('\n')
	result = 0

	for game in games:
		match = regex.match(r'^Game (\d+):(.+)$', game)

		if match:
			group = match.groups()
			game_nbr = int(group[0])
			draws = regex.findall(r'\d+ blue|\d+ red|\d+ green', group[1])
			correct = True

			for draw in draws:
				tmp = draw.split(' ')
				if valid[tmp[1]] < int(tmp[0]):
					correct = False
					break

			if correct:
				result += game_nbr

	return result

def level2(input):
	# Test value
	# input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n'
	games = input.strip().split('\n')
	result = 0

	for game in games:
		maximums = {'red': 0, 'blue': 0, 'green': 0}
		draws = regex.findall(r'\d+ blue|\d+ red|\d+ green', game)

		for draw in draws:
			tmp = draw.split(' ')
			maximums[tmp[1]] = max(maximums[tmp[1]], int(tmp[0]))

		result += maximums['red'] * maximums['blue'] * maximums['green']

	return result