#!/usr/bin/python

def find_bottom_program(lines):
	all_program = {}
	upper_program = []
	lower_program = []

	for line in lines:
		first_separation = line.split(' -> ')

		left_separation = first_separation[0].split(' ')

		program_name = left_separation[0]
		program_weight = int(left_separation[1].replace('(', '').replace(')', ''))

		sup_program = []
		if len(first_separation) == 2:
			sup_program = first_separation[1].split(', ')

		all_program[program_name] = {'weight': program_weight, 'upper_program': sup_program}
		upper_program = upper_program + sup_program
		lower_program.append(program_name)

	to_return = ''
	for program in lower_program:
		if not(program in upper_program):
			to_return = program
			break

	return [to_return, all_program]

def define_sum_program(tower, program):
	value = 0
	for upper_program in tower[program]['upper_program']:
		value = value + define_sum_program(tower, upper_program)

	tower[program]['sum'] = value + tower[program]['weight']

	return tower[program]['sum']

def balance_tower(tower, program):
	upper_program = tower[program]['upper_program']
	test_sum = {}

	for tmp in upper_program:
		tmp_sum = str(tower[tmp]['sum'])
		if not(tmp_sum in test_sum.keys()):
			test_sum[tmp_sum] = []

		test_sum[tmp_sum].append(tmp)

	to_return = -1

	if len(test_sum.keys()) > 1:
		wrong_value = 0
		right_value = 0
		program_wrong = ''
		for tmp_key in test_sum.keys():
			if len(test_sum[tmp_key]) == 1 and wrong_value == 0:
				program_wrong = test_sum[tmp_key][0]
				wrong_value = int(tmp_key)
				to_return = balance_tower(tower, test_sum[tmp_key][0])
			else:
				right_value = int(tmp_key)

		if to_return == -1:
			diff = right_value - wrong_value
			to_return = tower[program_wrong]['weight'] + diff

	return to_return

def level1(input):
	# Test value
	# input = 'pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)\nfwft (72) -> ktlj, cntj, xhth\nqoyq (66)\npadx (45) -> pbga, havc, qoyq\ntknk (41) -> ugml, padx, fwft\njptl (61)\nugml (68) -> gyxo, ebii, jptl\ngyxo (61)\ncntj (57)\n'
	return find_bottom_program(input.strip().split('\n'))[0]

def level2(input):
	# Test value
	# input = 'pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)\nfwft (72) -> ktlj, cntj, xhth\nqoyq (66)\npadx (45) -> pbga, havc, qoyq\ntknk (41) -> ugml, padx, fwft\njptl (61)\nugml (68) -> gyxo, ebii, jptl\ngyxo (61)\ncntj (57)\n'
	tmp = find_bottom_program(input.strip().split('\n'))
	bottom_program = tmp[0]
	tower = tmp[1]
	define_sum_program(tower, bottom_program)
	return balance_tower(tower, bottom_program)