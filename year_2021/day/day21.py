#!/usr/bin/python

import re as regex

def GetAllPossibleMove():
	result = [0] * 7
	for i in range(3):
		for j in range(3):
			for k in range(3):
				result[i + j + k] += 1
	return result

def QuantumUniverse(p1pos, p2pos, allRoll, p1Turn=True, p1score=0, p2score=0, multiverseWin=1, level=1):
	wins = {'p1': 0, 'p2': 0}
	for i in range(len(allRoll)):
		tmpP1pos = p1pos
		tmpP1score = p1score
		tmpP2pos = p2pos
		tmpP2score = p2score
		if p1Turn:
			tmpP1pos = 10 if (p1pos + i + 3) % 10 == 0 else ((p1pos + i + 3) % 10)
			tmpP1score += tmpP1pos
			if tmpP1score >= 21:
				wins['p1'] += multiverseWin * allRoll[i]
				continue
		else:
			tmpP2pos = 10 if (p2pos + i + 3) % 10 == 0 else ((p2pos + i + 3) % 10)
			tmpP2score += tmpP2pos
			if tmpP2score >= 21:
				wins['p2'] += multiverseWin * allRoll[i]
				continue

		tmpWins = QuantumUniverse(tmpP1pos, tmpP2pos, allRoll, not(p1Turn), tmpP1score, tmpP2score, multiverseWin * allRoll[i], level + 1)
		wins['p1'] += tmpWins['p1']
		wins['p2'] += tmpWins['p2']

	return wins

def level1(input):
	#input = 'Player 1 starting position: 4\nPlayer 2 starting position: 8'
	numbers = regex.findall(r'\d+', input)
	p1pos = int(numbers[1])
	p1score = 0
	p2pos = int(numbers[3])
	p2score = 0
	nbrRoll = 0
	p1Turn = True

	while max(p1score, p2score) < 1000:
		movement = 0
		nbrRoll += 1
		movement += 100 if nbrRoll % 100 == 0 else (nbrRoll % 100)
		nbrRoll += 1
		movement += 100 if nbrRoll % 100 == 0 else (nbrRoll % 100)
		nbrRoll += 1
		movement += 100 if nbrRoll % 100 == 0 else (nbrRoll % 100)

		if p1Turn:
			p1pos = 10 if (p1pos + movement) % 10 == 0 else ((p1pos + movement) % 10)
			p1score += p1pos
		else:
			p2pos = 10 if (p2pos + movement) % 10 == 0 else ((p2pos + movement) % 10)
			p2score += p2pos

		p1Turn = not(p1Turn)

	print(nbrRoll)
	print(p1score)
	print(p2score)
	return nbrRoll * min(p1score, p2score)

def level2(input):
	#input = 'Player 1 starting position: 4\nPlayer 2 starting position: 8'
	allRoll = GetAllPossibleMove()
	numbers = regex.findall(r'\d+', input)
	p1pos = int(numbers[1])
	p2pos = int(numbers[3])

	wins = QuantumUniverse(p1pos, p2pos, allRoll)
	return max(wins['p1'], wins['p2'])