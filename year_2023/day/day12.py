#!/usr/bin/python

import re as regex
from functools import cache

@cache
def get_all_possibilities(springs, groups):
	if len(groups) == 0:
		if not('#' in springs):
			return 1
		else:
			return 0

	new_groups = [int(x) for x in groups.split(',')]

	min_len = sum(new_groups) + len(new_groups) - 1
	if len(springs) < min_len:
		return 0

	result = 0

	in_groups = False
	breaks = False
	terminate_index = -1

	for i in range(len(springs)):

		if len(new_groups) == 0:
			terminate_index = i
			breaks = True
			break

		if new_groups[0] < 0:
			breaks = True
			break

		if springs[i] == '#':
			new_groups[0] -= 1
			in_groups = True

		elif springs[i] == '.':
			if in_groups and new_groups[0] > 0:
				breaks = True
				break
			elif in_groups and new_groups[0] == 0:
				if len(new_groups) == 0:
					terminate_index = i
					breaks = True
					break
				new_groups.pop(0)
				in_groups = False

		elif springs[i] == '?':
			if in_groups:
				if new_groups[0] > 0:
					springs = springs.replace('?', '#', 1)
					new_groups[0] -= 1
				elif new_groups[0] == 0:
					springs = springs.replace('?', '.', 1)
					if len(new_groups) == 0:
						terminate_index = i
						breaks = True
						break
					new_groups.pop(0)
					in_groups = False
			else:
				# Test possibility of starting group
				size = new_groups[0]
				to_check = springs[i:i + size]
				if not('.' in to_check) and (i + size == len(springs) or (i+size < len(springs) and springs[i+size] != '#')):
					to_send = ''
					if i + size + 1 < len(springs):
						to_send = springs[i + size + 1:]
					to_send_group = ''
					if len(new_groups) > 1:
						to_send_group = ','.join([str(x) for x in new_groups[1:]])

					result += get_all_possibilities(to_send, to_send_group)

				result += get_all_possibilities(springs[i + 1:], ','.join([str(x) for x in new_groups]))
				breaks = True
				break


	if len(new_groups) != 0 and new_groups[0] == 0:
		new_groups.pop(0)

	if ((terminate_index != -1 and not('#' in springs[terminate_index:])) or
		(i + 1 == len(springs) and not(breaks) and len(new_groups) == 0)):
		result += 1


	return result


def level1(input):
	# Test value
	# input = '???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1\n'
	lines = input.strip().split('\n')
	result = 0
	for line in lines:
		springs = line.split(' ')[0]
		groups = line.split(' ')[1]

		poss = get_all_possibilities(springs, groups)
		print(line + ': ' + str(poss))
		result += poss

	return result

def level2(input):
	# Test value
	input = '???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1\n'
	lines = input.strip().split('\n')
	result = 0
	for i in range(len(lines)):
		line = lines[i]
		tmp_s = [line.split(' ')[0]] * 5
		springs = '?'.join(tmp_s)

		tmp_g = [line.split(' ')[1]] * 5
		groups = ','.join(tmp_g)

		poss = get_all_possibilities(springs, groups)
		print(str(i + 1) + '/' + str(len(lines)) + ' - ' + line + ': ' + str(poss))
		result += poss

	return result