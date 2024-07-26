#!/usr/bin/python

def spin(table, size):
	pivot = len(table) - size
	table = table[pivot:] + table[:pivot]

	return table

def exchange(table, pos1, pos2):
	tmp = table[pos1]
	table[pos1] = table[pos2]
	table[pos2] = tmp

	return table

def partner(table, prog1, prog2):
	pos1 = table.index(prog1)
	pos2 = table.index(prog2)
	exchange(table, pos1, pos2)

	return table

def level1(input):
	# Test value
	# input = 's1,x3/4,pe/b'
	# table = ['a','b','c','d','e']
	table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
	lines = input.strip().split(',')

	for line in lines:
		if line[0] == 's':
			table = spin(table, int(line[1:]))
		elif line[0] == 'x':
			tmp = [int(x) for x in line[1:].split('/')]
			table = exchange(table, tmp[0], tmp[1])
		else:
			tmp = line[1:].split('/')
			table = partner(table, tmp[0], tmp[1])

	return ''.join(table)

def level2(input):
	# Test value
	# input = 's1,x3/4,pe/b'
	# table = ['a','b','c','d','e']
	table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
	lines = input.strip().split(',')
	start = ''.join(table)
	permut = 0

	for i in range(1000000000):
		for line in lines:
			if line[0] == 's':
				table = spin(table, int(line[1:]))
			elif line[0] == 'x':
				tmp = [int(x) for x in line[1:].split('/')]
				table = exchange(table, tmp[0], tmp[1])
			else:
				tmp = line[1:].split('/')
				table = partner(table, tmp[0], tmp[1])

		if ''.join(table) == start:
			permut = i + 1
			break

	for i in range(1000000000 % permut):
		for line in lines:
			if line[0] == 's':
				table = spin(table, int(line[1:]))
			elif line[0] == 'x':
				tmp = [int(x) for x in line[1:].split('/')]
				table = exchange(table, tmp[0], tmp[1])
			else:
				tmp = line[1:].split('/')
				table = partner(table, tmp[0], tmp[1])

	return ''.join(table)