#!/usr/bin/python

import re as regex

def IncrementPassword(password):
	end = False
	i = len(password) - 1
	while not(end):
		if password[i] != 'z':
			password[i] = chr(ord(password[i]) + 1)
			end = True
		else:
			password[i] = 'a'
			i -= 1

	if 'i' in password:
		index = password.index('i')
		password[index] = 'j'
		for i in range(index + 1, len(password)):
			password[i] = 'a'

	if 'l' in password:
		index = password.index('l')
		password[index] = 'm'
		for i in range(index + 1, len(password)):
			password[i] = 'a'

	if 'o' in password:
		index = password.index('o')
		password[index] = 'p'
		for i in range(index + 1, len(password)):
			password[i] = 'a'

	return password

def ValidatePassword(password):
	
	pair = r'([a-z])\1'
	matchPair = regex.findall(pair, password)
	if not(matchPair):
		return False
	elif len(matchPair) < 2:
		return False


	isSequential = False
	for i in range(len(password) - 2):
		char1 = ord(password[i])
		char2 = ord(password[i + 1])
		char3 = ord(password[i + 2])
		if char1 + 1 == char2 and char2 + 1 == char3:
			isSequential = True
			break

	if not(isSequential):
		return False

	return True

def level1(input):
	password = IncrementPassword(list(input.strip()))

	while not(ValidatePassword(''.join(password))):
		password = IncrementPassword(password)

	return ''.join(password)

def level2(input):
	password = IncrementPassword(list(input.strip()))

	while not(ValidatePassword(''.join(password))):
		password = IncrementPassword(password)

	password = IncrementPassword(password)

	while not(ValidatePassword(''.join(password))):
		password = IncrementPassword(password)

	return ''.join(password)