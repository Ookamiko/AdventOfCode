#!/usr/bin/python

def level1(input):
	num = int(input)
	power = 1
	while power ** 2 < num:
		power += 2

	rest = power ** 2 - num

	while rest > power:
		rest -= power - 1

	if rest > (power - 1) // 2:
		middle = (power - 1) // 2
		rest = middle - (rest - middle)

	return (power - 1) // 2 + (((power - 1) // 2) - rest)

def get_next_value(x, y, mapping_ord, mapping_val):
	neightboor = [
		str(x-1) + ',' + str(y-1),
		str(x) + ',' + str(y-1),
		str(x+1) + ',' + str(y-1),
		str(x-1) + ',' + str(y),
		str(x+1) + ',' + str(y),
		str(x-1) + ',' + str(y+1),
		str(x) + ',' + str(y+1),
		str(x+1) + ',' + str(y+1),
	]

	result = 0

	for coord in neightboor:
		if not(coord in mapping_ord):
			continue
		index = mapping_ord.index(coord)
		result += mapping_val[index]

	return result

def level2(input):
	maximum = int(input)
	mapping_ord = ['0,0']
	mapping_val = [1]

	count = 3
	x = 0
	y = 0

	finish = False

	result = 0

	while not(finish):
		x += 1
		value = get_next_value(x, y, mapping_ord, mapping_val)

		if value > maximum:
			result = value
			break

		mapping_ord.append(str(x) + ',' + str(y))
		mapping_val.append(value)

		for i in range(count - 2):
			y -= 1
			value = get_next_value(x, y, mapping_ord, mapping_val)

			if value > maximum:
				result = value
				finish = True
				break

			mapping_ord.append(str(x) + ',' + str(y))
			mapping_val.append(value)

		if finish:
			break

		for i in range(count - 1):
			x -= 1
			value = get_next_value(x, y, mapping_ord, mapping_val)

			if value > maximum:
				result = value
				finish = True
				break

			mapping_ord.append(str(x) + ',' + str(y))
			mapping_val.append(value)

		if finish:
			break

		for i in range(count - 1):
			y += 1
			value = get_next_value(x, y, mapping_ord, mapping_val)

			if value > maximum:
				result = value
				finish = True
				break

			mapping_ord.append(str(x) + ',' + str(y))
			mapping_val.append(value)

		if finish:
			break

		for i in range(count - 1):
			x += 1
			value = get_next_value(x, y, mapping_ord, mapping_val)

			if value > maximum:
				result = value
				finish = True
				break

			mapping_ord.append(str(x) + ',' + str(y))
			mapping_val.append(value)

		count += 2

	return result