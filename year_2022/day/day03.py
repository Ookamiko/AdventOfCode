#!/usr/bin/python

import re as regex

def valueOfLetter(letter):
	value = ord(letter)
	return value - 96 if value >= 97 else (value - 64 + 26)

def level1(input):
	sacks = input.strip().split('\n')
	result = 0

	for sack in sacks:
		comp1 = sack[:int(len(sack)/2)]
		comp2 = sack[int(len(sack)/2):]

		duplicate = regex.findall(r'[' + comp1 + r']', comp2)

		result += valueOfLetter(duplicate[0])

	return result

def level2(input):
	sacks = input.strip().split('\n')
	result = 0

	for i in range(0, len(sacks), 3):
		first_occ = regex.findall(r'[' + sacks[i] + r']', sacks[i + 1])
		second_occ = regex.findall(r'[' + ''.join(first_occ) + r']', sacks[i + 2])

		result += valueOfLetter(second_occ[0])

	return result