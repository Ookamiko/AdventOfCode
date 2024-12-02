#!/usr/bin/python

def level1(input):
	ruban = {}
	state = 'A'
	cursor = 0

	for i in range(12425180):
		index = str(cursor)
		if not(index in ruban.keys()):
			ruban[index] = 0

		if state == 'A':
			if ruban[index] == 0:
				ruban[index] = 1
				cursor += 1
				state = 'B'
			else:
				ruban[index] = 0
				cursor += 1
				state = 'F'

		elif state == 'B':
			if ruban[index] == 0:
				cursor -= 1
				state = 'B'
			else:
				cursor -= 1
				state = 'C'

		elif state == 'C':
			if ruban[index] == 0:
				ruban[index] = 1
				cursor -= 1
				state = 'D'
			else:
				ruban[index] = 0
				cursor += 1
				state = 'C'

		elif state == 'D':
			if ruban[index] == 0:
				ruban[index] = 1
				cursor -= 1
				state = 'E'
			else:
				cursor += 1
				state = 'A'

		elif state == 'E':
			if ruban[index] == 0:
				ruban[index] = 1
				cursor -= 1
				state = 'F'
			else:
				ruban[index] = 0
				cursor -= 1
				state = 'D'

		elif state == 'F':
			if ruban[index] == 0:
				ruban[index] = 1
				cursor += 1
				state = 'A'
			else:
				ruban[index] = 0
				cursor -= 1
				state = 'E'

	return sum(ruban.values())

def level2(input):
	return "Done"