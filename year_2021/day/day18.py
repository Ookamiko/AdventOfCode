#!/usr/bin/python

import re as regex
import math

def ParseNumber(str_number):
	reg = r'(\d+)'
	openBracket = str_number[0]
	result = []
	index = 1

	match = regex.match(reg, str_number[index:])
	if match:
		result.append(int(match.groups()[0]))
		index += len(match.groups()[0])
	else:
		tmp = ParseNumber(str_number[index:])
		result.append(tmp['result'])
		index += tmp['length']

	coma = str_number[index]
	index += 1

	match = regex.match(reg, str_number[index:])
	if match:
		result.append(int(match.groups()[0]))
		index += len(match.groups()[0])
	else:
		tmp = ParseNumber(str_number[index:])
		result.append(tmp['result'])
		index += tmp['length']

	closeBracket = str_number[index]
	index += 1

	return {'result': result, 'length': index}

def IncreaseNumber(number, toAdd, left):
	if left:
		if isinstance(number[1], int):
			number[1] += toAdd
		else:
			IncreaseNumber(number[1], toAdd, left)
	else:
		if isinstance(number[0], int):
			number[0] += toAdd
		else:
			IncreaseNumber(number[0], toAdd, left)


def ExplodeNumber(number, level=0):
	if level == 4:
		return {'left': number[0], 'right': number[1], 'explode': True, 'reset': True}

	if not(isinstance(number[0], int)):
		tmp = ExplodeNumber(number[0], level + 1)
		if tmp['explode']:
			if tmp['reset']:
				number[0] = 0
				tmp['reset'] = False
			if tmp['right'] != 0:
				if isinstance(number[1], int):
					number[1] += tmp['right']
				else:
					IncreaseNumber(number[1], tmp['right'], False)
				tmp['right'] = 0
			return tmp

	if not(isinstance(number[1], int)):
		tmp = ExplodeNumber(number[1], level + 1)
		if tmp['explode']:
			if tmp['reset']:
				number[1] = 0
				tmp['reset'] = False
			if tmp['left'] != 0:
				if isinstance(number[0], int):
					number[0] += tmp['left']
				else:
					IncreaseNumber(number[0], tmp['left'], True)
				tmp['left'] = 0
			return tmp

	return {'left': 0, 'right': 0, 'explode': False}

def SplitNumber(number):
	if isinstance(number[0], int):
		if number[0] > 9:
			number[0] = [math.floor(number[0] / 2), math.ceil(number[0] / 2)]
			return True
	else:
		if SplitNumber(number[0]):
			return True

	if isinstance(number[1], int):
		if number[1] > 9:
			number[1] = [math.floor(number[1] / 2), math.ceil(number[1] / 2)]
			return True
	else:
		if SplitNumber(number[1]):
			return True

	return False

def CalculMagnitude(number):
	number1 = 0
	number2 = 0
	if isinstance(number[0], int):
		number1 = 3 * number[0]
	else:
		number1 = 3 * CalculMagnitude(number[0])

	if isinstance(number[1], int):
		number2 = 2 * number[1]
	else:
		number2 = 2 * CalculMagnitude(number[1])

	return number1 + number2

def level1(input):
	#input = '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]\n[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]\n[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]\n[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]\n[7,[5,[[3,8],[1,4]]]]\n[[2,[2,2]],[8,[8,1]]]\n[2,9]\n[1,[[[9,3],9],[[9,0],[0,7]]]]\n[[[5,[7,4]],7],1]\n[[[[4,2],2],6],[8,7]]\n'
	allNumbers = input.strip().split('\n')
	number = ParseNumber(allNumbers[0])['result']
	for current in allNumbers[1:]:
		number = [number, ParseNumber(current)['result']]

		finish = False
		while not(finish):
			finish = True
			resultExplode = ExplodeNumber(number)
			if resultExplode['explode']:
				finish = False
				continue

			if SplitNumber(number):
				finish = False
				continue

	return CalculMagnitude(number)

def level2(input):
	#input = '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]\n[[[5,[2,8]],4],[5,[[9,9],0]]]\n[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]\n[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]\n[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]\n[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]\n[[[[5,4],[7,7]],8],[[8,3],8]]\n[[9,3],[[9,9],[6,[4,9]]]]\n[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]\n[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]\n'
	allNumbers = input.strip().split('\n')
	maxMagnitude = 0
	for i in range(len(allNumbers)):
		for j in range(len(allNumbers)):
			if i == j:
				continue

			number = [ParseNumber(allNumbers[i])['result'], ParseNumber(allNumbers[j])['result']]

			finish = False
			while not(finish):
				finish = True
				resultExplode = ExplodeNumber(number)
				if resultExplode['explode']:
					finish = False
					continue

				if SplitNumber(number):
					finish = False
					continue

			maxMagnitude = max(maxMagnitude, CalculMagnitude(number))

	return maxMagnitude