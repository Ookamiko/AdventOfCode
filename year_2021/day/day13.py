#!/usr/bin/python

import re as regex

def CreateInitialObject(lines):
	regStar = r'(\d+),(\d+)'
	regInstr = r'fold along (x|y)=(\d+)'
	maxHor = 0
	maxVer = 0
	place = []
	fold = []
	for line in lines:
		if line == '':
			continue

		matches = regex.match(regStar, line)
		if matches:
			place.append([ int(value) for value in matches.groups()])
			maxHor = max(maxHor, int(matches.groups()[0]))
			maxVer = max(maxVer, int(matches.groups()[1]))

		matches = regex.match(regInstr, line)
		if matches:
			fold.append([matches.groups()[0], int(matches.groups()[1])])

	maxHor += 1
	maxVer += 1

	paper = ['.'] * (maxVer * maxHor)
	for x, y in place:
		paper[y * maxHor + x] = '#'

	return {'paper': paper, 'maxVer': maxVer, 'maxHor': maxHor, 'folds': fold}

def MergePaper(paper1, paper2, maxHor, maxVer, foldHor):
	for i in range(len(paper1)):
		if paper1[i] == '.':
			j = 0
			if foldHor:
				j = (maxVer - 1 - (i // maxHor)) * maxHor + i % maxHor
			else:
				j = (i // maxHor) * maxHor + maxHor - 1 - i % maxHor
			if j < len(paper2):
				paper1[i] = paper2[j]
	return paper1

def FoldPaper(paper, fold, maxHor, maxVer):
	paper1 = []
	paper2 = []
	foldHor = False

	if fold[0] == 'x':
		for i in range(len(paper)):
			if i % maxHor < fold[1] % maxHor:
				paper1.append(paper[i])
			elif i % maxHor > fold[1] % maxHor:
				paper2.append(paper[i])
		maxHor = fold[1]

	elif fold[0] == 'y':
		foldHor = True
		maxVer = fold[1]
		paper1 = paper[:fold[1] * maxHor]
		paper2 = paper[(fold[1] + 1) * maxHor:]

	return {'paper': MergePaper(paper1, paper2, maxHor, maxVer, foldHor), 'maxHor': maxHor, 'maxVer': maxVer}

def DisplayArray(array, hor, ver):
	for i in range(ver):
		print(''.join(array[i * hor:(i * hor) + hor]))

def level1(input):
	initial = CreateInitialObject(input.strip().split('\n'))
	paper = initial['paper']
	maxHor = initial['maxHor']
	maxVer = initial['maxVer']
	folds = initial['folds']
	tmp = FoldPaper(paper, folds[0], maxHor, maxVer)
	return tmp['paper'].count('#')

def level2(input):
	initial = CreateInitialObject(input.strip().split('\n'))
	paper = initial['paper']
	maxHor = initial['maxHor']
	maxVer = initial['maxVer']
	folds = initial['folds']
	for fold in folds:
		tmp = FoldPaper(paper, fold, maxHor, maxVer)
		paper = tmp['paper']
		maxHor = tmp['maxHor']
		maxVer = tmp['maxVer']

	DisplayArray(paper, maxHor, maxVer)
	return ''