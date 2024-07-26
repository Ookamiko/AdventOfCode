#!/usr/bin/python

import re as regex

def next_value(value, factor):
	return (value * factor) % 2147483647

def get_binary_part(value):
	tmp = bin(value)[2:].zfill(16)
	return tmp[len(tmp) - 16:]

def level1(input):
	# Test value
	# input = '65 8921'
	tmp = regex.findall(r'\d+', input)
	gen_a = int(tmp[0])
	gen_b = int(tmp[1])
	factor_a = 16807
	factor_b = 48271

	match = 0

	for i in range(40000000):
		gen_a = next_value(gen_a, factor_a)
		gen_b = next_value(gen_b, factor_b)

		if get_binary_part(gen_a) == get_binary_part(gen_b):
			match += 1

	return match

def level2(input):
	# Test value
	# input = '65 8921'
	tmp = regex.findall(r'\d+', input)
	gen_a = int(tmp[0])
	gen_b = int(tmp[1])
	factor_a = 16807
	factor_b = 48271

	match = 0

	for i in range(5000000):
		gen_a = next_value(gen_a, factor_a)
		while gen_a % 4 != 0:
			gen_a = next_value(gen_a, factor_a)

		gen_b = next_value(gen_b, factor_b)
		while gen_b % 8 != 0:
			gen_b = next_value(gen_b, factor_b)

		if get_binary_part(gen_a) == get_binary_part(gen_b):
			match += 1

	return match