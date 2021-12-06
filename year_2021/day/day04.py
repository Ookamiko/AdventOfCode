#!/usr/bin/python

def CreateBoard(instructions):
	boards = []
	tmpBoard = []
	for current in instructions:
		if current == '':
			boards.append(list(tmpBoard))
			tmpBoard = []
		else:
			tmp = current.split(' ')
			for current in tmp:
				if current != '':
					tmpBoard.append(current)

	boards.append(list(tmpBoard))
	return boards

def Bingo(board, index):
	start_line = index - (index % 5)
	start_column = index % 5

	bingo = True
	for line in range(start_line, start_line + 5):
		if board[line] != '':
			bingo = False
			break

	if not(bingo):
		bingo = True
		for column in range(start_column, 25, 5):
			if board[column] != '':
				bingo = False
				break

	return bingo

def CalculTotalScore(board, last_number):
	total = 0
	for current in board:
		if current != '':
			total += int(current)

	return int(last_number) * total

def CrossNumber(boards, number):
	result = -1
	toRemove = []
	for current in boards:
		if number in current:
			index = current.index(number)
			current[index] = ''
			if Bingo(current, index):
				result = CalculTotalScore(current, number)
				toRemove.append(boards.index(current))

	toRemove = sorted(toRemove, reverse = True)
	for current in toRemove:
		print(toRemove)
		boards.pop(current)

	return result


def level1(input):
	list_number = input.strip().split('\n')[0].split(',')
	boards = CreateBoard(input.strip().split('\n')[2:])
	result = -1
	for number in list_number:
		result = CrossNumber(boards, number)
		if (result != -1):
			break

	return result

def level2(input):
	list_number = input.strip().split('\n')[0].split(',')
	boards = CreateBoard(input.strip().split('\n')[2:])
	result = -1
	for number in list_number:
		tmp = CrossNumber(boards, number)
		if (tmp != -1):
			result = tmp

	return result