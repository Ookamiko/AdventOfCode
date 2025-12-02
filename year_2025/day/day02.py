#!/usr/bin/python

def double_nbr(nbr):
	return repeat_nbr(nbr, 2)

def repeat_nbr(nbr, occurence):
	return int(''.join([str(nbr) for _ in range(occurence)]))

def treat_double(low, up):
	result = []
	base = '1'

	low_str = str(low)
	low_size = len(low_str)
	if low_size % 2 == 0:
		base = low_str[:(low_size//2)]
	else:
		base += ''.join(['0' for _ in range(low_size//2)])

	count = int(base)

	return find_repeat(count, low, up, 2)

def find_repeat(nbr, low, up, occurence):
	result = []

	while repeat_nbr(nbr, occurence) < low:
		nbr += 1

	while repeat_nbr(nbr, occurence) <= up:
		result.append(repeat_nbr(nbr, occurence))
		nbr += 1

	return result


def level1(input):
	#input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124\n'
	doubles = []

	for seg in input.strip().split(','):
		low, up = seg.split('-')
		doubles += treat_double(int(low), int(up))

	return sum(doubles)

def level2(input):
	#input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124\n'

	repeats = set()

	for seg in input.strip().split(','):
		low, up = seg.split('-')
		count = '1'
		size_count = len(count)

		while size_count <= len(up) // 2:
			occurences = []

			for size in range(max(2, len(low)), len(up) + 1):
				if size % size_count == 0:
					occurences.append(size // size_count)

			for occ in occurences:
				found = find_repeat(int(count), int(low), int(up), occ)

				for f in found:
					repeats.add(f)

			count += '0'
			size_count = len(count)

	return sum(repeats)