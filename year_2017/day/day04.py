#!/usr/bin/python

def level1(input):
	result = 0
	for passphrase in input.strip().split('\n'):
		words = passphrase.split(' ')
		dict_words = [*set(words)]
		if len(words) == len(dict_words):
			result += 1
	return result

def level2(input):
	result = 0
	for passphrase in input.strip().split('\n'):
		words = []
		for word in passphrase.split(' '):
			chars = [x for x in word]
			chars.sort()
			words.append(''.join(chars))

		dict_words = [*set(words)]
		if len(words) == len(dict_words):
			result += 1

	return result