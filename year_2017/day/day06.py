#!/usr/bin/python

import re as regex

def convert_state(state):
	result = 0
	for i in range(len(state)):
		result += state[i] * (i ** len(state))

	return result

def perform_org(memory_banks):
	index = 0
	value = -1

	for i in range(len(memory_banks)):
		if value < memory_banks[i]:
			value = memory_banks[i]
			index = i

	count = memory_banks[index]
	memory_banks[index] = 0

	for i in range(count):
		index = (index + 1) % len(memory_banks)
		memory_banks[index] += 1

	return memory_banks

def level1(input):
	memory_banks = [int(x) for x in regex.findall(r'\d+', input)]
	seen = []
	step = 0

	state = convert_state(memory_banks)

	while not(state in seen):
		step += 1
		seen.append(state)
		memory_banks = perform_org(memory_banks)
		state = convert_state(memory_banks)

	return step

def level2(input):
	memory_banks = [int(x) for x in regex.findall(r'\d+', input)]
	seen = []
	step = 0

	state = convert_state(memory_banks)

	while not(state in seen):
		step += 1
		seen.append(state)
		memory_banks = perform_org(memory_banks)
		state = convert_state(memory_banks)

	index_seen = seen.index(state)

	return step - index_seen