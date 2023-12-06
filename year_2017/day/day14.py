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

def perform_hash(key):
	table = [i for i in range(0, 256)]
	lengths = [ord(x) for x in key.strip()] + [17, 31, 73, 47, 23]
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

def convert_to_binary(hexa):
	result = ''
	for current in hexa:
		result += bin(int(current, 16))[2:].zfill(4)

	return result

def delete_zone(table, index, size=128):
	table[index] = '0'

	next_index = []

	if index % size != 0:
		next_index.append(index - 1)

	if index % size != size - 1:
		next_index.append(index + 1)

	if index - size >= 0:
		next_index.append(index - size)

	if index + size < size * size:
		next_index.append(index + size)

	for current in next_index:
		if table[current] == '1':
			delete_zone(table, current)

def level1(input):
	# Test value
	# input = 'flqrgnkx'
	key = input.strip() + '-'
	result = 0

	for i in range(128):
		hashed = perform_hash(key + str(i))
		binary = convert_to_binary(hashed)
		result += binary.count('1')

	return result

def level2(input):
	# Test value
	# input = 'flqrgnkx'
	key = input.strip() + '-'
	table = []

	for i in range(128):
		hashed = perform_hash(key + str(i))
		table += [x for x in convert_to_binary(hashed)]

	zone = 0

	for i in range(len(table)):
		if table[i] != '0':
			zone += 1
			delete_zone(table, i)

	return zone