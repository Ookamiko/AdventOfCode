#!/usr/bin/python

def CreateInitialState(instructions):
	tmp = [int(number) for number in instructions]
	states = [0] * 9
	for i in range(9):
		states[i] = tmp.count(i)

	return states

def NextState(previous):
	nextState = [0] * 9
	for i in range(9):
		if i == 0:
			nextState[6] = previous[i]
			nextState[8] = previous[i]
		else:
			nextState[i - 1] += previous[i]

	return nextState

def SumAllFish(state):
	result = 0
	for i in range(len(state)):
		result += state[i]
	return result

def level1(input):
	state = CreateInitialState(input.strip().split(','))
	for i in range(1, 81):
		state = NextState(state)
	return SumAllFish(state)

def level2(input):
	state = CreateInitialState(input.strip().split(','))
	for i in range(1, 257):
		state = NextState(state)
	return SumAllFish(state)