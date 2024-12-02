#!/usr/bin/python

import re as regex

def init_table(column, row):
	table = []
	for i in range(column):
		table.append([' '] * row)
	return table

def rect_inst(table, column, row):
	for i in range(0, column):
		for j in range(0, row):
			table[i][j] = '#'

def slide_column(table, column, offset):
	to_slide = table[column]
	len_slide = len(to_slide)
	slided = to_slide[len_slide - offset:] + to_slide[:len_slide - offset]
	table[column] = slided

def slide_row(table, row, offset):
	to_slide = []
	for line in table:
		to_slide.append(line[row])

	len_slide = len(to_slide)
	slided = to_slide[len_slide - offset:] + to_slide[:len_slide - offset]

	for i in range(len(table)):
		table[i][row] = slided[i]

def display_table(table):
	for line in table:
		print(''.join(line))

def count_light(table):
	sum_light = 0
	for line in table:
		sum_light += line.count('#')

	return sum_light

def stringify_table(table):
	reverse_table = init_table(6, 50)
	for i in range(len(table)):
		for j in range(len(table[i])):
			reverse_table[j][i] = table[i][j]

	string = ''
	for line in reverse_table:
		string += ''.join(line) + '\n'

	return string

def level1(input):
	instructions = input.strip().split('\n')
	table = init_table(50, 6)
	for line in instructions:
		numbers = regex.findall(r'\d+', line)

		if 'rect' in line:
			rect_inst(table, int(numbers[0]), int(numbers[1]))
		elif 'column' in line:
			slide_column(table, int(numbers[0]), int(numbers[1]))
		else:
			slide_row(table, int(numbers[0]), int(numbers[1]))

	return count_light(table)

def level2(input):
	instructions = input.strip().split('\n')
	table = init_table(50, 6)
	for line in instructions:
		numbers = regex.findall(r'\d+', line)

		if 'rect' in line:
			rect_inst(table, int(numbers[0]), int(numbers[1]))
		elif 'column' in line:
			slide_column(table, int(numbers[0]), int(numbers[1]))
		else:
			slide_row(table, int(numbers[0]), int(numbers[1]))

	return "\n" + stringify_table(table)