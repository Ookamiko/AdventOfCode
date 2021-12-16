#!/usr/bin/python

import sys

def GetBinary(hexa):
	tmp = str(bin(int(hexa, 16))).replace('0b', '')
	return ''.join(['0'] * (len(hexa) * 4 - len(tmp))) + tmp

def CalculateVersion(binary):
	packetV = int(binary[0:3], 2)
	packetID = int(binary[3:6], 2)

	length = 0

	if packetID == 4:
		# Literal
		literal = ''
		for position in range(6, len(binary), 5):
			subBinary = binary[position:position+5]
			literal += subBinary[1:]
			if subBinary[0] == '0':
				length = position + 5
				break
	else:
		# Operator
		length = 7
		lengthTypeId = binary[6]
		if lengthTypeId == '0':
			length += 15
			totalLength = int(binary[7:22], 2)
			tmpLength = 0
			position = 22
			while tmpLength != totalLength:
				tmpResult = CalculateVersion(binary[position:])
				tmpLength += tmpResult['length']
				position += tmpResult['length']
				packetV += tmpResult['version']

			length += tmpLength
		else:
			length += 11
			nbrSub = int(binary[7:18], 2)
			position = 18
			for i in range(nbrSub):
				tmpResult = CalculateVersion(binary[position:])
				length += tmpResult['length']
				position += tmpResult['length']
				packetV += tmpResult['version']

	return {'version': packetV, 'length': length}


def CalculateValue(binary):
	packetV = int(binary[0:3], 2)
	packetID = int(binary[3:6], 2)

	length = 0
	value = 0

	if packetID == 4:
		# Literal
		literal = ''
		for position in range(6, len(binary), 5):
			subBinary = binary[position:position+5]
			literal += subBinary[1:]
			if subBinary[0] == '0':
				length = position + 5
				break
		value = int(literal, 2)
	else:
		# Operator
		length = 7
		lengthTypeId = binary[6]
		tmpValue = []
		if lengthTypeId == '0':
			length += 15
			totalLength = int(binary[7:22], 2)
			tmpLength = 0
			position = 22
			while tmpLength != totalLength:
				tmpResult = CalculateValue(binary[position:])
				tmpLength += tmpResult['length']
				position += tmpResult['length']
				tmpValue.append(tmpResult['value'])

			length += tmpLength
		else:
			length += 11
			nbrSub = int(binary[7:18], 2)
			position = 18
			for i in range(nbrSub):
				tmpResult = CalculateValue(binary[position:])
				length += tmpResult['length']
				position += tmpResult['length']
				tmpValue.append(tmpResult['value'])

		if packetID == 0:
			value = sum(tmpValue)
		elif packetID == 1:
			value = 1
			for tmp in tmpValue:
				value *= tmp
		elif packetID == 2:
			value = sys.maxsize
			for tmp in tmpValue:
				value = min(value, tmp)
		elif packetID == 3:
			value = 0
			for tmp in tmpValue:
				value = max(value, tmp)
		elif packetID == 5:
			value = 1 if tmpValue[0] > tmpValue[1] else 0
		elif packetID == 6:
			value = 1 if tmpValue[0] < tmpValue[1] else 0
		elif packetID == 7:
			value = 1 if tmpValue[0] == tmpValue[1] else 0

	return {'value': value, 'length': length}

def level1(input):
	binary = GetBinary(input.strip())
	result = CalculateVersion(binary)
	return result['version']

def level2(input):
	binary = GetBinary(input.strip())
	result = CalculateValue(binary)
	return result['value']