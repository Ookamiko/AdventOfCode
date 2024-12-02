#!/usr/bin/python

import re as regex
import sys

MISSILE_COST = 53
MISSILE_DMG = 4
DRAIN_COST = 73
DRAIN_DMG = 2
SHIELD_COST = 113
SHIELD_BONUS = 7
SHIELD_TIME = 6
POISON_COST = 173
POISON_DMG = 3
POISON_TIME = 6
RECHARGE_COST = 229
RECHARGE_GAIN = 101
RECHERGE_TIME = 5

def WinWithLessMana(bossHP, bossAtk, playerHP, playerMP, timePoison=0, timeShield=0, timeRegain=0, usedMP=0, lessMana=sys.maxsize, level=0):
	# Pre check
	if usedMP >= lessMana:
		return lessMana

	# Pre Player
	playerMP += RECHARGE_GAIN if timeRegain > 0 else 0
	timeRegain -= 1
	bossHP -= POISON_DMG if timePoison > 0 else 0
	timePoison -= 1
	timeShield -= 1

	if bossHP <= 0:
		return min(lessMana, usedMP)

	# Player Turn
	if playerMP >= MISSILE_COST:
		tmpUsedMP = usedMP + MISSILE_COST
		tmpPMP = playerMP - MISSILE_COST
		tmpBHP = bossHP - MISSILE_DMG
		tmpPHP = playerHP

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessMana(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))

	if playerMP >= DRAIN_COST:
		tmpUsedMP = usedMP + DRAIN_COST
		tmpPMP = playerMP - DRAIN_COST
		tmpBHP = bossHP - DRAIN_DMG
		tmpPHP = playerHP + DRAIN_DMG

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessMana(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= SHIELD_COST and timeShield <= 0:
		tmpUsedMP = usedMP + SHIELD_COST
		tmpPMP = playerMP - SHIELD_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = SHIELD_TIME - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessMana(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= POISON_COST and timePoison <= 0:
		tmpUsedMP = usedMP + POISON_COST
		tmpPMP = playerMP - POISON_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG
		tmpTPoison = POISON_TIME - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessMana(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= RECHARGE_COST and timeRegain <= 0:
		tmpUsedMP = usedMP + RECHARGE_COST
		tmpPMP = playerMP - RECHARGE_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN
		tmpTRegain = RECHERGE_TIME - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessMana(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))

	return lessMana

def WinWithLessManaHardMode(bossHP, bossAtk, playerHP, playerMP, timePoison=0, timeShield=0, timeRegain=0, usedMP=0, lessMana=sys.maxsize, level=0):
	# Pre check
	if usedMP >= lessMana:
		return lessMana

	# Hard Mode
	playerHP -= 1

	if playerHP <= 0:
		return sys.maxsize

	# Pre Player
	playerMP += RECHARGE_GAIN if timeRegain > 0 else 0
	timeRegain -= 1
	bossHP -= POISON_DMG if timePoison > 0 else 0
	timePoison -= 1
	timeShield -= 1

	if bossHP <= 0:
		return min(lessMana, usedMP)

	# Player Turn
	if playerMP >= MISSILE_COST:
		tmpUsedMP = usedMP + MISSILE_COST
		tmpPMP = playerMP - MISSILE_COST
		tmpBHP = bossHP - MISSILE_DMG
		tmpPHP = playerHP

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessManaHardMode(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))

	if playerMP >= DRAIN_COST:
		tmpUsedMP = usedMP + DRAIN_COST
		tmpPMP = playerMP - DRAIN_COST
		tmpBHP = bossHP - DRAIN_DMG
		tmpPHP = playerHP + DRAIN_DMG

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessManaHardMode(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= SHIELD_COST and timeShield <= 0:
		tmpUsedMP = usedMP + SHIELD_COST
		tmpPMP = playerMP - SHIELD_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = SHIELD_TIME - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessManaHardMode(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= POISON_COST and timePoison <= 0:
		tmpUsedMP = usedMP + POISON_COST
		tmpPMP = playerMP - POISON_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG
		tmpTPoison = POISON_TIME - 1
		tmpPMP += RECHARGE_GAIN if timeRegain > 0 else 0
		tmpTRegain = timeRegain - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessManaHardMode(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))
		
	if playerMP >= RECHARGE_COST and timeRegain <= 0:
		tmpUsedMP = usedMP + RECHARGE_COST
		tmpPMP = playerMP - RECHARGE_COST
		tmpBHP = bossHP
		tmpPHP = playerHP

		# Pre boss
		tmpBHP -= POISON_DMG if timePoison > 0 else 0
		tmpTPoison = timePoison - 1
		tmpPMP += RECHARGE_GAIN
		tmpTRegain = RECHERGE_TIME - 1
		tmpTShield = timeShield - 1

		if tmpBHP <= 0:
			return min(lessMana, tmpUsedMP)

		# Boss Turn
		tmpPHP -= bossAtk - (SHIELD_BONUS if tmpTShield > 0 else 0)

		if tmpPHP > 0:
			lessMana = min(lessMana, WinWithLessManaHardMode(tmpBHP, bossAtk, tmpPHP, tmpPMP, max(0, tmpTPoison), max(0, tmpTShield), max(0, tmpTRegain), tmpUsedMP, lessMana, level + 1))

	return lessMana


def level1(input):
	reg = r'\d+'
	number = regex.findall(reg, input)
	bossHP = int(number[0])
	bossAtk = int(number[1])
	playerHP = 50
	playerMP = 500
	return WinWithLessMana(bossHP, bossAtk, playerHP, playerMP)

def level2(input):
	reg = r'\d+'
	number = regex.findall(reg, input)
	bossHP = int(number[0])
	bossAtk = int(number[1])
	playerHP = 50
	playerMP = 500
	return WinWithLessManaHardMode(bossHP, bossAtk, playerHP, playerMP)