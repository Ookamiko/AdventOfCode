#!/usr/bin/python

def level1(input):
	# Test value
	# input = '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet\n'
	lines = input.strip().split('\n')
	digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	to_return = 0

	for line in lines:
		save = ''

		# first digit
		for i in range(0, len(line)):
			if line[i] in digit:
				save = save + line[i]
				break

		# last digit
		for i in range(len(line) - 1, -1, -1):
			if line[i] in digit:
				save = save + line[i]
				break

		to_return = to_return + int(save)

	return to_return

def level2(input):
	# Test value
	# input = 'two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen\n'
	lines = input.strip().split('\n')
	digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	digit_str_3 = [
		['one', '1'],
		['two', '2'],
		['six', '6']
	]
	digit_str_4 = [
		['four', '4'],
		['five', '5'],
		['nine', '9']
	]
	digit_str_5 = [
		['three', '3'],
		['seven', '7'],
		['eight', '8']
	]
	to_return = 0

	for line in lines:
		save = ''

		# first digit
		for i in range(0, len(line)):
			found = False

			if line[i] in digit:
				save = save + line[i]
				found = True

			if i < len(line) - 3 and not(found):
				for test in digit_str_3:
					if (test[0] == line[i:i + 3]):
						save = save + test[1]
						found = True
						break

			if i < len(line) - 4 and not(found):
				for test in digit_str_4:
					if (test[0] == line[i:i + 4]):
						save = save + test[1]
						found = True
						break

			if i < len(line) - 5 and not(found):
				for test in digit_str_5:
					if (test[0] == line[i:i + 5]):
						save = save + test[1]
						found = True
						break
			if found:
				break

		# last digit
		for i in range(len(line) - 1, -1, -1):
			found = False

			if line[i] in digit:
				save = save + line[i]
				found = True

			if i - 2 >= 0 and not(found):
				for test in digit_str_3:
					if (test[0] == line[i - 2:i + 1]):
						save = save + test[1]
						found = True
						break

			if i - 3 >= 0 and not(found):
				for test in digit_str_4:
					if (test[0] == line[i - 3:i + 1]):
						save = save + test[1]
						found = True
						break

			if i - 4 >= 0 and not(found):
				for test in digit_str_5:
					if (test[0] == line[i - 4:i + 1]):
						save = save + test[1]
						found = True
						break

			if found:
				break

		to_return = to_return + int(save)

	return to_return