#!/usr/bin/python

def level1(input):
	numbers = [int(x) for x in input.strip()]
	count = numbers[0] if numbers[0] == numbers[len(numbers) - 1] else 0

	for i in range(len(numbers) - 1):
		if numbers[i] == numbers[i + 1]:
			count += numbers[i]

	return count

def level2(input):
	numbers = [int(x) for x in input.strip()]
	count = 0

	for i in range(len(numbers) // 2):
		if numbers[i] == numbers[i + len(numbers) // 2]:
			count += numbers[i] * 2

	return count