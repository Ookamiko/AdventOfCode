#!/usr/bin/python

import sys

def GetAllPossibilitiesForSize(packages, size):
	result = []
	for i in range(len(packages)):
		weight = packages[i]
		if weight > size:
			continue
		elif weight == size:
			result.append([weight])
		else:
			tmp = GetAllPossibilitiesForSize(packages[i + 1:], size - weight)
			for current in tmp:
				result.append([weight] + current)
	return result

def Multiply(array):
	result = 1
	for number in array:
		result *= number
	return result

def level1(input):
	packages = [int(value) for value in input.strip().split('\n')]
	group_size = sum(packages) // 3
	allPossibilities = GetAllPossibilitiesForSize(packages, group_size)
	allPossibilities.sort(key=lambda x: len(x))
	best_size = len(allPossibilities[0])
	best_entanglement = sys.maxsize
	i = 0
	while len(allPossibilities[i]) == best_size:
		best_entanglement = min(best_entanglement, Multiply(allPossibilities[i]))
		i += 1
	return best_entanglement

def level2(input):
	packages = [int(value) for value in input.strip().split('\n')]
	group_size = sum(packages) // 4
	allPossibilities = GetAllPossibilitiesForSize(packages, group_size)
	allPossibilities.sort(key=lambda x: len(x))
	best_size = len(allPossibilities[0])
	best_entanglement = sys.maxsize
	i = 0
	while len(allPossibilities[i]) == best_size:
		best_entanglement = min(best_entanglement, Multiply(allPossibilities[i]))
		i += 1
	return best_entanglement