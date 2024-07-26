#!/usr/bin/python
import re as regex

def level1(input):
	str_list = input.strip().split("\n")
	count_total = 0
	count_code = 0

	for current in str_list:
		count_total += len(current)
		count_code += len(regex.sub(r'(\\\\)|(\\")|(\\x[a-f0-9]{2})', "a", current).replace("\"", ""))

	return str(count_total - count_code)

def level2(input):
	str_list = input.strip().split("\n")
	count_new = 0
	count_old = 0

	for current in str_list:
		count_old += len(current)
		count_new += len(current.replace('\\', '\\\\').replace('"', '\\"')) + 2

	return str(count_new - count_old)