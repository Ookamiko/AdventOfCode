#!/usr/bin/python

def CreateMap(instructions):
	maps = []
	for current in instructions:
		maps += [int(value) for value in list(current)]

	return maps

def GetLowPoint(maps, sizeVer, sizeHor):
	lowPoints = []
	
	for x in range(len(maps)):

		if x - sizeHor >= 0 and maps[x - sizeHor] <= maps[x]:
			continue
		elif x + sizeHor < len(maps) and maps[x + sizeHor] <= maps[x]:
			continue
		elif x % sizeHor != 0 and maps[x -1] <= maps[x]:
			continue
		elif x % sizeHor != sizeHor - 1 and maps[x + 1] <= maps[x]:
			continue

		lowPoints.append(x)

	return lowPoints

def GetSizeBassin(indice, maps, sizeVer, sizeHor, alreadyCheck):
	
	alreadyCheck.append(indice)

	if indice - sizeHor >= 0 and not(indice - sizeHor in alreadyCheck) and maps[indice - sizeHor] != 9:
		GetSizeBassin(indice - sizeHor, maps, sizeVer, sizeHor, alreadyCheck)

	if indice + sizeHor < len(maps) and not(indice + sizeHor in alreadyCheck) and maps[indice + sizeHor] != 9:
		GetSizeBassin(indice + sizeHor, maps, sizeVer, sizeHor, alreadyCheck)

	if indice % sizeHor != 0 and not(indice - 1 in alreadyCheck) and maps[indice - 1] != 9:
		GetSizeBassin(indice - 1, maps, sizeVer, sizeHor, alreadyCheck)

	if indice % sizeHor != sizeHor - 1 and not(indice + 1 in alreadyCheck) and maps[indice + 1] != 9:
		GetSizeBassin(indice + 1, maps, sizeVer, sizeHor, alreadyCheck)

	return len(alreadyCheck)

def level1(input):
	tmp = input.strip().split('\n')
	sizeVer = len(tmp)
	sizeHor = len(tmp[0])
	maps = CreateMap(tmp)
	lowPoints = GetLowPoint(maps, sizeVer, sizeHor)
	return sum([maps[x] for x in lowPoints], len(lowPoints))

def level2(input):
	tmp = input.strip().split('\n')
	sizeVer = len(tmp)
	sizeHor = len(tmp[0])
	maps = CreateMap(tmp)
	lowPoints = GetLowPoint(maps, sizeVer, sizeHor)

	bassins = []
	for current in lowPoints:
		bassins.append(GetSizeBassin(current, maps, sizeVer, sizeHor, []))

	bassins.sort(reverse=True)

	print(bassins)

	return bassins[0] * bassins[1] * bassins[2]