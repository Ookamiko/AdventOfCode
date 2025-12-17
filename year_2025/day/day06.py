#!/usr/bin/python

import re
import math

def level1(input):
	#input = '123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  \n'

	numbers = []
	operands = []

	lines = [x.strip() for x in input.strip().split('\n')]

	for line in lines[:len(lines) - 1]:
		numbers.append([int(x) for x in re.split(r'\s+', line)])

	operands = [x for x in re.split(r'\s+', lines[-1])]

	result = 0

	for i in range(len(numbers[0])):
		sub_result = 0 if operands[i] == '+' else 1

		for j in range(len(numbers)):
			if operands[i] == '+':
				sub_result += numbers[j][i]
			else:
				sub_result *= numbers[j][i]

		result += sub_result

	return result

def level2(input):
	#input = '123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  \n'

	numbers = []
	operands = []

	lines = [x for x in input.strip().split('\n')]
	operands = [x for x in re.split(r'\s+', lines.pop(-1))]

	number = ''
	sub_numbers = []

	for i in range(len(lines[0])):
		number = ''

		for j in range(len(lines)):

			number += lines[j][i]

		number = number.strip()

		if number == '':
			numbers.append(sub_numbers)
			sub_numbers = []
		else:
			sub_numbers.append(int(number))

	if len(sub_numbers) != 0:
		numbers.append(sub_numbers)

	result = 0

	for i in range(len(numbers)):
		if operands[i] == '+':
			result += sum(numbers[i])
		else:
			result += math.prod(numbers[i])

	return result