#!/usr/bin/python

import re as regex

def CreateGrid(maxX, maxY):
	toReturn = []
	for i in range(maxX):
		toReturn.append([0] * maxY)
	return toReturn

def CreateCoordinates(instructions):
	coordinates = []
	maxX = 0
	maxY = 0
	reg = r'(\d*),(\d*) -> (\d*),(\d*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			x1 = int(groups[0])
			x2 = int(groups[2])
			y1 = int(groups[1])
			y2 = int(groups[3])
			maxX = max(maxX, x1, x2)
			maxY = max(maxY, y1, y2)
			coordinates.append([{'x': x1, 'y': y1}, {'x': x2, 'y': y2}])

	return [coordinates, maxX, maxY]

def ElaboratePlan(coords, grid, withDiags = False):
	for current in coords:
		minX = current[0]['x']
		maxX = current[1]['x']
		minY = current[0]['y']
		maxY = current[1]['y']
		reverseX = minX > maxX
		reverseY = minY > maxY
		if minX == maxX or minY == maxY:
			for x in range(minX, maxX + (-1 if reverseX else 1), -1 if reverseX else 1):
				for y in range(minY, maxY + (-1 if reverseY else 1), -1 if reverseY else 1):
					grid[x][y] += 1
		elif withDiags:
			for x, y in zip(range(minX, maxX + (-1 if reverseX else 1), -1 if reverseX else 1), range(minY, maxY + (-1 if reverseY else 1), -1 if reverseY else 1)):
				grid[x][y] += 1


def CountDangerousZone(grid):
	dangerousZone = 0
	for current in grid:
		dangerousZone += len(current) - current.count(0) - current.count(1)

	return dangerousZone

def level1(input):
	result = CreateCoordinates(input.strip().split('\n'))
	grid = CreateGrid(result[1] + 1, result[2] + 1)
	ElaboratePlan(result[0], grid)
	return CountDangerousZone(grid)

def level2(input):
	result = CreateCoordinates(input.strip().split('\n'))
	grid = CreateGrid(result[1] + 1, result[2] + 1)
	ElaboratePlan(result[0], grid, True)
	return CountDangerousZone(grid)