#!/usr/bin/python

import re as regex

def level1(input):
	#input = 'abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n'
	sum_triple = 0
	sum_double = 0
	for current in input.strip().split('\n'):
		keys = list(dict.fromkeys(current))
		found_triple = False
		found_double = False

		for key in keys:
			if not(found_triple) and current.count(key) == 3:
				found_triple = True
				sum_triple += 1

			elif not(found_double) and current.count(key) == 2:
				found_double = True
				sum_double += 1

			if found_double and found_triple:
				break;

	return sum_triple * sum_double

def level2(input):
	#input = "abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz\n"
	to_test = input.strip().split('\n')
	literal1 = ""
	literal2 = ""
	found = False
	for i in range(len(to_test)):
		literal1 = to_test[i]

		for current in to_test[i+1:]:
			literal2 = current

			if (test_literal(list(literal1), list(literal2), False)):
				found = True
				break

		if found:
			break

	solution = ""
	for i in range(len(literal1)):
		if literal1[i] == literal2[i]:
			solution += literal1[i]
		else:
			solution += ''.join(literal1[i+1:])
			break

	return solution

def test_literal(code1, code2, found_error):
	if len(code1) > 1:
		if found_error and code1[0] != code2[0]:
			return False
		elif code1[0] == code2[0]:
			return test_literal(code1[1:], code2[1:], found_error)
		elif code1[0] != code2[0]:
			return test_literal(code1[1:], code2[1:], True)

	else:
		return code1[0] == code2[0] or (code1[0] != code2[0] and not(found_error))