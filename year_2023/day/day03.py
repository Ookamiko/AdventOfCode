#!/usr/bin/python

def get_around_index(index, nbr_line, nbr_char):
	result = []

	# Left
	if (index - 1) % nbr_char != nbr_char - 1:
		result.append(index - 1)

		if index - nbr_char >= 0:
			result.append(index - (nbr_char + 1))

		if index + nbr_char < nbr_line * nbr_char:
			result.append(index + (nbr_char - 1))

	# Middle
	if index - nbr_char >= 0:
		result.append(index - nbr_char)

	if index + nbr_char < nbr_line * nbr_char:
		result.append(index + nbr_char)

	# Right
	if (index + 1) % nbr_char != 0:
		result.append(index + 1)

		if index - nbr_char >= 0:
			result.append(index - (nbr_char - 1))

		if index + nbr_char < nbr_line * nbr_char:
			result.append(index + (nbr_char + 1))

	return result

def check_symbol(manuel, list_index):
	result = False
	for index in list_index:
		if manuel[index] != '.' and not(manuel[index].isnumeric()):
			result = True
			break

	return result


def check_symbol_gear(manuel, list_index):
	result = False
	index_gear = -1
	for index in list_index:
		if manuel[index] == '*':
			result = True
			index_gear = index
			break

	return [result, index_gear]

def level1(input):
	# Test value
	# input = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..\n'
	tmp = input.strip().split('\n')
	manuel = ''.join(tmp)
	nbr_line = len(tmp)
	nbr_char = len(tmp[0])
	result = 0

	saved_number = ''
	symbol_found = False

	for i in range(len(manuel)):
		current = manuel[i]

		if not(current.isnumeric()) or i % nbr_char == 0:
			if saved_number != '' and symbol_found:
				result += int(saved_number)

			saved_number = ''
			symbol_found = False

		if current.isnumeric():
			saved_number += current
			if not(symbol_found):
				symbol_found = check_symbol(manuel, get_around_index(i, nbr_line, nbr_char))

	if saved_number != '' and symbol_found:
		result += int(saved_number)

	return result

def level2(input):
	# Test value
	# input = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..\n'
	tmp = input.strip().split('\n')
	manuel = ''.join(tmp)
	nbr_line = len(tmp)
	nbr_char = len(tmp[0])

	saved_number = ''
	symbol_found = False
	saved_gear = {}
	saved_gear_index = ''

	for i in range(len(manuel)):
		current = manuel[i]

		if not(current.isnumeric()) or i % nbr_char == 0:
			if saved_number != '' and symbol_found and saved_gear_index != '':
				if not(saved_gear_index in saved_gear.keys()):
					saved_gear[saved_gear_index] = []

				saved_gear[saved_gear_index].append(int(saved_number))

			saved_number = ''
			symbol_found = False
			saved_gear_index = ''

		if current.isnumeric():
			saved_number += current
			if not(symbol_found):
				tmp_found_gear = check_symbol_gear(manuel, get_around_index(i, nbr_line, nbr_char))
				symbol_found = tmp_found_gear[0]
				if symbol_found:
					saved_gear_index = str(tmp_found_gear[1])

	result = 0

	for key in saved_gear.keys():
		if len(saved_gear[key]) == 2:
			result += saved_gear[key][0] * saved_gear[key][1]

	return result