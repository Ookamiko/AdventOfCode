#!/usr/bin/python
import hashlib

def level1(input):
	compt = 0
	while(hashlib.md5((input.strip() + str(compt)).encode()).hexdigest()[0:5] != "00000"):
		compt += 1
	return str(compt)

def level2(input):
	compt = 0
	while(hashlib.md5((input.strip() + str(compt)).encode()).hexdigest()[0:6] != "000000"):
		compt += 1
	return str(compt)