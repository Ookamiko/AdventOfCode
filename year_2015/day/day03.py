#!/usr/bin/python

def level1(input):
	inst = list(input)
	x = 0
	y = 0
	position = [(x,y)]

	for current in inst:
		if current == '<':
			x -= 1
		elif current == '>':
			x += 1
		elif current == '^':
			y -= 1
		elif current == 'v':
			y += 1

		position.append((x,y))

	return str(len(list(dict.fromkeys(position))))

def level2(input):
	inst = list(input)
	x_s = x_r = 0
	y_s = y_r = 0
	position = [(x_s,y_s)]
	robot_turn = False

	for current in inst:
		if current == '<':
			if robot_turn:
				x_r -= 1
			else:
				x_s -=1
			robot_turn = not(robot_turn)

		elif current == '>':
			if robot_turn:
				x_r += 1
			else:
				x_s +=1
			robot_turn = not(robot_turn)

		elif current == '^':
			if robot_turn:
				y_r -= 1
			else:
				y_s -=1
			robot_turn = not(robot_turn)

		elif current == 'v':
			if robot_turn:
				y_r += 1
			else:
				y_s +=1
			robot_turn = not(robot_turn)

		position.append((x_s,y_s) if robot_turn else (x_r, y_r))

	return str(len(list(dict.fromkeys(position))))