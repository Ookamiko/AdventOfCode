#!/usr/bin/python

import re as regex

def CreateMap(instructions):
	maps = {}
	reg = r'([a-zA-Z]+)-([a-zA-Z]+)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			place1 = matches.groups()[0]
			place2 = matches.groups()[1]

			if not(place1 in maps.keys()):
				maps[place1] = []

			if not(place2 in maps.keys()):
				maps[place2] = []

			maps[place1].append(place2)
			maps[place2].append(place1)

	return maps

def IsLowerCase(cave):
	return len(regex.findall(r'[a-z]+', cave)) != 0

def CreateAllPath(maps, location, path=[], allPath=[]):
	for current in maps[location]:
		if IsLowerCase(current) and current in path:
			continue

		if current == 'end':
			allPath.append(path + [current])
		else:
			CreateAllPath(maps, current, path + [current], allPath)

def CreateAllPathTime(maps, location, path=[], allPath=[], visitedSmallTwice=False):
	for current in maps[location]:
		tmp = visitedSmallTwice
		if IsLowerCase(current) and current in path:
			if current == 'start' or visitedSmallTwice:
				continue
			else:
				tmp = True

		if current == 'end':
			allPath.append(path + [current])
		else:
			CreateAllPathTime(maps, current, path + [current], allPath, tmp)

def level1(input):
	maps = CreateMap(input.strip().split('\n'))
	allPath = []
	CreateAllPath(maps, 'start', ['start'], allPath)
	return len(allPath)

def level2(input):
	maps = CreateMap(input.strip().split('\n'))
	allPath = []
	CreateAllPathTime(maps, 'start', ['start'], allPath)
	return len(allPath)