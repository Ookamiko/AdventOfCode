#!/usr/bin/python

def level1(input):
	#input = 'L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n'
	point = 50
	soluce = 0

	for inst in input.strip().split('\n'):
		direction = inst[0]
		count = int(inst[1:])

		# reduce to minimum
		count = count % 100

		if direction == 'L':
			point -= count
		elif direction == 'R':
			point += count

		if point < 0:
			point += 100
		elif point >= 100:
			point -= 100

		if point == 0:
			soluce += 1

	return soluce

def level2(input):
	#input = 'L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n'
	point = 50
	soluce = 0

	for inst in input.strip().split('\n'):
		direction = inst[0]
		count = int(inst[1:])

		# reduce to minimum and count over-0 step
		soluce += count // 100
		count = count % 100

		if direction == 'L':
			# small correction if start at 0 to not count over-0 step
			if point == 0:
				soluce -= 1
			point -= count
		elif direction == 'R':
			point += count

		if point < 0:
			point += 100
			soluce += 1
		elif point >= 100:
			point -= 100
			soluce += 1
		elif point == 0:
			soluce += 1


	return soluce