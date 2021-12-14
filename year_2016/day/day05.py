#!/usr/bin/python

import hashlib, random

def level1(input):
	code = []
	compt = 0
	while len(code) != 8:
		tmp = hashlib.md5((input.strip() + str(compt)).encode()).hexdigest()
		if tmp[0:5] == "00000":
			code.append(tmp[5])
		compt += 1
	return ''.join(code)

def level2(input):
	code = ['.'] * 8
	compt = 0
	while code.count('.') != 0:
		tmp = hashlib.md5((input.strip() + str(compt)).encode()).hexdigest()
		if tmp[0:5] == "00000":
			position = int(tmp[5], 16)
			if position < 8 and code[position] == '.':
				code[position] = tmp[6]
				print(''.join(code))
#		if compt % 10000 == 0:
#			tmpCode = ''
#			for letter in code:
#				tmpCode += letter if letter != '.' else chr(random.randrange(33, 126))
#			print(tmpCode)
		compt += 1


	return ''.join(code)