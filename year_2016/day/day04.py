#!/usr/bin/python

import re as regex

def IsRealRoom(room, test):
	tmpLetters = []
	for keys in list(dict.fromkeys(list(room))):
		if keys != '-':
			tmpLetters.append([keys, room.count(keys)])
	tmpLetters.sort(key=lambda x: x[0])
	tmpLetters.sort(key=lambda x: x[1], reverse=True)
	tmpLetters = [value[0] for value in tmpLetters[:len(test)]]

	for current in test:
		if not(current in tmpLetters):
			return False

	for i in range(len(test) - 1):
		if room.count(test[i]) < room.count(test[i + 1]):
			return False
		elif room.count(test[i]) == room.count(test[i + 1]) and test[i] > test[i + 1]:
			return False
	return True

def DecryptRoom(room, cypher):
	result = ''
	for letter in room:
		if letter == '-':
			result += ' '
		else:
			result += chr(((ord(letter) - ord('a') + cypher) % 26) + ord('a'))
	return result.strip()

def level1(input):
	reg = r'([a-z\-]+-)(\d+)\[([a-z]+)\]'
	addition = 0
	for current in input.strip().split('\n'):
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			if IsRealRoom(groups[0], groups[2]):
				addition += int(groups[1])
	return addition

def level2(input):
	reg = r'([a-z\-]+-)(\d+)\[([a-z]+)\]'
	realRoom = []
	for current in input.strip().split('\n'):
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			if IsRealRoom(groups[0], groups[2]):
				realRoom.append([groups[0], int(groups[1])])

	indice = 0
	for test in realRoom:
		name = DecryptRoom(test[0], test[1])
		if name == 'northpole object storage':
			indice = test[1]
			break

	return indice