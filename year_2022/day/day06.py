#!/usr/bin/python

def level1(input):
	line = input.strip()
	result = 4

	for i in range(len(line)):
		letters = [x for x in line[i:i+4]]
		test = [*set(letters)]
		if len(test) == 4:
			break
		else:
			result += 1

	return result

def level2(input):
	line = input.strip()
	result = 14

	for i in range(len(line)):
		letters = [x for x in line[i:i+14]]
		test = [*set(letters)]
		if len(test) == 14:
			break
		else:
			result += 1

	return result