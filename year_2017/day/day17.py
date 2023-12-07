#!/usr/bin/python

def get_next_table(table, index, jump, value):
	next_index = (index + jump) % len(table)
	new_table = table[:next_index + 1] + [value]

	if next_index + 1 < len(table):
		new_table += table[next_index + 1:]

	return [new_table, next_index + 1]

def level1(input):
	# Test value
	# input = '3'
	jump = int(input.strip())
	table = [0]
	index = 0

	for i in range(1, 2018):
		tmp = get_next_table(table, index, jump, i)
		table = tmp[0]
		index = tmp[1]

	index += 1

	if index == len(table):
		index = 0

	return table[index]

def level2(input):
	# Test value
	# input = '3'
	jump = int(input.strip())
	size_table = 1
	index = 0
	result = 0

	for i in range(1, 50000001):
		index = ((index + jump) % size_table) + 1
		size_table += 1
		if index == 1:
			result = i

	return result