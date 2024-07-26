#!/usr/bin/python

import re as regex

def CreateObject(instructions):
	reg = r'([A-Za-z]*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.'
	toReturn = {}

	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			toReturn[groups[0]] = {'speed': int(groups[1]), 'speedTime': int(groups[2]), 'timeTotal': int(groups[2]) + int(groups[3]), 'point': 0}

	return toReturn

def CalculateWinnerDistance(obj, time):
	maxDist = 0
	winners = []
	for key in obj:
		element = obj[key]
		dist = element['speed'] * element['speedTime'] * (time // element['timeTotal']) + element['speed'] * min(time % element['timeTotal'], element['speedTime'])

		if dist > maxDist:
			maxDist = dist
			winners = [key]
		elif dist == maxDist:
			winners.append(key)

	return {'distance': maxDist, 'wins': winners}

def level1(input):
	parameters = CreateObject(input.strip().split('\n'))
	winners = CalculateWinnerDistance(parameters, 2503)
	return str(winners['distance'])

def level2(input):
	parameters = CreateObject(input.strip().split('\n'))
	for i in range(1, 2504):
		winners = CalculateWinnerDistance(parameters, i)
		for deer in winners['wins']:
			parameters[deer]['point'] += 1

	maximum = 0
	for deer in parameters:
		maximum = max(maximum, parameters[deer]['point'])

	return str(maximum)