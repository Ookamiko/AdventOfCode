#!/usr/bin/python

def GetAllAvailableAssociation(containers, liter):
	toReturn = []
	for i in range(len(containers)):
		container = containers[i]
		if container > liter:
			break
		elif container == liter:
			toReturn.append([container])
		else:
			sub = containers[i+1:]
			associations = GetAllAvailableAssociation(sub, liter - container)
			for i in range(len(associations)):
				newArray = list(associations[i])
				newArray.append(container)
				toReturn.append(newArray)
	return toReturn


def level1(input):
	container = []
	for current in input.strip().split('\n'):
		container.append(int(current))

	container.sort()
	return len(GetAllAvailableAssociation(container, 150))

def level2(input):
	container = []
	for current in input.strip().split('\n'):
		container.append(int(current))
	container.sort()
	associations = GetAllAvailableAssociation(container, 150)

	count = 0
	minimum = 99999
	for association in associations:
		length = len(association)
		if (length < minimum):
			minimum = length
			count = 1
		elif (length == minimum):
			count += 1

	return count