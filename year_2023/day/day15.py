#!/usr/bin/python

def a1_hash(text):
	result = 0

	for char in text:
		result += ord(char)
		result *= 17
		result = result % 256

	return result

def level1(input):
	# Test value
	# input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
	result = 0

	for cmd in input.strip().split(','):
		result += a1_hash(cmd)

	return result

def level2(input):
	# Test value
	# input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
	boxes = []
	
	for i in range(256):
		boxes.append([])

	for cmd in input.strip().split(','):

		label = ''
		insert = False
		lens_value = 0

		if '=' in cmd:
			tmp = cmd.split('=')
			label = tmp[0]
			insert = True
			lens_value = int(tmp[1])
		else:
			label = cmd[:-1]

		box = a1_hash(label)
		label_present = [x[0] for x in boxes[box]]

		if insert:
			if label in label_present:
				index = label_present.index(label)
				boxes[box][index][1] = lens_value
			else:
				boxes[box].append([label, lens_value])

		else:
			if label in label_present:
				index = label_present.index(label)
				boxes[box].pop(index)

	focusing_power = 0

	for i in range(len(boxes)):
		for j in range(len(boxes[i])):
			focusing_power += (i + 1) * (j + 1) * boxes[i][j][1]

	return focusing_power