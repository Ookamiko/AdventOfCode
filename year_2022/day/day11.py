#!/usr/bin/python

import re as regex

def init_monkeys(instructions):
	monkeys = []

	for i in range(0, len(instructions), 7):
		items = [int(x) for x in regex.findall(r'\d+', instructions[i + 1])]
		tmp_ope = instructions[i + 2].strip().split(' ')
		if tmp_ope[5] == 'old':
			if tmp_ope[4] == '+':
				tmp_ope[4] = '*'
				tmp_ope[5] = '2'
			elif tmp_ope[4] == '*':
				tmp_ope[4] = '^'
				tmp_ope[5] = '2'
		operation = {'op': tmp_ope[4], 'value': int(tmp_ope[5])}
		test = int(regex.findall(r'\d+', instructions[i + 3])[0])
		monkey_true = int(regex.findall(r'\d+', instructions[i + 4])[0])
		monkey_false = int(regex.findall(r'\d+', instructions[i + 5])[0])

		monkeys.append({'items': items, 'operation': operation, 'test': test, 'true': monkey_true, 'false': monkey_false, 'inspect': 0})

	return monkeys

def calc_monkey_business(monkeys):
	inspection = []
	for monkey in monkeys:
		inspection.append(monkey['inspect'])

	inspection.sort(reverse=True)

	return inspection[0] * inspection[1]

def level1(input):
	#input = 'Monkey 0:\nStarting items: 79, 98\nOperation: new = old * 19\nTest: divisible by 23\nIf true: throw to monkey 2\nIf false: throw to monkey 3\n\nMonkey 1:\nStarting items: 54, 65, 75, 74\nOperation: new = old + 6\nTest: divisible by 19\nIf true: throw to monkey 2\nIf false: throw to monkey 0\n\nMonkey 2:\nStarting items: 79, 60, 97\nOperation: new = old * old\nTest: divisible by 13\nIf true: throw to monkey 1\nIf false: throw to monkey 3\n\nMonkey 3:\nStarting items: 74\nOperation: new = old + 3\nTest: divisible by 17\nIf true: throw to monkey 0\nIf false: throw to monkey 1\n'
	monkeys = init_monkeys(input.strip().split('\n'))

	for cround in range(20):
		for monkey in monkeys:
			monkey['inspect'] += len(monkey['items'])
			while len(monkey['items']) > 0:
				# Change worry value and throw
				item = monkey['items'].pop(0)

				if monkey['operation']['op'] == '+':
					item = (item + monkey['operation']['value']) // 3
				elif monkey['operation']['op'] == '*':
					item = (item * monkey['operation']['value']) // 3
				elif monkey['operation']['op'] == '^':
					item = (item ** monkey['operation']['value']) // 3
				elif monkey['operation']['op'] == '-':
					item = (item - monkey['operation']['value']) // 3
				elif monkey['operation']['op'] == '/':
					item = (item / monkey['operation']['value']) // 3

				if item % monkey['test'] == 0:
					monkeys[monkey['true']]['items'].append(item)
				else:
					monkeys[monkey['false']]['items'].append(item)

	return calc_monkey_business(monkeys)

def level2(input):
	#input = 'Monkey 0:\nStarting items: 79, 98\nOperation: new = old * 19\nTest: divisible by 23\nIf true: throw to monkey 2\nIf false: throw to monkey 3\n\nMonkey 1:\nStarting items: 54, 65, 75, 74\nOperation: new = old + 6\nTest: divisible by 19\nIf true: throw to monkey 2\nIf false: throw to monkey 0\n\nMonkey 2:\nStarting items: 79, 60, 97\nOperation: new = old * old\nTest: divisible by 13\nIf true: throw to monkey 1\nIf false: throw to monkey 3\n\nMonkey 3:\nStarting items: 74\nOperation: new = old + 3\nTest: divisible by 17\nIf true: throw to monkey 0\nIf false: throw to monkey 1\n'
	monkeys = init_monkeys(input.strip().split('\n'))
	manage_worries = 1
	for monkey in monkeys:
		manage_worries *= monkey['test']


	for cround in range(10000):
		for monkey in monkeys:
			monkey['inspect'] += len(monkey['items'])
			while len(monkey['items']) > 0:
				# Change worry value and throw
				item = monkey['items'].pop(0)

				if monkey['operation']['op'] == '+':
					item = (item + monkey['operation']['value']) % manage_worries
				elif monkey['operation']['op'] == '*':
					item = (item * monkey['operation']['value']) % manage_worries
				elif monkey['operation']['op'] == '^':
					item = (item ** monkey['operation']['value']) % manage_worries
				elif monkey['operation']['op'] == '-':
					item = (item - monkey['operation']['value']) % manage_worries
				elif monkey['operation']['op'] == '/':
					item = (item / monkey['operation']['value']) % manage_worries

				if item % monkey['test'] == 0:
					monkeys[monkey['true']]['items'].append(item)
				else:
					monkeys[monkey['false']]['items'].append(item)

	return calc_monkey_business(monkeys)