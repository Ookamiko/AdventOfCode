#!/usr/bin/python

import math

def GetWrongClosing(line):
	openChar = ['(', '{', '<', '[']
	closeChar = [')', '}', '>', ']']
	result = ''
	remember = []
	for char in list(line):
		if char in openChar:
			remember.append(char)
		elif char in closeChar:
			rememberChar = remember.pop(len(remember) - 1)
			if openChar.index(rememberChar) != closeChar.index(char):
				result = char
				break
	return result

def GetUnfinishedLine(line):
	openChar = ['(', '{', '<', '[']
	closeChar = [')', '}', '>', ']']
	result = []
	for char in list(line):
		if char in openChar:
			result.append(char)
		elif char in closeChar:
			rememberChar = result.pop(len(result) - 1)
			if openChar.index(rememberChar) != closeChar.index(char):
				result = []
				break
	return result

def GetScoreUncomplete(chars):
	point = {'(': 1, '{': 3, '<': 4, '[': 2}
	score = 0
	for char in chars:
		score *= 5
		score += point[char]
	return score

def level1(input):
	allWrongClosing = []
	for current in input.strip().split('\n'):
		allWrongClosing.append(GetWrongClosing(current))
	return allWrongClosing.count(')') * 3 + allWrongClosing.count('}') * 1197 + allWrongClosing.count('>') * 25137 + allWrongClosing.count(']') * 57

def level2(input):
	allScore = []
	for current in input.strip().split('\n'):
		tmp = GetUnfinishedLine(current)
		if len(tmp) != 0:
			tmp = tmp[::-1]
			allScore.append(GetScoreUncomplete(tmp))
	allScore.sort()
	return allScore[math.floor(len(allScore) / 2)]