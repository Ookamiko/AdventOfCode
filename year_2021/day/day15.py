#!/usr/bin/python

import math, sys

def FindLessRiskyPath(cave, sizeCave, position=0):
	toCheck = []
	cave[position]['pass'] = True

	availablePosition = []
	if position - sizeCave >= 0:
		availablePosition.append(position - sizeCave)
	if position + sizeCave < len(cave):
		availablePosition.append(position + sizeCave)
	if position % sizeCave != 0:
		availablePosition.append(position - 1)
	if position % sizeCave != sizeCave - 1:
		availablePosition.append(position + 1)

	for i in availablePosition:
		if cave[i]['pass']:
			continue

		toCheck.append(i)
		cave[i]['pathRisk'] = min(cave[i]['pathRisk'], cave[i]['weight'] + cave[position]['pathRisk'])


	return toCheck

def CreateRiskMap(instruction):
	baseRisks = [int(value) for value in instruction]
	risk1 = [(value + 1) if value != 9 else 1 for value in list(baseRisks)]
	risk2 = [(value + 1) if value != 9 else 1 for value in list(risk1)]
	risk3 = [(value + 1) if value != 9 else 1 for value in list(risk2)]
	risk4 = [(value + 1) if value != 9 else 1 for value in list(risk3)]
	baseSize = int(math.sqrt(len(baseRisks)))
	topLigne = [0] * len(baseRisks) * 5
	fullSize = baseSize * 5
	for i in range(len(baseRisks)):
		topLigne[(i // baseSize) * fullSize + (i % baseSize)] = baseRisks[i]
		topLigne[(i // baseSize) * fullSize + (i % baseSize) + baseSize] = risk1[i]
		topLigne[(i // baseSize) * fullSize + (i % baseSize) + baseSize * 2] = risk2[i]
		topLigne[(i // baseSize) * fullSize + (i % baseSize) + baseSize * 3] = risk3[i]
		topLigne[(i // baseSize) * fullSize + (i % baseSize) + baseSize * 4] = risk4[i]

	ligne2 = [(value + 1) if value != 9 else 1 for value in topLigne]
	ligne3 = [(value + 1) if value != 9 else 1 for value in ligne2]
	ligne4 = [(value + 1) if value != 9 else 1 for value in ligne3]
	ligne5 = [(value + 1) if value != 9 else 1 for value in ligne4]

	fullRisk = [0] * len(topLigne) * 5

	for i in range(len(topLigne)):
		fullRisk[i] = topLigne[i]
		fullRisk[i + len(topLigne)] = ligne2[i]
		fullRisk[i + len(topLigne) * 2] = ligne3[i]
		fullRisk[i + len(topLigne) * 3] = ligne4[i]
		fullRisk[i + len(topLigne) * 4] = ligne5[i]

	return fullRisk

def level1(input):
	risks = [int(value) for value in input.replace('\n', '')]
	cave = []
	sizeCave = int(math.sqrt(len(risks)))
	for value in risks:
		cave.append({'weight': value, 'pathRisk': sizeCave * 2 * 9, 'pass': False})
	cave[0]['pathRisk'] = 0
	position = 0
	toCheck = []
	while position != len(cave) - 1:
		toCheck = list(dict.fromkeys(toCheck + FindLessRiskyPath(cave, sizeCave, position)))
		minRisk = sys.maxsize
		for i in toCheck:
			if cave[i]['pathRisk'] < minRisk:
				minRisk = cave[i]['pathRisk']
				position = i

		toCheck.remove(position)

	return cave[position]['pathRisk']

def level2(input):
	risks = CreateRiskMap(input.replace('\n', ''))
	cave = []
	sizeCave = int(math.sqrt(len(risks)))
	for value in risks:
		cave.append({'weight': value, 'pathRisk': sizeCave * 2 * 9, 'pass': False})
	cave[0]['pathRisk'] = 0
	position = 0
	toCheck = []
	while position != len(cave) - 1:
		toCheck = list(dict.fromkeys(toCheck + FindLessRiskyPath(cave, sizeCave, position)))
		minRisk = sys.maxsize
		for i in toCheck:
			if cave[i]['pathRisk'] < minRisk:
				minRisk = cave[i]['pathRisk']
				position = i

		toCheck.remove(position)

	return cave[position]['pathRisk']