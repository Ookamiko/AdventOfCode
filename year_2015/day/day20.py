#!/usr/bin/python

import math

def GetMultipleForHouse(house):
	result = []
	for i in range(1, int(math.sqrt(house)) + 1):
		if house % i == 0:
			if house / i == i:
				result.append(i)
			else:
				result.append(i)
				result.append(int(house / i))
	return result

def GetMultipleForHouseNotInfinite(house):
	result = []
	for i in range(1, min(house, 50) + 1):
		if house % i == 0:
			result.append(int(house / i))
	return result

def level1(input):
	house = 0
	present = 0
	while present < int(input.strip()):
		house += 1
		multiples = GetMultipleForHouse(house)
		present = sum([value * 10 for value in multiples])
		print(str(house) + ": " + str(present))

	return house

def level2(input):
	house = 0
	present = 0
	while present < int(input.strip()):
		house += 1
		multiples = GetMultipleForHouseNotInfinite(house)
		present = sum([value * 11 for value in multiples])
		print(str(house) + ": " + str(present))
	return house