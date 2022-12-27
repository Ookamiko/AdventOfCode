#!/usr/bin/python

def snafu_to_decimal(snafu):
	result = 0
	size = len(snafu)

	for i in range(len(snafu)):
		char = snafu[i]

		value = 0
		if char == '2':
			value = 2
		elif char == '1':
			value = 1
		elif char == '0':
			value = 0
		elif char == '-':
			value = -1
		elif char == '=':
			value = -2

		result += value  * (5 ** (size - i - 1))

	return result

def get_value(values, power_of_5):
	if len(values) == 0:
		return 0

	result = 0

	for i in range(len(values)):
		result += values[i] * power_of_5[i]

	return result

def recursive_transform(number, power_of_5, values=[], rest_was_negative=True):
	current_value = get_value(values, power_of_5)
	rest = current_value - number

	if number == current_value:
		while len(values) != len(power_of_5):
			values.append(0)
		return values, False

	if len(values) == len(power_of_5):
		return [], (rest_was_negative and rest > 0) or (not(rest_was_negative) and rest < 0)

	next_value = []

	if rest < 0:
		next_value = [2, 1, 0]
	else:
		next_value = [-2, -1, 0]

	has_change_sign = False
	for value in next_value:
		tmp_values, has_change_sign = recursive_transform(number, power_of_5, values + [value], rest < 0)
		if len(tmp_values) != 0:
			return tmp_values, False

		if not(has_change_sign):
			break

	return [], has_change_sign or (rest_was_negative and rest > 0) or (not(rest_was_negative) and rest < 0)

def decimal_to_snafu(number):
	power_of_5 = []
	count = 0
	current = 5 ** count
	while current < number:
		power_of_5.append(current)
		count += 1
		current = 5 ** count

	test = current
	for value in power_of_5:
		test -= 2 * value

	if test < number:
		power_of_5.append(current)
	power_of_5.sort(reverse=True)

	values = recursive_transform(number, power_of_5, [])

	return ''.join([str(x) for x in values[0]]).replace('-2', '=').replace('-1', '-')

def level1(input):
	#input = '1=-0-2\n12111\n2=0=\n21\n2=01\n111\n20012\n112\n1=-1=\n1-12\n12\n1=\n122\n'
	somme = 0
	for snafu in input.strip().split('\n'):
		somme += snafu_to_decimal(snafu)

	return decimal_to_snafu(somme)

def level2(input):
	return "Done"