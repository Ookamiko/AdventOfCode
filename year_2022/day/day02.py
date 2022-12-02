#!/usr/bin/python

def level1(input):
	instructions = input.strip().split('\n')
	score = 0

	for line in instructions:
		chars = line.split(' ')

		if chars[1] == 'X':
			score += 1
			if chars[0] == 'A':
				score += 3
			elif chars[0] == 'B':
				score += 0
			else:
				score += 6
		elif chars[1] == 'Y':
			score += 2
			if chars[0] == 'A':
				score += 6
			elif chars[0] == 'B':
				score += 3
			else:
				score += 0
		else:
			score += 3
			if chars[0] == 'A':
				score += 0
			elif chars[0] == 'B':
				score += 6
			else:
				score += 3

	return score

def level2(input):
	instructions = input.strip().split('\n')
	score = 0

	for line in instructions:
		chars = line.split(' ')

		if chars[1] == 'X':
			score += 0
			if chars[0] == 'A':
				score += 3
			elif chars[0] == 'B':
				score += 1
			else:
				score += 2
		elif chars[1] == 'Y':
			score += 3
			if chars[0] == 'A':
				score += 1
			elif chars[0] == 'B':
				score += 2
			else:
				score += 3
		else:
			score += 6
			if chars[0] == 'A':
				score += 2
			elif chars[0] == 'B':
				score += 3
			else:
				score += 1

	return score