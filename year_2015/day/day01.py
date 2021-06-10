#!/usr/bin/python

def level1(input):
	str_list = list(input)
	return str(str_list.count('(') - str_list.count(')'))

def level2(input):
	str_list = list(input)
	count = 0
	index = 0
	for i in range(len(str_list)):
		count += 1 if str_list[i] == '(' else -1
		if count < 0:
			index = i
			break;

	return str(index + 1)