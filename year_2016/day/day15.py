#!/usr/bin/python

import re as regex

def init_discs(lines):
	discs = []
	for current in lines:
		numbers = regex.findall(r'\d+', current)
		discs.append([int(numbers[3]), int(numbers[1])])

	return discs

def init_ball(discs):
	return [-1] * (len(discs) + 1)

def get_next_state(prev):
	next_state = []
	for disc in prev:
		next_state.append([disc[0] + 1 if (disc[0] + 1) < disc[1] else 0, disc[1]])

	return next_state

def level1(input):
	current_state = init_discs(input.strip().split('\n'))
	ball = init_ball(current_state)
	ball[0] = 0
	time = 0

	while ball[-1] == -1:
		time += 1
		next_state = get_next_state(current_state)

		for i in range(len(ball) - 2, 0, -1):
			if ball[i] != -1 and current_state[i-1][0] == next_state[i][0]:
				ball[i + 1] = ball[i]

			ball[i] = -1

		ball[1] = ball[0]
		ball[0] = time
		current_state = next_state

	return ball[-1]

def level2(input):
	current_state = init_discs(input.strip().split('\n'))
	current_state.append([0, 11])
	ball = init_ball(current_state)
	ball[0] = 0
	time = 0

	while ball[-1] == -1:
		time += 1
		next_state = get_next_state(current_state)

		for i in range(len(ball) - 2, 0, -1):
			if ball[i] != -1 and current_state[i-1][0] == next_state[i][0]:
				ball[i + 1] = ball[i]

			ball[i] = -1

		ball[1] = ball[0]
		ball[0] = time
		current_state = next_state

	return ball[-1]