#!/usr/bin/python

import re as regex

def level1(input):
	# Test value
	# input = 'px{a<2006:qkq,m>2090:A,rfg}\npv{a>1716:R,A}\nlnx{m>1548:A,A}\nrfg{s<537:gd,x>2440:R,A}\nqs{s>3448:A,lnx}\nqkq{x<1416:A,crn}\ncrn{x>2662:A,R}\nin{s<1351:px,qqz}\nqqz{s>2770:qs,m<1801:hdj,R}\ngd{a>3333:R,R}\nhdj{m>838:A,pv}\n\n{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}\n{x=2036,m=264,a=79,s=2244}\n{x=2461,m=1339,a=466,s=291}\n{x=2127,m=1623,a=2188,s=1013}\n'
	workflow = {}
	i = 0
	lines = input.strip().split('\n')
	while lines[i] != '':
		line = lines[i]
		tmp = line.split('{')
		name = tmp[0]
		workflow[name] = []
		for test in tmp[1][:-1].split(','):
			if ':' in test:
				re_str = r'([xmas])([<>])(\d+):([ARa-z]+)'

				match = regex.search(re_str, test)
				if match:
					groups = match.groups()

					workflow[name].append({'cat': groups[0], 'operator': groups[1], 'value': int(groups[2]), 'go_to': groups[3]})
			else:
				workflow[name].append({'cat': 'x', 'operator': '>', 'value': -1, 'go_to': test})

		i += 1

	i += 1
	result = 0
	while i < len(lines):
		nbrs = [int(x) for x in regex.findall(r'\d+', lines[i])]
		part = {'x': nbrs[0], 'm': nbrs[1], 'a': nbrs[2], 's': nbrs[3]}
		current = 'in'

		while current != 'A' and current != 'R':
			for rule in workflow[current]:
				finish = False
				if rule['operator'] == '>' and part[rule['cat']] > rule['value']:
					current = rule['go_to']
					finish = True
				elif rule['operator'] == '<' and part[rule['cat']] < rule['value']:
					current = rule['go_to']
					finish = True

				if finish:
					break

		if current == 'A':
			result += part['x'] + part['m'] + part['a'] + part['s']

		i += 1

	return result

def found_all_possibility(workflow, index):
	result = []

	dont_go = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

	for rule in workflow[index]:

		tmp = {'x': [dont_go['x'][0], dont_go['x'][1]], 'm': [dont_go['m'][0], dont_go['m'][1]], 'a': [dont_go['a'][0], dont_go['a'][1]], 's': [dont_go['s'][0], dont_go['s'][1]]}
		if rule['operator'] == '>':
			tmp[rule['cat']][0] = max(tmp[rule['cat']][0], rule['value'] + 1)
			dont_go[rule['cat']][1] = min(dont_go[rule['cat']][1], rule['value'])
		else:
			tmp[rule['cat']][1] = min(tmp[rule['cat']][1], rule['value'] - 1)
			dont_go[rule['cat']][0] = max(dont_go[rule['cat']][0], rule['value'])

		if rule['go_to'] == 'A':
			result.append(tmp)
		elif rule['go_to'] != 'R':
			to_include = found_all_possibility(workflow, rule['go_to'])

			for current in to_include:
				to_append = {'x': [tmp['x'][0], tmp['x'][1]], 'm': [tmp['m'][0], tmp['m'][1]], 'a': [tmp['a'][0], tmp['a'][1]], 's': [tmp['s'][0], tmp['s'][1]]}
				to_append['x'][0] = max(to_append['x'][0], current['x'][0])
				to_append['x'][1] = min(to_append['x'][1], current['x'][1])
				to_append['m'][0] = max(to_append['m'][0], current['m'][0])
				to_append['m'][1] = min(to_append['m'][1], current['m'][1])
				to_append['a'][0] = max(to_append['a'][0], current['a'][0])
				to_append['a'][1] = min(to_append['a'][1], current['a'][1])
				to_append['s'][0] = max(to_append['s'][0], current['s'][0])
				to_append['s'][1] = min(to_append['s'][1], current['s'][1])

				if (to_append['x'][0] <= to_append['x'][1] and to_append['m'][0] <= to_append['m'][1] and
					to_append['a'][0] <= to_append['a'][1] and to_append['s'][0] <= to_append['s'][1]):
					result.append(to_append)

		if not(dont_go['x'][0] <= dont_go['x'][1] and dont_go['m'][0] <= dont_go['m'][1] and
			dont_go['a'][0] <= dont_go['a'][1] and dont_go['s'][0] <= dont_go['s'][1]):
			break

	return result


def level2(input):
	# Test value
	# input = 'px{a<2006:qkq,m>2090:A,rfg}\npv{a>1716:R,A}\nlnx{m>1548:A,A}\nrfg{s<537:gd,x>2440:R,A}\nqs{s>3448:A,lnx}\nqkq{x<1416:A,crn}\ncrn{x>2662:A,R}\nin{s<1351:px,qqz}\nqqz{s>2770:qs,m<1801:hdj,R}\ngd{a>3333:R,R}\nhdj{m>838:A,pv}\n\n{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}\n{x=2036,m=264,a=79,s=2244}\n{x=2461,m=1339,a=466,s=291}\n{x=2127,m=1623,a=2188,s=1013}\n'
	workflow = {}
	i = 0
	lines = input.strip().split('\n')
	while lines[i] != '':
		line = lines[i]
		tmp = line.split('{')
		name = tmp[0]
		workflow[name] = []
		for test in tmp[1][:-1].split(','):
			if ':' in test:
				re_str = r'([xmas])([<>])(\d+):([ARa-z]+)'

				match = regex.search(re_str, test)
				if match:
					groups = match.groups()

					workflow[name].append({'cat': groups[0], 'operator': groups[1], 'value': int(groups[2]), 'go_to': groups[3]})
			else:
				workflow[name].append({'cat': 'x', 'operator': '>', 'value': -1, 'go_to': test})

		i += 1

	all_possibilities = found_all_possibility(workflow, 'in')

	result = 0

	for current in all_possibilities:
		result += (current['x'][1] - current['x'][0] + 1) * (current['m'][1] - current['m'][0] + 1) * (current['a'][1] - current['a'][0] + 1) * (current['s'][1] - current['s'][0] + 1)

	return result