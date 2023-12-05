#!/usr/bin/python

import re as regex

def level1(input):
	# Test value
	# input = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n'
	lines = input.strip().split('\n')
	result = 0

	for line in lines:
		card = line.split(':')[1]
		tmp = card.split('|')
		winning = [int(x) for x in regex.findall(r'\d+', tmp[0])]
		personnal = [int(x) for x in regex.findall(r'\d+', tmp[1])]
		power = -1

		for nbr in personnal:
			if nbr in winning:
				power += 1

		if power != -1:
			result += pow(2, power)

	return result

def level2(input):
	# Test value
	# input = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n'
	lines = input.strip().split('\n')
	gain_cards = [1 for x in range(len(lines))]
	index = -1

	for line in lines:
		index += 1
		card = line.split(':')[1]
		tmp = card.split('|')
		winning = [int(x) for x in regex.findall(r'\d+', tmp[0])]
		personnal = [int(x) for x in regex.findall(r'\d+', tmp[1])]
		win = 0

		for nbr in personnal:
			if nbr in winning:
				win += 1

		for i in range(1, win + 1):
			gain_cards[index + i] += gain_cards[index]

	return sum(gain_cards)