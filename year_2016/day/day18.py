#!/usr/bin/python

def next_row(current_row):
	row = ''

	for i in range(len(current_row)):

		if i == 0:
			row += '^' if current_row[i+1] == '^' else '.'
		elif i == len(current_row) - 1:
			row += '^' if current_row[i-1] == '^' else '.'
		else:
			row += '^' if current_row[i-1] != current_row[i+1] else '.'

	return row

def level1(input):
	row = input.strip()
	count = 0
	for i in range(40):
		count += row.count('.')
		row = next_row(row)
	return count

def level2(input):
	row = input.strip()
	count = 0
	for i in range(400000):
		count += row.count('.')
		row = next_row(row)
	return count