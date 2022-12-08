#!/usr/bin/python

def dragon_curve(initial, length):
	a = initial
	while len(a) < length:
		b = ''.join([x.replace('1', 'a').replace('0', '1').replace('a', '0') for x in a[::-1]])
		a = a + '0' + b

	return a[:length]

def checksum(data):
	while len(data) % 2 == 0:
		next_data = ''
		for i in range(0, len(data), 2):
			next_data += '1' if data[i] == data[i+1] else '0'

		data = next_data

	return data

def level1(input):
	#input = '10000'
	dragon = dragon_curve(input.strip(), 272)
	return checksum(dragon)

def level2(input):
	dragon = dragon_curve(input.strip(), 35651584)
	return checksum(dragon)