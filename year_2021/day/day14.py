#!/usr/bin/python

import re as regex
import sys

def CreateRuleObject(instructions):
	rules = {}
	reg = r'([A-Z]{2}) -> ([A-Z])'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			rules[matches.groups()[0]] = matches.groups()[1]

	return rules

def NextStep(polymer, rules):
	result = ''
	for i in range(len(polymer) - 1):
		if polymer[i:i+2] in rules.keys():
			result += polymer[i] + rules[polymer[i:i+2]]
		else:
			result += polymer[i]

	return result + polymer[len(polymer) - 1]

def CountLetter(part, rules, level, maxLevel, store):
	newLetter = rules[part]
	count = {newLetter: 0}

	if (part + str(level)) in store:
		count = store[part + str(level)]
	else:
		if level < maxLevel:
			left = CountLetter(part[0] + newLetter, rules, level + 1, maxLevel, store)
			right = CountLetter(newLetter + part[1], rules, level + 1, maxLevel, store)
			count[newLetter] += 1

			for key in left.keys():
				if not(key in count.keys()):
					count[key] = 0
				count[key] += left[key]

			for key in right.keys():
				if not(key in count.keys()):
					count[key] = 0
				count[key] += right[key]
		else:
			count[newLetter] += 1
		store[part + str(level)] = count

	return count

def level1(input):
	polymer = input.strip().split('\n')[0]
	rules = CreateRuleObject(input.strip().split('\n')[2:])
	allKeys = {polymer[len(polymer)-1:]: 1}
	store = {}
	
	for i in range(len(polymer) - 1):
		if not(polymer[i] in allKeys.keys()):
			allKeys[polymer[i]] = 0
		allKeys[polymer[i]] += 1
		tmpCount = CountLetter(polymer[i:i+2], rules, 1, 10, store)
		for key in tmpCount.keys():
			if not(key in allKeys.keys()):
				allKeys[key] = 0
			allKeys[key] += tmpCount[key]

	maxOccurence = 0
	minOccurence = sys.maxsize
	for keys in allKeys:
		maxOccurence = max(maxOccurence, allKeys[keys])
		minOccurence = min(minOccurence, allKeys[keys])

	return maxOccurence - minOccurence

def level2(input):
	polymer = input.strip().split('\n')[0]
	rules = CreateRuleObject(input.strip().split('\n')[2:])
	allKeys = {polymer[len(polymer)-1:]: 1}
	store = {}
	
	for i in range(len(polymer) - 1):
		if not(polymer[i] in allKeys.keys()):
			allKeys[polymer[i]] = 0
		allKeys[polymer[i]] += 1
		tmpCount = CountLetter(polymer[i:i+2], rules, 1, 40, store)
		for key in tmpCount.keys():
			if not(key in allKeys.keys()):
				allKeys[key] = 0
			allKeys[key] += tmpCount[key]

	maxOccurence = 0
	minOccurence = sys.maxsize
	for keys in allKeys:
		maxOccurence = max(maxOccurence, allKeys[keys])
		minOccurence = min(minOccurence, allKeys[keys])

	return maxOccurence - minOccurence