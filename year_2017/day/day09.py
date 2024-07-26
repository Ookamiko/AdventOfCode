#!/usr/bin/python

def remove_garbage(text):
	index = 0
	char_removed = 0
	inside_garbage = False
	correct_text = ''

	while index < len(text):
		if text[index] == '!' and inside_garbage:
			index += 1
		elif text[index] == '<' and not(inside_garbage):
			inside_garbage = True
		elif text[index] == '>' and inside_garbage:
			inside_garbage = False
		elif inside_garbage:
			char_removed += 1
		else:
			correct_text += text[index]

		index += 1

	return [correct_text, char_removed]

def score_group(text, index=0, point=0):
	score = point

	while index < len(text):
		if text[index] == '{':
			tmp = score_group(text, index + 1, point + 1)
			index = tmp[0]
			score += tmp[1]
		elif text[index] == '}':
			break

		index += 1

	return [index, score]

def level1(input):
	# Test value
	# input = '{{{},{},{{}}}}'
	without_garbage = remove_garbage(input)[0]
	return score_group(without_garbage)[1]

def level2(input):
	# Test value
	# input = '<{o"i!a,<{i<a>'
	return remove_garbage(input)[1]