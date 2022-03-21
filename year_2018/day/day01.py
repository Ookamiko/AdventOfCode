#!/usr/bin/python

def level1(input):
	lines = input.strip().split('\n')
	result = 0
	for line in lines:
		result += int(line.replace('+', ''))
	return result

def level2(input):
	lines = input.strip().split('\n')
	result = 0
	save = [0]
	finish = False

	while not(finish):
		for line in lines:
			result += int(line.replace('+', ''))
			if (result in save):
				finish = True
				break
			else:
				save.append(result)

	return result