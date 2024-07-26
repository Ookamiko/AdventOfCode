#!/usr/bin/python
import re as regex

def CreateRoutesObject(instructions):
	routes = {}
	reg = r'([A-Za-z]*) to ([A-Za-z]*) = (\d*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			group = matches.groups()
			ville1 = group[0]
			ville2 = group[1]
			dist = int(group[2])
			if not(ville1 in routes.keys()):
				routes[ville1] = {}
			if not(ville2 in routes.keys()):
				routes[ville2] = {}

			routes[ville1][ville2] = dist
			routes[ville2][ville1] = dist

	return routes

def CreateCitiesObject(instructions):
	cities = []
	reg = r'([A-Za-z]*) to ([A-Za-z]*) = (\d*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			group = matches.groups()
			city1 = group[0]
			city2 = group[1]
			if not(city1 in cities):
				cities.append(city1)
			if not(city2 in cities):
				cities.append(city2)

	return cities

def CreateAllPermutation(array):
	toReturn = []
	for i in range(len(array)):
		if len(array) == 1:
			toReturn.append([array[i]])
		else:
			sub = list(array)
			sub.remove(array[i])
			tmp = CreateAllPermutation(sub)
			for j in range(len(tmp)):
				newArray = list(tmp[j])
				newArray.append(array[i])
				toReturn.append(newArray)
	return toReturn


def level1(input):
	routes = CreateRoutesObject(input.strip().split('\n'))
	citys = CreateCitiesObject(input.strip().split('\n'))
	permutations = CreateAllPermutation(citys)
	minimum = 99999
	for travel in permutations:
		dist = 0
		for i in range(len(travel) - 1):
			city1 = travel[i]
			city2 = travel[i + 1]
			dist += routes[city1][city2]

		minimum = min(dist, minimum)

	return str(minimum)

def level2(input):
	routes = CreateRoutesObject(input.strip().split('\n'))
	citys = CreateCitiesObject(input.strip().split('\n'))
	permutations = CreateAllPermutation(citys)
	maximum = 0
	for travel in permutations:
		dist = 0
		for i in range(len(travel) - 1):
			city1 = travel[i]
			city2 = travel[i + 1]
			dist += routes[city1][city2]

		maximum = max(dist, maximum)

	return str(maximum)