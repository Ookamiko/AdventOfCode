#!/usr/bin/python

def RetrieveCode(instructions, reverseJam=True):
	code = ''
	length = len(instructions.strip().split('\n')[0]) + 1
	for i in range(length - 1):
		tmp = [instructions[j] for j in range(len(instructions)) if j % length == i]
		tmpLetter = list(dict.fromkeys(tmp))
		tmpOrder = []
		for letter in tmpLetter:
			tmpOrder.append([letter, tmp.count(letter)])
		tmpOrder.sort(key=lambda x: x[1], reverse=reverseJam)
		code += tmpOrder[0][0]

	return code

def level1(input):
	return RetrieveCode(input)

def level2(input):
	return RetrieveCode(input, False)