#!/usr/bin/python

import re as regex

def init_base(instructions):
	size_bots = (len(instructions) - ' '.join(instructions).count('value'))
	bots = [] * size_bots

	for i in range(size_bots):
		bots.append({'hand': []})

	outputs = [-1] * size_bots
	inputs = []

	for line in instructions:

		if 'value' in line:
			numbers = regex.findall(r'\d+', line)
			inputs.append({'bot': int(numbers[1]), 'value': int(numbers[0])})
		else:
			break_line = line.split(' ')
			bot = int(break_line[1])
			bots[bot]['low'] = int(break_line[6]) + (size_bots if break_line[5] == 'output' else 0)
			bots[bot]['high'] = int(break_line[11]) + (size_bots if break_line[10] == 'output' else 0)

	return {'bots': bots, 'in': inputs, 'out': outputs}

def level1(input):
	#input = 'value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2\n'
	instructions = input.strip().split('\n')
	initial = init_base(instructions)
	bots = initial['bots']
	inputs = initial['in']
	outputs = initial['out']

	perform_inst = []
	size_bots = len(bots)

	for line in inputs:
		bots[line['bot']]['hand'].append(line['value'])

		if len(bots[line['bot']]['hand']) > 1:
			perform_inst.append(line['bot'])

	result = -1

	while len(perform_inst) > 0:
		id_bot = perform_inst.pop()

		min_val = min(bots[id_bot]['hand'])
		max_val = max(bots[id_bot]['hand'])

		if min_val == 17 and max_val == 61:
			result = id_bot
			break

		if bots[id_bot]['low'] >= size_bots:
			outputs[bots[id_bot]['low'] - size_bots] = min_val
		else:
			bots[bots[id_bot]['low']]['hand'].append(min_val)
			if len(bots[bots[id_bot]['low']]['hand']) > 1:
				perform_inst.append(bots[id_bot]['low'])

		if bots[id_bot]['high'] >= size_bots:
			outputs[bots[id_bot]['high'] - size_bots] = max_val
		else:
			bots[bots[id_bot]['high']]['hand'].append(max_val)
			if len(bots[bots[id_bot]['high']]['hand']) > 1:
				perform_inst.append(bots[id_bot]['high'])

	return result

def level2(input):
	#input = 'value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2\n'
	instructions = input.strip().split('\n')
	initial = init_base(instructions)
	bots = initial['bots']
	inputs = initial['in']
	outputs = initial['out']

	perform_inst = []
	size_bots = len(bots)

	for line in inputs:
		bots[line['bot']]['hand'].append(line['value'])

		if len(bots[line['bot']]['hand']) > 1:
			perform_inst.append(line['bot'])

	while len(perform_inst) > 0:
		id_bot = perform_inst.pop()

		min_val = min(bots[id_bot]['hand'])
		max_val = max(bots[id_bot]['hand'])

		if bots[id_bot]['low'] >= size_bots:
			outputs[bots[id_bot]['low'] - size_bots] = min_val
		else:
			bots[bots[id_bot]['low']]['hand'].append(min_val)
			if len(bots[bots[id_bot]['low']]['hand']) > 1:
				perform_inst.append(bots[id_bot]['low'])

		if bots[id_bot]['high'] >= size_bots:
			outputs[bots[id_bot]['high'] - size_bots] = max_val
		else:
			bots[bots[id_bot]['high']]['hand'].append(max_val)
			if len(bots[bots[id_bot]['high']]['hand']) > 1:
				perform_inst.append(bots[id_bot]['high'])

	return outputs[0] * outputs[1] * outputs[2]