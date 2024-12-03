#!/usr/bin/python

import re as regex

def level1(input):
	#input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
	all_mul = [(int(x[0]), int(x[1])) for x in
		regex.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)]

	result = 0

	for x, y in all_mul:
		result += x * y

	return result

def level2(input):
	#input = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
	all_infos = regex.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', input)

	all_mul = []
	allowed = True

	for info in all_infos:
		if allowed and info[1] != '':
			allowed = False
		elif not(allowed) and info[0] != '':
			allowed = True
		elif allowed and info[2] != '':
			all_mul.append((int(info[2]), int(info[3])))

	result = 0

	for x, y in all_mul:
		result += x * y

	return result