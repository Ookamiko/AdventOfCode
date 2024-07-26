#!/usr/bin/python

import re as regex

def get_value_of_monkey(monkeys, monkey_name):
	result = 0

	if monkeys[monkey_name]['value'] != None:
		result = monkeys[monkey_name]['value']
	else:
		source1 = get_value_of_monkey(monkeys, monkeys[monkey_name]['source1'])
		source2 = get_value_of_monkey(monkeys, monkeys[monkey_name]['source2'])

		if monkeys[monkey_name]['operator'] == '+':
			result = source1 + source2
		elif monkeys[monkey_name]['operator'] == '-':
			result = source1 - source2
		elif monkeys[monkey_name]['operator'] == '/':
			result = source1 // source2
		elif monkeys[monkey_name]['operator'] == '*':
			result = source1 * source2

	return result

def init_monkeys(instructions):
	monkeys = {}
	for line in instructions:
		str_split = line.replace(':', '').split(' ')
		if len(str_split) > 2:
			monkeys[str_split[0]] = {'source1': str_split[1], 'source2': str_split[3], 'operator': str_split[2], 'value': None}
		else:
			numbers = regex.findall(r'-?\d+', line)
			monkeys[str_split[0]] = {'value': int(numbers[0])}

	return monkeys

def level1(input):
	#input = 'root: pppw + sjmn\ndbpl: 5\ncczh: sllz + lgvd\nzczc: 2\nptdq: humn - dvpt\ndvpt: 3\nlfqf: 4\nhumn: 5\nljgn: 2\nsjmn: drzm * dbpl\nsllz: 4\npppw: cczh / lfqf\nlgvd: ljgn * ptdq\ndrzm: hmdt - zczc\nhmdt: 32\n'
	monkeys = init_monkeys(input.strip().split('\n'))
	return get_value_of_monkey(monkeys, 'root')

def level2(input):
	#input = 'root: pppw + sjmn\ndbpl: 5\ncczh: sllz + lgvd\nzczc: 2\nptdq: humn - dvpt\ndvpt: 3\nlfqf: 4\nhumn: 5\nljgn: 2\nsjmn: drzm * dbpl\nsllz: 4\npppw: cczh / lfqf\nlgvd: ljgn * ptdq\ndrzm: hmdt - zczc\nhmdt: 32\n'
	monkeys = init_monkeys(input.strip().split('\n'))
	monkeys['root']['operator'] = '-'
	monkeys['humn']['value'] = 0
	value = get_value_of_monkey(monkeys, 'root')
	old_value_positive = value >= 0
	modulator = 10000000000
	while value != 0:
		value_positive = value >= 0
		if value_positive != old_value_positive:
			modulator = modulator // 2
		old_value_positive = value_positive
		print(monkeys['humn']['value'], value)
		monkeys['humn']['value'] += modulator * (-1 if not(value_positive) else 1)
		value = get_value_of_monkey(monkeys, 'root')

	temp_value = monkeys['humn']['value']

	for i in range(temp_value - 1000, temp_value + 1000):
		monkeys['humn']['value'] = i
		if get_value_of_monkey(monkeys, 'root') == 0:
			break

	return monkeys['humn']['value']