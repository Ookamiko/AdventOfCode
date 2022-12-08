#!/usr/bin/python

import hashlib
import re as regex

def is_valid(char, hashes, cursor, key, occ=1):
	for i in range(cursor + 1, cursor + 1001):
		if i >= len(hashes):
			hashes.append(multiple_hash(key + str(i), muli=occ))

		found = regex.findall(char + r'{5}', hashes[i])
		if len(found) != 0:
			return True

	return False

def multiple_hash(string, muli=1):
	for i in range(muli):
		string = hashlib.md5(string.encode()).hexdigest()
	return string

def level1(input):
	key = input.strip()
	#key = 'abc'
	count = 0
	hashes = []
	cursor = -1
	while count < 64:
		cursor += 1
		if cursor >= len(hashes):
			hashes.append(multiple_hash(key + str(cursor)))
		triplet = regex.findall(r'(.)\1\1', hashes[cursor])

		if len(triplet) != 0 and is_valid(triplet[0], hashes, cursor, key):
			count +=1

	return cursor

def level2(input):
	key = input.strip()
	#key = 'abc'
	count = 0
	hashes = []
	cursor = -1
	while count < 64:
		cursor += 1
		print(cursor)
		if cursor >= len(hashes):
			hashes.append(multiple_hash(key + str(cursor), muli=2017))
		triplet = regex.findall(r'(.)\1\1', hashes[cursor])

		if len(triplet) != 0 and is_valid(triplet[0], hashes, cursor, key, occ=2017):
			count +=1

	return cursor