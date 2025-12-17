#!/usr/bin/python

def treat_overlapping(freshes):
	to_treat = sorted(freshes, key=lambda x: (x[0], x[1]))

	cursor = 0

	while cursor < len(to_treat) - 1:
		current = to_treat[cursor]
		next_one = to_treat[cursor + 1]

		if current[1] + 1 >= next_one[0]:
			to_treat[cursor] = [current[0], max(current[1], next_one[1])]
			to_treat.pop(cursor + 1)
		else:
			cursor += 1

	return to_treat

def is_fresh(to_test, ranges):
	for start, end in ranges:
		if to_test >= start and to_test <= end:
			return True

		if to_test < start:
			return False

	return False

def count_fresh_ids(fresh_ids):
	result = 0

	for start, end in fresh_ids:
		result += end - start + 1

	return result


def level1(input):
	#input = '3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32\n'

	ranges, ids = [x.split('\n') for x in input.strip().split('\n\n')]

	fresh_ids = []

	for r in ranges:
		fresh_ids.append([int(x) for x in r.split('-')])

	fresh_ids = treat_overlapping(fresh_ids)

	result = 0

	for test_id in [int(x) for x in ids]:
		if is_fresh(test_id, fresh_ids):
			result += 1

	return result

def level2(input):
	#input = '3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32\n'

	ranges, ids = [x.split('\n') for x in input.strip().split('\n\n')]

	fresh_ids = []

	for r in ranges:
		fresh_ids.append([int(x) for x in r.split('-')])

	fresh_ids = treat_overlapping(fresh_ids)

	return count_fresh_ids(fresh_ids)