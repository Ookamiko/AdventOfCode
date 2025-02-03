#!/usr/bin/python

def level1(input):
	#input = '47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47\n'
	lines = input.strip().split('\n')
	i = 0
	rules = {}
	line = lines[i]

	while line != '':
		numbers = [int(x) for x in line.split('|')]

		if not(numbers[0] in rules.keys()):
			rules[numbers[0]] = []

		rules[numbers[0]].append(numbers[1])

		i += 1
		line = lines[i]

	result = 0

	for line in lines[i+1:]:
		pages = [int(x) for x in line.split(',')]

		p = 0
		valid = True

		while valid and p < len(pages):
			page = pages[p]

			for test in pages[:p]:
				if page in rules.keys() and test in rules[page]:
					valid = False
					break

			p += 1

		if valid:
			result += pages[len(pages) // 2]

	return result

def level2(input):
	#input = '47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47\n'
	lines = input.strip().split('\n')
	i = 0
	rules = {}
	line = lines[i]

	while line != '':
		numbers = [int(x) for x in line.split('|')]

		if not(numbers[0] in rules.keys()):
			rules[numbers[0]] = []

		rules[numbers[0]].append(numbers[1])

		i += 1
		line = lines[i]

	to_order = []

	for line in lines[i+1:]:
		pages = [int(x) for x in line.split(',')]

		p = 0
		valid = True

		while valid and p < len(pages):
			page = pages[p]

			for test in pages[:p]:
				if page in rules.keys() and test in rules[page]:
					valid = False
					break

			p += 1

		if not(valid):
			to_order.append(pages)

	result = 0

	for i in range(len(to_order)):
		current = to_order[i]
		valid = False

		while not(valid):
			valid = True

			for i in range(1, len(current)):
				page = current[i]

				if page in rules.keys():
					for j in range(i - 1, -1, -1):
						sub_part = current[j:i]

						for test in sub_part:
							if test in rules[page]:
								valid = False
								new = []
								if j != 0:
									new = current[:j]
								new.append(page)
								new += current[j:i]

								if i < len(current) - 1:
									new += current[i+1:]

								current = new
								break

						if not(valid):
							break

				if not(valid):
					break

		result += current[len(current) // 2]

	return result