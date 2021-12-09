#!/usr/bin/python

import re as regex

def DecryptNumber(cyphers, number):
	afficheur = [''] * 10
	afficheur[1] = cyphers[0]
	afficheur[7] = cyphers[1]
	afficheur[4] = cyphers[2]
	afficheur[8] = cyphers[9]

	# Determine 3
	
	reg = r'[' + afficheur[1] + ']'

	test1 = regex.findall(reg, cyphers[3])
	test2 = regex.findall(reg, cyphers[4])
	test3 = regex.findall(reg, cyphers[5])

	lastTest = []

	if len(test1) == 2:
		afficheur[3] = cyphers[3]
		lastTest = [cyphers[4], cyphers[5]]
	elif len(test2) == 2:
		afficheur[3] = cyphers[4]
		lastTest = [cyphers[3], cyphers[5]]
	elif len(test3) == 2:
		afficheur[3] = cyphers[5]
		lastTest = [cyphers[3], cyphers[4]]

	# Determine 2 and 5
	
	reg = r'[^' + lastTest[0] + ']'
	segment4 = regex.findall(reg, afficheur[4])

	if len(segment4) == 2:
		afficheur[2] = lastTest[0]
		afficheur[5] = lastTest[1]
	else:
		afficheur[2] = lastTest[1]
		afficheur[5] = lastTest[0]

	# Determine 6, 9 and 0

	reg = r'[' + afficheur[1] + ']'

	test1 = regex.findall(reg, cyphers[6])
	test2 = regex.findall(reg, cyphers[7])
	test3 = regex.findall(reg, cyphers[8])

	if len(test1) == 1:
		afficheur[6] = cyphers[6]
		lastTest = [cyphers[7], cyphers[8]]
	elif len(test2) == 1:
		afficheur[6] = cyphers[7]
		lastTest = [cyphers[6], cyphers[8]]
	elif len(test3) == 1:
		afficheur[6] = cyphers[8]
		lastTest = [cyphers[6], cyphers[7]]

	reg = r'[' + afficheur[5] + ']'

	test = regex.findall(reg, lastTest[0])

	if len(test) == 4:
		afficheur[0] = lastTest[0]
		afficheur[9] = lastTest[1]
	else:
		afficheur[9] = lastTest[0]
		afficheur[0] = lastTest[1]

	mil = afficheur.index(number[0])
	cent = afficheur.index(number[1])
	dix = afficheur.index(number[2])
	unit = afficheur.index(number[3])

	return mil * 1000 + cent * 100 + dix * 10 + unit


def level1(input):
	allmatch = list(value for value in input.replace('\n', ' ').strip().split(' ') if (len(value) >= 2 and len(value) <= 4) or len(value) == 7)
	return len(allmatch) - 4 * len(input.strip().split('\n'))

def level2(input):
	# input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
	instructions = input.strip().split('\n')
	result = 0
	for current in instructions:
		tmp = current.split(' | ')

		cyphers = []
		for specific in tmp[0].split(' '):
			tmpc = list(specific)
			tmpc.sort()
			cyphers.append(''.join(tmpc))
		cyphers.sort(key=lambda x: len(x))

		number = []
		for specific in tmp[1].split(' '):
			tmpc = list(specific)
			tmpc.sort()
			number.append(''.join(tmpc))

		result += DecryptNumber(cyphers, number)

	return result