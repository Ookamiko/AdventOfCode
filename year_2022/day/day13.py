#!/usr/bin/python

def compare(a, b):
	for i in range(len(a)):
		if i >= len(b):
			return -1

		if type(a[i]) == type(b[i]) and type(a[i]) == type(5):
			if a[i] < b[i]:
				return 1
			elif a[i] > b[i]:
				return -1

		elif type(a[i]) == type(b[i]) and type(a[i]) == type([]):
			tmp_result = compare(a[i], b[i])
			if tmp_result != 0:
				return tmp_result

		else:
			if type(a[i]) == type([]):
				tmp_result = compare(a[i], [b[i]])
				if tmp_result != 0:
					return tmp_result
			else:
				tmp_result = compare([a[i]], b[i])
				if tmp_result != 0:
					return tmp_result

	return 0 if len(a) == len(b) else 1


def convert_string_to_list(string, cursor=1):
	list = []
	cypher = ''

	while cursor < len(string):

		if string[cursor] == '[':
			tmp_array, cursor = convert_string_to_list(string, cursor + 1)
			list.append(tmp_array)
		elif string[cursor] == ']':
			break
		elif string[cursor] == ',':
			if len(cypher) != 0:
				list.append(int(cypher))
				cypher = ''
		else:
			cypher += string[cursor]

		cursor += 1

	if len(cypher) != 0:
		list.append(int(cypher))
		cypher = ''

	return list, cursor

def bubble_sort(liste):
	finish = False
	offset = 1

	while not(finish):
		finish = True

		for i in range(len(liste) - offset):
			if compare(liste[i], liste[i + 1]) == -1:
				tmp = liste[i + 1]
				liste[i + 1] = liste[i]
				liste[i] = tmp
				finish = False

		offset += 1

	return liste

def display_packet(packets):
	for packet in packets:
		print(packet)

def level1(input):
	#input = '[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]\n'
	lines = input.strip().split('\n')
	count = 0

	for i in range(0, len(lines), 3):
		a = convert_string_to_list(lines[i])
		b = convert_string_to_list(lines[i+1])
		if compare(a, b) == 1:
			count += (i // 3) + 1

	return count

def level2(input):
	#input = '[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]\n'
	lines = input.strip().split('\n')

	all_packet = [[[2]], [[6]]]

	for i in range(0, len(lines), 3):
		a, tmp = convert_string_to_list(lines[i])
		b, tmp = convert_string_to_list(lines[i+1])
		all_packet.append(a)
		all_packet.append(b)

	all_packet = bubble_sort(all_packet)

	count = 1

	for i in range(len(all_packet)):
		if compare([[2]], all_packet[i]) == 0 or compare([[6]], all_packet[i]) == 0:
			count *= (i + 1)

	return count