#!/usr/bin/python
import re as regex

def level1(input):
	str_list = input.split("\n")
	compt = 0
	reg1 = r'[aeiou]'
	reg2 = r'(\S)\1'
	reg3 = r'(ab)|(cd)|(pq)|(xy)'
	for i in range(len(str_list)):
		nice = True
		nice &= len(regex.findall(reg1, str_list[i])) >= 3
		nice &= len(regex.findall(reg2, str_list[i])) > 0
		nice &= len(regex.findall(reg3, str_list[i])) == 0
		if nice:
			compt += 1

	return str(compt)

def level2(input):
	str_list = input.split("\n")
	compt = 0
	reg1 = r'(\S\S)\S*\1'
	reg2 = r'(\S)\S\1'
	for i in range(len(str_list)):
		nice = True
		nice &= len(regex.findall(reg1, str_list[i])) > 0
		nice &= len(regex.findall(reg2, str_list[i])) > 0
		if nice:
			compt += 1

	return str(compt)