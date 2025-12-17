#!/usr/bin/python

def count_metadata(ribon, cursor):
	nbr_child = ribon[cursor]
	nbr_metadata = ribon[cursor + 1]

	result = 0
	cursor += 2

	for _ in range(nbr_child):
		cursor, metadata = count_metadata(ribon, cursor)
		result += metadata

	for _ in range(nbr_metadata):
		result += ribon[cursor]
		cursor += 1

	return cursor, result

def count_root_value(ribon, cursor):
	nbr_child = ribon[cursor]
	nbr_metadata = ribon[cursor + 1]

	cursor += 2
	childs_value = []

	for _ in range(nbr_child):
		cursor, metadata = count_root_value(ribon, cursor)
		childs_value.append(metadata)

	result = 0

	for _ in range(nbr_metadata):
		if nbr_child == 0:
			result += ribon[cursor]
		else:
			i = ribon[cursor] - 1
			if i >= 0 and i < len(childs_value):
				result += childs_value[i]

		cursor += 1

	return cursor, result

def level1(input):
	#input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2\n'

	ribon = [int(x) for x in input.strip().split(' ')]

	return count_metadata(ribon, 0)[1]

def level2(input):
	#input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2\n'

	ribon = [int(x) for x in input.strip().split(' ')]

	return count_root_value(ribon, 0)[1]