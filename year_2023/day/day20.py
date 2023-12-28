#!/usr/bin/python

import math

def define_circuit(lines):
	result = {}

	conjunction = []

	for line in lines:
		tmp = line.split(' -> ')

		name = tmp[0]

		if '&' == name[0]:
			result[name[1:]] = {'type': 'cj', 'connexion': {}, 'dest': tmp[1].split(', ')}
			conjunction.append(name[1:])
		elif '%' == name[0]:
			result[name[1:]] = {'type': 'ff', 'value': False, 'dest': tmp[1].split(', ')}
		else:
			result[name] = {'type': 'start', 'dest': tmp[1].split(', ')}

	for conj in conjunction:
		for key, value in result.items():
			if conj in value['dest']:
				result[conj]['connexion'][key] = False

	return result

def press_button(circuit):
	low = 1
	high = 0
	action = [['button', 'broadcaster', False]]

	while len(action) > 0:
		new_action = []

		for current in action:
			sender = current[0]
			receiver = current[1]
			pulse = current[2]

			if not(receiver in circuit.keys()): continue

			elem_type = circuit[receiver]['type']
			next_receiver = []
			pulse_to_send = False
			next_sender = receiver

			if elem_type == 'start':
				next_receiver = circuit[receiver]['dest']
				pulse_to_send = pulse

			elif elem_type == 'cj':
				next_receiver = circuit[receiver]['dest']

				circuit[receiver]['connexion'][sender] = pulse
				pulse_to_send = True

				if not(False in circuit[receiver]['connexion'].values()):
					pulse_to_send = False

			elif elem_type == 'ff' and not(pulse):
				next_receiver = circuit[receiver]['dest']

				circuit[receiver]['value'] = not(circuit[receiver]['value'])
				pulse_to_send = circuit[receiver]['value']


			for dest in next_receiver:
				if pulse_to_send:
					high += 1
				else:
					low += 1

				new_action.append([next_sender, dest, pulse_to_send])

		action = new_action

	return low, high

def press_button_adv(circuit, want_low):
	low = {}
	action = [['button', 'broadcaster', False]]

	for key in want_low.keys():
		low[key] = 0

	while len(action) > 0:
		new_action = []

		for current in action:
			sender = current[0]
			receiver = current[1]
			pulse = current[2]

			if not(receiver in circuit.keys()): continue

			elem_type = circuit[receiver]['type']
			next_receiver = []
			pulse_to_send = False
			next_sender = receiver

			if elem_type == 'start':
				next_receiver = circuit[receiver]['dest']
				pulse_to_send = pulse

			elif elem_type == 'cj':
				next_receiver = circuit[receiver]['dest']

				circuit[receiver]['connexion'][sender] = pulse
				pulse_to_send = True

				if not(False in circuit[receiver]['connexion'].values()):
					pulse_to_send = False

			elif elem_type == 'ff' and not(pulse):
				next_receiver = circuit[receiver]['dest']

				circuit[receiver]['value'] = not(circuit[receiver]['value'])
				pulse_to_send = circuit[receiver]['value']

			if sender in low.keys() and not(pulse):
				low[sender] += 1

			for dest in next_receiver:
				new_action.append([next_sender, dest, pulse_to_send])

		action = new_action

	return low

def get_ppcm(values):
	ppcm = 0
	values.sort()
	test = values[::-1]
	to_reach = test.pop(0)
	to_reach_add = to_reach
	while len(test) > 0:
		to_test = test.pop(0)
		to_test_add = to_test
		while to_test != to_reach:
			if to_test < to_reach:
				diff = to_reach - to_test
				to_test += to_test_add * math.ceil(diff / to_test_add)
			else:
				to_reach += to_reach_add

		to_reach_add = to_reach

	return to_reach

def level1(input):
	# Test value
	# input = 'broadcaster -> a, b, c\n%a -> b\n%b -> c\n%c -> inv\n&inv -> a\n'
	# input = 'broadcaster -> a\n%a -> inv, con\n&inv -> b\n%b -> con\n&con -> output\n'

	circuit = define_circuit(input.strip().split('\n'))

	low = 0
	high = 0

	for i in range(1000):
		tmp_l, tmp_h = press_button(circuit)
		low += tmp_l
		high += tmp_h

	return low * high

def level2(input):
	print('Exec long')
	circuit = define_circuit(input.strip().split('\n'))

	low = 0
	button_pressed = 0
	result = 0

	want_low = {'nh': -1, 'mf': -1, 'fd': -1, 'kb': -1}
	found = 0

	while found < 4:
		button_pressed += 1
		test_result = press_button_adv(circuit, want_low)

		for key, value in test_result.items():
			if value != 0:
				if want_low[key] == -1:
					want_low[key] = button_pressed
					found += 1

	return get_ppcm([x for x in want_low.values()])