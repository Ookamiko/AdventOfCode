#!/usr/bin/python

def GetGammaAndEpsylonRate(instructions):
	gamma = []
	epsylon = []
	for j in range(len(instructions[0])):
		bits = []
		for i in range(len(instructions)):
			bits.append(instructions[i][j])
		if bits.count('1') >= len(instructions) / 2:
			gamma.append('1')
			epsylon.append('0')
		else:
			gamma.append('0')
			epsylon.append('1')
	return [''.join(gamma), ''.join(epsylon)]

def GetOxygenRating(instructions, indice):
	if len(instructions) == 1:
		return instructions[0]
	else:
		aone = []
		azero = []
		for current in instructions:
			if current[indice] == '1':
				aone.append(current)
			else:
				azero.append(current)
		if len(aone) >= len(azero):
			return GetOxygenRating(aone, indice + 1)
		else:
			return GetOxygenRating(azero, indice + 1)

def GetCO2Rating(instructions, indice):
	if len(instructions) == 1:
		return instructions[0]
	else:
		aone = []
		azero = []
		for current in instructions:
			if current[indice] == '1':
				aone.append(current)
			else:
				azero.append(current)
		if len(aone) >= len(azero):
			return GetCO2Rating(azero, indice + 1)
		else:
			return GetCO2Rating(aone, indice + 1)


def level1(input):
	result = GetGammaAndEpsylonRate(input.strip().split('\n'))
	return int(result[0], 2) * int(result[1], 2)

def level2(input):
	oxygen = GetOxygenRating(input.strip().split('\n'), 0)
	co2 = GetCO2Rating(input.strip().split('\n'), 0)
	return int(oxygen, 2) * int(co2, 2)