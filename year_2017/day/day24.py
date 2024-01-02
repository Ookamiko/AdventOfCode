#!/usr/bin/python

def bridge_to_str(start, end):
	if int(start) <= int(end):
		return start + '/' + end
	else:
		return end + '/' + start

def find_all_combi(bridges, pins='0', taken=[]):
	result = []
	available_next = []

	for test in bridges[pins]:
		tmp = bridge_to_str(test, pins)
		if not(tmp in taken):
			available_next.append(test)

	for next_pins in available_next:
		str_bridge = bridge_to_str(next_pins, pins)

		tmp = find_all_combi(bridges, next_pins, taken + [str_bridge])

		if len(tmp) != 0:
			for one in tmp:
				result.append([str_bridge] + one)
		else:
			result.append([str_bridge])

	return result

def get_strongest_path(paths):
	result = 0

	for path in paths:
		tmp = 0
		for bridge in path:
			nbrs = [int(x) for x in bridge.split('/')]
			tmp += nbrs[0] + nbrs[1]

		result = max(tmp, result)

	return result

def get_longest_strongest_path(paths):
	result = 0
	biggest_bridge = max([len(x) for x in paths])

	for path in paths:
		if len(path) < biggest_bridge:
			continue

		tmp = 0
		for bridge in path:
			nbrs = [int(x) for x in bridge.split('/')]
			tmp += nbrs[0] + nbrs[1]

		result = max(tmp, result)

	return result

def level1(input):
	# Test value
	# input = '0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10\n'

	bridges = {}
	for bridge in input.strip().split('\n'):
		nbrs = bridge.split('/')

		if not(nbrs[0] in bridges.keys()):
			bridges[nbrs[0]] = []

		bridges[nbrs[0]].append(nbrs[1])

		if nbrs[0] != nbrs[1]:

			if not(nbrs[1] in bridges.keys()):
				bridges[nbrs[1]] = []

			bridges[nbrs[1]].append(nbrs[0])

	paths = find_all_combi(bridges)

	return get_strongest_path(paths)

def level2(input):
	# Test value
	# input = '0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10\n'

	bridges = {}
	for bridge in input.strip().split('\n'):
		nbrs = bridge.split('/')

		if not(nbrs[0] in bridges.keys()):
			bridges[nbrs[0]] = []

		bridges[nbrs[0]].append(nbrs[1])

		if nbrs[0] != nbrs[1]:

			if not(nbrs[1] in bridges.keys()):
				bridges[nbrs[1]] = []

			bridges[nbrs[1]].append(nbrs[0])

	paths = find_all_combi(bridges)

	return get_longest_strongest_path(paths)