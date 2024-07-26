#!/usr/bin/python

import re as regex
import sys, math

weapon = [[8,4],[10,5],[25,6],[40,7],[74,8]]
armor = [[0,0],[13,1],[31,2],[53,3],[75,4],[102,5]]
rings = [[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]
playerHP = 100

def PlayerWin(boss, player):
	turnForBoss = math.ceil(player[0] / max(1, boss[1] - player[2]))
	turnForPlayer = math.ceil(boss[0] / max(1, player[1] - boss[2]))
	return turnForPlayer <= turnForBoss

def level1(input):
	instructions = input.strip().split('\n')
	boss = []
	reg = r'\d+'
	for current in instructions:
		number = regex.findall(reg, current)
		if len(number) == 1:
			boss.append(int(number[0]))

	minCost = sys.maxsize
	for costAtk, wAtk in weapon:
		for costDef, aDef in armor:
			for costRg1, rg1Atk, rg1Def in rings:
				for costRg2, rg2Atk, rg2Def in rings:
					if costRg1 == costRg2 and costRg1 != 0:
						continue
					tmp = [playerHP, wAtk + rg1Atk + rg2Atk, aDef + rg1Def + rg2Def]
					if PlayerWin(boss, tmp):
						minCost = min(minCost, costAtk + costDef + costRg1 + costRg2)

	return minCost

def level2(input):
	instructions = input.strip().split('\n')
	boss = []
	reg = r'\d+'
	for current in instructions:
		number = regex.findall(reg, current)
		if len(number) == 1:
			boss.append(int(number[0]))

	maxCost = 0
	for costAtk, wAtk in weapon:
		for costDef, aDef in armor:
			for costRg1, rg1Atk, rg1Def in rings:
				for costRg2, rg2Atk, rg2Def in rings:
					if costRg1 == costRg2 and costRg1 != 0:
						continue
					tmp = [playerHP, wAtk + rg1Atk + rg2Atk, aDef + rg1Def + rg2Def]
					if not(PlayerWin(boss, tmp)):
						maxCost = max(maxCost, costAtk + costDef + costRg1 + costRg2)

	return maxCost