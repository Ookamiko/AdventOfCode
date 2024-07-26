#!/usr/bin/python

def move_elem(array, old_ind, new_ind):
	elem = array.pop(old_ind)
	return array[:new_ind] + [elem] + array[new_ind:]

def test(key, real, pos):
	for i in range(len(pos)):
		ind = pos.index(i)
		offset = real[ind]
		if ind == 0 and offset < 0:
			ind = len(pos) - 1
		for j in range(abs(offset)):
			new_ind = ind + (-1 if offset < 0 else 1)
			if new_ind == 0:
				new_ind = len(pos) - 1
			elif new_ind >= len(pos):
				new_ind = 1
			real = move_elem(real, ind, new_ind)
			pos = move_elem(pos, ind, new_ind)
			ind = new_ind
		print(real)

def level1(input):
	#input = '1\n2\n-3\n3\n-2\n0\n4\n'
	real = []
	pos = []
	real_test = []
	pos_test = []
	numbers = [int(x) for x in input.strip().split('\n')]
	for i in range(len(numbers)):
		real.append(numbers[i])
		pos.append(i)

	for i in range(len(pos)):
		ind = pos.index(i)
		offset = real[ind]

		if offset == 0:
			continue
		elif offset > 0:
			offset = offset % (len(pos) - 1)
			new_ind = (ind + offset) % (len(pos) - 1)
		elif offset < 0:
			offset = (abs(offset) % (len(pos) - 1)) * -1
			new_ind = (ind + offset)
			if new_ind <= 0:
				new_ind += len(pos) - 1

		real = move_elem(real, ind, new_ind)
		pos = move_elem(pos, ind, new_ind)

	pos_0 = real.index(0)
	num_1000 = real[(pos_0 + 1000) % len(real)]
	print(num_1000)
	num_2000 = real[(pos_0 + 2000) % len(real)]
	print(num_2000)
	num_3000 = real[(pos_0 + 3000) % len(real)]
	print(num_3000)

	return num_1000 + num_2000 + num_3000

def level2(input):
	#input = '1\n2\n-3\n3\n-2\n0\n4\n'
	key = 811589153
	real = []
	pos = []
	real_test = []
	pos_test = []
	numbers = [int(x) * key for x in input.strip().split('\n')]
	for i in range(len(numbers)):
		real.append(numbers[i])
		pos.append(i)

	for j in range(10):
		for i in range(len(pos)):
			ind = pos.index(i)
			offset = real[ind]

			if offset == 0:
				continue
			elif offset > 0:
				offset = offset % (len(pos) - 1)
				new_ind = (ind + offset) % (len(pos) - 1)
			elif offset < 0:
				offset = (abs(offset) % (len(pos) - 1)) * -1
				new_ind = (ind + offset)
				if new_ind <= 0:
					new_ind += len(pos) - 1

			real = move_elem(real, ind, new_ind)
			pos = move_elem(pos, ind, new_ind)

	pos_0 = real.index(0)
	num_1000 = real[(pos_0 + 1000) % len(real)]
	print(num_1000)
	num_2000 = real[(pos_0 + 2000) % len(real)]
	print(num_2000)
	num_3000 = real[(pos_0 + 3000) % len(real)]
	print(num_3000)

	return num_1000 + num_2000 + num_3000