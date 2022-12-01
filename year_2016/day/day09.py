#!/usr/bin/python

def uncompress(file, cursor, size, occurence):
	sequence = file[cursor + 1 : cursor + 1 + size]

	return ''.join([sequence] * occurence)

def level1(input):
	compressed_file = input.strip()
	cursor = 0
	decompressed_file = ''
	found_marker = False
	marker = ''

	while cursor < len(compressed_file):

		if found_marker:
			if compressed_file[cursor] == ')':
				numbers = marker.split('x')
				decompressed_file += uncompress(compressed_file, cursor, int(numbers[0]), int(numbers[1]))
				found_marker = False
				marker = ''
				cursor += int(numbers[0])
			else:
				marker += compressed_file[cursor]

		elif compressed_file[cursor] == '(':
			found_marker = True
		else:
			decompressed_file += compressed_file[cursor]

		cursor += 1

	return len(decompressed_file)

def calculate_uncompress_length(file):
	length = 0
	cursor = 0
	found_marker = False
	marker = ''

	while cursor < len(file):

		if found_marker:
			if file[cursor] == ')':
				numbers = marker.split('x')
				size = int(numbers[0])
				muli = int(numbers[1])
				sequence = file[cursor + 1 : cursor + 1 + size]

				if '(' in sequence:
					length += calculate_uncompress_length(sequence) * muli
				else:
					length += size * muli

				cursor += size
				found_marker = False
				marker = ''

			else:
				marker += file[cursor]

		elif file[cursor] == '(':
			found_marker = True
		else:
			length += 1

		cursor += 1

	return length

def level2(input):
	return calculate_uncompress_length(input.strip())