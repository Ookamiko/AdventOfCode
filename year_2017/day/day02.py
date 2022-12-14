#!/usr/bin/python

def level1(input):
	lines = input.strip().split('\n')
	count = 0
	for line in lines:
		numbers = [int(x) for x in line.split('\t')]
		numbers.sort()
		count += numbers[len(numbers) - 1] - numbers[0]

	return count

def level2(input):
	lines = input.strip().split('\n')
	count = 0
	for line in lines:
		numbers = [int(x) for x in line.split('\t')]
		numbers.sort(reverse=True)
		for i in range(len(numbers) - 1):
			for j in range(i + 1, len(numbers)):
				if numbers[i] % numbers[j] == 0:
					count += numbers[i] // numbers[j]

	return count