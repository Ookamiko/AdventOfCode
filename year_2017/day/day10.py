#!/usr/bin/python

def perform_knot(table, length, index):
	end_index = (index + length - 1) % len(table)
	part = []

	if end_index < index:
		part = table[index:] + table[:end_index + 1]
	else:
		part = table[index:end_index + 1]

	part = part[::-1]

	for i in range(length):
		table[(index + i) % len(table)] = part[i]

	return end_index + 1

def level1(input):
	# Test value
	# input = '3,4,1,5'
	# table = [i for i in range(0, 5)]
	table = [i for i in range(0, 256)]
	lengths = [int(x) for x in input.strip().split(',')]
	skip = 0
	index = 0

	for length in lengths:
		index = (perform_knot(table, length, index) + skip) % len(table)
		skip += 1

	return table[0] * table[1]

def level2(input):
	# Test value
	table = [i for i in range(0, 256)]
	lengths = [ord(x) for x in input.strip()] + [17, 31, 73, 47, 23]
	skip = 0
	index = 0

	for i in range(64):
		for length in lengths:
			index = (perform_knot(table, length, index) + skip) % len(table)
			skip += 1

	sparse_hash = []
	for i in range(0, len(table), 16):
		tmp = 0
		for j in range(16):
			tmp ^= table[i + j]

		sparse_hash.append(tmp)

	hexa = [hex(x).replace('0x', '') for x in sparse_hash]
	result = ''

	for current in hexa:
		if len(current) != 2:
			result += '0'

		result += current

	return result