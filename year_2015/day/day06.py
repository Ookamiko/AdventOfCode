#!/usr/bin/python
import re as regex

def CreateDefaultTuple(defaultValue = False):
	toReturn = []
	for i in range(1000):
		toReturn.append([defaultValue] * 1000)
	return toReturn

def ManipulateLight(lights, xmin, ymin, xmax, ymax, option):
	for i in range(xmin, xmax + 1):
		for j in range(ymin, ymax + 1):
			if (option == "turn on"):
				lights[i][j] = True
			elif (option == "turn off"):
				lights[i][j] = False
			elif (option == "toggle"):
				lights[i][j] = not(lights[i][j])

	return lights

def DimingLight(lights, xmin, ymin, xmax, ymax, option):
	for i in range(xmin, xmax + 1):
		for j in range(ymin, ymax + 1):
			if (option == "turn on"):
				lights[i][j] += 1
			elif (option == "turn off"):
				lights[i][j] = max(lights[i][j] - 1, 0)
			elif (option == "toggle"):
				lights[i][j] += 2

	return lights

def CountLightOn(lights):
	toReturn = 0
	for i in range(len(lights)):
		toReturn += lights[i].count(True)

	return toReturn

def CountIntensity(lights):
	toReturn = 0
	for i in range(len(lights)):
		for j in range(len(lights)):
			toReturn += lights[i][j]

	return toReturn

def level1(input):
	lights = CreateDefaultTuple()
	str_list = input.split("\n")
	reg = r'^([a-z]*\s*[a-z]*) (\d*),(\d*) through (\d*),(\d*)$'
	for i in range(len(str_list)):
		matches = regex.match(reg, str_list[i])
		if (matches):
			groups = matches.groups()
			lights = ManipulateLight(lights, int(groups[1]), int(groups[2]), int(groups[3]), int(groups[4]), groups[0])
	
	return str(CountLightOn(lights))

def level2(input):
	lights = CreateDefaultTuple(0)
	str_list = input.split("\n")
	reg = r'^([a-z]*\s*[a-z]*) (\d*),(\d*) through (\d*),(\d*)$'
	for i in range(len(str_list)):
		matches = regex.match(reg, str_list[i])
		if (matches):
			groups = matches.groups()
			lights = DimingLight(lights, int(groups[1]), int(groups[2]), int(groups[3]), int(groups[4]), groups[0])
	return str(CountIntensity(lights))