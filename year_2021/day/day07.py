#!/usr/bin/python

import sys

def CalculConso(positions, place):
	conso = 0
	for position in positions:
		conso += abs(position - place)
	return conso

def CalculRealConso(positions, place):
	conso = 0
	for position in positions:
		distance = abs(position - place)
		conso += distance * (distance + 1) // 2
	return conso	

def level1(input):
	position = [int(value) for value in input.strip().split(',')]
	position.sort()
	minConso = sys.maxsize
	for i in range(position[0], position[len(position) - 1] + 1):
		conso = CalculConso(position, i)
		if conso <= minConso:
			minConso = conso
		else:
			break

	return minConso

def level2(input):
	position = [int(value) for value in input.strip().split(',')]
	position.sort()
	minConso = sys.maxsize
	for i in range(position[0], position[len(position) - 1] + 1):
		conso = CalculRealConso(position, i)
		print(conso)
		if conso <= minConso:
			minConso = conso
		else:
			break

	return minConso