#!/usr/bin/python

import math

def calc_dist(a, b):
	return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))

def get_dist_mapping(b):
	mapping = []

	for i in range(len(b) - 1):
		for j in range(i + 1, len(b)):
			dist = calc_dist(b[i], b[j])
			mapping.append([[i,j], dist])

	return mapping

def create_circuits(links):
	has_create_circuits = False

	circuits = []

	for link in links:
		found = False

		for c in circuits:
			for l in link:
				if l in c:
					found = True
					break

			if found:
				for l in link:
					if not(l in c):
						c.append(l)
						has_create_circuits = True
				break

		if not(found):
			circuits.append(link)

	if has_create_circuits:
		return create_circuits(circuits)
	else:
		return circuits

def level1(input):
	#input = '162,817,812\n57,618,57\n906,360,560\n592,479,940\n352,342,300\n466,668,158\n542,29,236\n431,825,988\n739,650,466\n52,470,668\n216,146,977\n819,987,18\n117,168,530\n805,96,715\n346,949,466\n970,615,88\n941,993,340\n862,61,35\n984,92,344\n425,690,689\n'
	#nbr_box = 10

	nbr_box = 1000
	boxes = []
	for line in input.strip().split('\n'):
		boxes.append([int(x) for x in line.split(',')])

	mapping = get_dist_mapping(boxes)
	mapping = sorted(mapping, key=lambda x: x[1])

	circuits = create_circuits([x[0] for x in mapping[:nbr_box]])

	circuits = sorted(circuits, key=lambda x: -len(x))

	return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def level2(input):
	#input = '162,817,812\n57,618,57\n906,360,560\n592,479,940\n352,342,300\n466,668,158\n542,29,236\n431,825,988\n739,650,466\n52,470,668\n216,146,977\n819,987,18\n117,168,530\n805,96,715\n346,949,466\n970,615,88\n941,993,340\n862,61,35\n984,92,344\n425,690,689\n'
	#nbr_box = 10

	nbr_box = 1000

	boxes = []
	for line in input.strip().split('\n'):
		boxes.append([int(x) for x in line.split(',')])

	mapping = get_dist_mapping(boxes)
	mapping = sorted(mapping, key=lambda x: x[1])

	circuits = create_circuits([[x[0][0], x[0][1]] for x in mapping[:nbr_box]])
	cursor = nbr_box - 1

	while len(circuits) > 1 or len(circuits[0]) < len(boxes):
		circuits = sorted(circuits, key=lambda x: -len(x))
		cursor += 1

		circuits.append([x for x in mapping[cursor][0]])
		circuits = create_circuits(circuits)

	ia, ib = mapping[cursor][0]

	print(boxes[ia])
	print(boxes[ib])

	return boxes[ia][0] * boxes[ib][0]