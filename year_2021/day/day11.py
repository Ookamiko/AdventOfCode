#!/usr/bin/python

def CreateCaveLayout(instructions):
	result = []
	for current in instructions:
		result += [int(value) for value in current]
	return result

def NextStep(layout, sizeSquare):
	# Increase
	layout = [value + 1 for value in layout]

	# Simulate flash
	i = 0
	while i < len(layout):
		if layout[i] >= 10:
			layout[i] = 0
			position = []
			# Top Line
			if i - sizeSquare >= 0:
				if i % sizeSquare != 0:
					position.append(i - sizeSquare - 1)
				if i % sizeSquare != sizeSquare - 1:
					position.append(i - sizeSquare + 1)
				position.append(i - sizeSquare)
			# Bottom Line
			if i + sizeSquare < len(layout):
				if i % sizeSquare != 0:
					position.append(i + sizeSquare - 1)
				if i % sizeSquare != sizeSquare - 1:
					position.append(i + sizeSquare + 1)
				position.append(i + sizeSquare)
			# Middle Line
			if i % sizeSquare != 0:
				position.append(i - 1)
			if i % sizeSquare != sizeSquare - 1:
				position.append(i + 1)

			position.sort()
			toReturn = False
			for x in position:
				if layout[x] != 0:
					layout[x] += 1
					if layout[x] >= 10:
						toReturn = True

			if toReturn:
				i = position[0] - 1
		i += 1
	return layout

def DisplayArray(layout):
	for i in range(10):
		print('|'.join([str(value) for value in layout[i * 10:i * 10 +10]]))

def level1(input):
	layout = CreateCaveLayout(input.strip().split('\n'))
	nbrFlash = 0
	for i in range(100):
		layout = NextStep(layout, len(input.strip().split('\n')))
		nbrFlash += layout.count(0)
	return nbrFlash

def level2(input):
	layout = CreateCaveLayout(input.strip().split('\n'))
	nbrFlash = 0
	i = 0
	while layout.count(0) != len(layout):
		layout = NextStep(layout, len(input.strip().split('\n')))
		i += 1
	return i