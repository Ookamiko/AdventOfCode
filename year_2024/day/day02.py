#!/usr/bin/python

def IsValidReport(report):
	mode = ''
	for i in range(len(report) - 1):
		c = report[i]
		n = report[i + 1]

		if (
			(mode == 'dec' and c <= n) or
			(mode == 'inc' and c >= n) or
			not(abs(c - n) in range(1,4))
		):
			return False
		elif mode == '':
			mode = 'dec' if c > n else 'inc'

	return True

def level1(input):
	#input = '7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n'

	result = 0

	for line in input.strip().split('\n'):
		levels = [int(x) for x in line.split(' ')]

		if IsValidReport(levels):
			result += 1

	return result

def level2(input):
	#input = '7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n'

	result = 0

	for line in input.strip().split('\n'):
		levels = [int(x) for x in line.split(' ')]

		if IsValidReport(levels):
			result += 1
		else:
			i = 0
			while i < len(levels):
				retry = levels.copy()
				retry.pop(i)
				if IsValidReport(retry):
					result += 1
					break
				else:
					i += 1

	return result