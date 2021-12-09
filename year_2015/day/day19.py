#!/usr/bin/python

import re as regex
import sys

def CreateInitialObject(instructions):
	result = {'transmutation': [], 'molecules': []}
	molecule = False
	regTrans = r'(e|[A-Z][a-z]?) => (\S*)'
	for current in instructions:
		if current == '':
			molecule = True
			continue
		if molecule: 
			result['molecules'] = [current]
		else:
			matches = regex.match(regTrans, current)
			if matches:
				groups = matches.groups()
				result['transmutation'].append([groups[0], groups[1]])

	return result

def GetAllTransmutation(trans, molecules, reverse = False):
	result = []
	best_len = sys.maxsize

	for molecule in molecules:
		for current in trans:
			if current[0] == 'e' and len(molecule) != len(current[1]):
				continue

			position = 0
			while True:
				if position >= len(molecule):
					break

				if current[0 if not(reverse) else 1] in molecule[position:]:
					index = molecule.index(current[0 if not(reverse) else 1], position)
					tmp = molecule[:index] + current[1 if not(reverse) else 0] + molecule[index + len(current[0 if not(reverse) else 1]):]
					result.append(tmp)
					position = index + 1
					best_len = min(best_len, len(tmp))
				else:
					break

	return {'result': result, 'best_len': best_len}

alreadyTest = []

def DecomposeMolecule(trans, molecule, iteration):
	result = -1
	if molecule == 'e':
		return iteration

	if iteration % 20 == 0:
		print("iteration :" + str(iteration) + " - molecule :" + molecule + " - alreadyTest :" + str(len(alreadyTest)))

	for current in trans:
		if current[0] == 'e' and len(molecule) != len(current[1]):
			continue

		position = 0
		while result == -1:
			if position >= len(molecule):
				break

			if current[1] in molecule[position:]:
				index = molecule.index(current[1], position)
				tmp = molecule[:index] + current[0] + molecule[index + len(current[1]):]
				position = index + 1
				if not(tmp in alreadyTest):
					result = DecomposeMolecule(trans, tmp, iteration + 1)
					if result == -1 and not(tmp in alreadyTest):
						alreadyTest.append(tmp)
			else:
				break

		if result != -1:
			break

	return result

def level1(input):
	# input = 'H => HO\nH => OH\nO => HH\n\nHOH'
	allInfo = CreateInitialObject(input.strip().split('\n'))
	allTrans = list(GetAllTransmutation(allInfo['transmutation'], allInfo['molecules'])['result'])
	return len(list(dict.fromkeys(allTrans)))

def level2(input):
	# input = 'e => H\ne => O\nH => HO\nH => OH\nO => HH\n\nHOHOHO'
	allInfo = CreateInitialObject(input.strip().split('\n'))
	allInfo['transmutation'].sort(key=lambda x: len(x[1]), reverse=True)
	# allInfo['molecules'] = ['CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFAr']
	iteration = DecomposeMolecule(allInfo['transmutation'], allInfo['molecules'][0], 0)

	return iteration