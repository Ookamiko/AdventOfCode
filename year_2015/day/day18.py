#!/usr/bin/python

import math

def CreateInitialState(instructions, withBlock = False):
	board = []
	for current in instructions:
		board += list(current)



	if withBlock:
		lenRow = int(math.sqrt(len(board)))
		board[0] = "#"
		board[lenRow - 1] = "#"
		board[lenRow * (lenRow - 1)] = "#"
		board[len(board) - 1] = "#"

	return board

def NextState(previous, withBlock = False):
	nextArray = ['.'] * len(previous)
	lenRow = int(math.sqrt(len(previous)))

	for i in range(len(previous)):
		position = []
		if i % lenRow != 0:
			if i % lenRow != lenRow - 1:
				# Right and Left side OK
				position = [i - 1, i + 1, i - 1 - lenRow, i - lenRow, i + 1 - lenRow, i - 1 + lenRow, i + lenRow, i + 1 + lenRow]
			else:
				# Left side OK
				position = [i - 1, i - 1 - lenRow, i - lenRow, i - 1 + lenRow, i + lenRow]
		else:
			# Right side OK
			position = [i + 1, i - lenRow, i + 1 - lenRow, i + lenRow, i + 1 + lenRow]

		count = 0
		for current in position:
			if current < 0 or current >= len(previous):
				continue

			if previous[current] == '#':
				count += 1

			if count > 3:
				break

		if count == 3:
			nextArray[i] = '#'
		elif previous[i] == '#' and count == 2:
			nextArray[i] = '#'

	if withBlock:
		nextArray[0] = "#"
		nextArray[lenRow - 1] = "#"
		nextArray[lenRow * (lenRow - 1)] = "#"
		nextArray[len(nextArray) - 1] = "#"

	return nextArray

def DisplayCuteArray(array):
	row_len = int(math.sqrt(len(array)))
	for i in range(row_len + 1):
		print(''.join(array[i * row_len:(i * row_len) + row_len]))

def level1(input):
	state = CreateInitialState(input.strip().split('\n'))
	for i in range(100):
		state = NextState(state)
	return state.count('#')

def level2(input):
	state = CreateInitialState(input.strip().split('\n'), True)
	for i in range(100):
		state = NextState(state, True)
	return state.count('#')