#!/usr/bin/python
import re
 
def lookandsay(sequence):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), sequence)

def NextConwaySequence(str_number):
	count = 0
	remember_char = ''
	toReturn = ''
	for char in str_number:
		if remember_char != char:
			if count != 0:
				toReturn = toReturn + str(count) + remember_char
			count = 1
			remember_char = char
		else:
			count += 1

	return toReturn + str(count) + remember_char



def level1(input):
	conway_sequence = input.strip()
	for i in range(40):
		conway_sequence = lookandsay(conway_sequence)

	return str(len(conway_sequence))

def level2(input):
	conway_sequence = input.strip()
	for i in range(50):
		conway_sequence = lookandsay(conway_sequence)

	return str(len(conway_sequence))