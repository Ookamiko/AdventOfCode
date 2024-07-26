#!/usr/bin/python
import json
import re as regex

def CalculateSum(obj):
	number = r'(-?\d+)'

	matches = regex.findall(number, obj)

	toReturn = 0
	for element in matches:
		toReturn += int(element)

	return toReturn

def level1(input):
	return str(CalculateSum(input.strip()))

def CalculateSumJson(obj):
	addition = 0

	if obj.__class__ == addition.__class__:
		addition += obj
	elif obj.__class__ == [].__class__:
		for i in range(len(obj)):
			addition += CalculateSumJson(obj[i])
	elif obj.__class__ == {}.__class__:
		dontPerform = False
		for key in obj.keys():
			if obj[key] == 'red':
				dontPerform = True
		if not(dontPerform):
			for key in obj.keys():
				addition += CalculateSumJson(obj[key])

	return addition


def level2(input):
	return str(CalculateSumJson(json.loads(input.strip())))