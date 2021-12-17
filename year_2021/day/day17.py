#!/usr/bin/python

import re as regex
import sys

def GetAllXT(minX, maxX):
	result = []
	for x in range(maxX, 0, -1):
		for t in range(1, x + 1):
			position = t * x - (t * (t - 1) // 2)
			if position > maxX:
				break
			if position < minX:
				continue

			result.append([x, t])

	return result

def GetAllVelocity(tableX, minY, maxY, yBestHeight, tBestHeight):
	result = []
	for x, t in tableX:
		for y in range(minY, yBestHeight + 1):
			for realT in range(t, (t + 1) if x != t else (tBestHeight)):
				position = realT * y - (realT * (realT - 1) // 2)
				if position < minY:
					break
				if position > maxY:
					continue

				result.append(str(x) + ',' + str(y))

	return result

def level1(input):
	#input = 'target area: x=20..30, y=-10..-5'
	reg = r'-?\d+'
	numbers = regex.findall(reg, input)
	minX = int(numbers[0])
	maxX = int(numbers[1])
	minY = int(numbers[2])
	maxY = int(numbers[3])
	yBestHeight = abs(minY) - 1
	return (yBestHeight * (yBestHeight + 1)) // 2

def level2(input):
	#input = 'target area: x=20..30, y=-10..-5'
	reg = r'-?\d+'
	numbers = regex.findall(reg, input)
	minX = int(numbers[0])
	maxX = int(numbers[1])
	minY = int(numbers[2])
	maxY = int(numbers[3])

	possibleX = GetAllXT(minX, maxX)
	tmp = GetAllVelocity(possibleX, minY, maxY, abs(minY) - 1, abs(minY) * 2 + 1)
	result = list(dict.fromkeys(tmp))

	return len(result)