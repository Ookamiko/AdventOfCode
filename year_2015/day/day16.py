#!/usr/bin/python

import re as regex

ticket =  {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}

def level1(input):
	reg = r'^Sue (\d+):(.*)$'
	smallReg = r'([a-z]+): (\d+)'
	instructions = input.strip().split('\n')
	toReturn = ""

	for instruction in instructions:
		matches = regex.match(reg, instruction)
		if matches:
			groups = matches.groups()
			correct = True
			for current in groups[1].strip().split(', '):
				attribute = current.split(':')[0].strip()
				value = int(current.split(':')[1].strip())
				if not(ticket[attribute] == value):
					correct = False
					break
			if correct:
				toReturn = groups[0]
				break

	return toReturn

def level2(input):
	reg = r'^Sue (\d+):(.*)$'
	smallReg = r'([a-z]+): (\d+)'
	instructions = input.strip().split('\n')
	toReturn = ""

	for instruction in instructions:
		matches = regex.match(reg, instruction)
		if matches:
			groups = matches.groups()
			correct = True
			for current in groups[1].strip().split(', '):
				attribute = current.split(':')[0].strip()
				value = int(current.split(':')[1].strip())
				if (attribute == 'cats' or attribute == 'trees') and ticket[attribute] >= value:
					correct = False
					break
				elif (attribute == 'pomeranians' or attribute == 'goldfish') and ticket[attribute] <= value:
					correct = False
					break
				elif attribute != 'pomeranians' and attribute != 'goldfish' and attribute != 'cats' and attribute != 'trees' and ticket[attribute] != value:
					correct = False
					break
			if correct:
				toReturn = groups[0]
				break

	return toReturn
	return "Not implemented"