#!/usr/bin/python

import re as regex

def CreateSittingsObject(instructions):
	sittings = {}
	reg = r'([A-Za-z]*) would ([A-Za-z]*) (\d*) happiness units by sitting next to ([A-Za-z]*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			group = matches.groups()
			people1 = group[0]
			people2 = group[3]
			value = int(group[2]) * (-1 if group[1] == 'lose' else 1)
			if not(people1 in sittings.keys()):
				sittings[people1] = {}

			sittings[people1][people2] = value

	return sittings

def CreatePeopleObject(instructions):
	peoples = []
	reg = r'([A-Za-z]*) would [A-Za-z]* \d* happiness units by sitting next to [A-Za-z]*'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			group = matches.groups()
			people = group[0]
			if not(people in peoples):
				peoples.append(people)

	return peoples

def CreateAllPermutation(array):
	toReturn = []
	for i in range(len(array)):
		if len(array) == 1:
			toReturn.append([array[i]])
		else:
			sub = list(array)
			sub.remove(array[i])
			tmp = CreateAllPermutation(sub)
			for j in range(len(tmp)):
				newArray = list(tmp[j])
				newArray.append(array[i])
				toReturn.append(newArray)
	return toReturn

def level1(input):
	sittings = CreateSittingsObject(input.strip().split('\n'))
	peoples = CreatePeopleObject(input.strip().split('\n'))
	permutations = CreateAllPermutation(peoples)
	maximum = 0
	for permutation in permutations:
		value = 0
		for i in range(len(permutation) - 1):
			people1 = permutation[i]
			people2 = permutation[i + 1]

			value += sittings[people1][people2] + sittings[people2][people1]

		people1 = permutation[0]
		people2 = permutation[len(permutation) - 1]
		value += sittings[people1][people2] + sittings[people2][people1]

		maximum = max(value, maximum)

	return str(maximum)

def level2(input):
	sittings = CreateSittingsObject(input.strip().split('\n'))
	peoples = CreatePeopleObject(input.strip().split('\n'))
	peoples.append("myself")
	permutations = CreateAllPermutation(peoples)
	maximum = 0
	for permutation in permutations:
		value = 0
		for i in range(len(permutation) - 1):
			people1 = permutation[i]
			people2 = permutation[i + 1]

			if people1 != "myself" and people2 != "myself":
				value += sittings[people1][people2] + sittings[people2][people1]

		people1 = permutation[0]
		people2 = permutation[len(permutation) - 1]
		
		if people1 != "myself" and people2 != "myself":
			value += sittings[people1][people2] + sittings[people2][people1]

		maximum = max(value, maximum)

	return str(maximum)