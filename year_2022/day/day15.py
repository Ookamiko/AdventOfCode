#!/usr/bin/python

import re as regex

def get_dist(pos_a, pos_b):
	return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

def get_blank_zone(sensor_pos, beacon_pos, rank):
	dist_to_beacon = get_dist(sensor_pos, beacon_pos)
	dist_to_rank = abs(sensor_pos[1] - rank)
	result = []

	if dist_to_rank <= dist_to_beacon:
		offset_rank = dist_to_beacon - dist_to_rank
		result = [sensor_pos[0] - offset_rank, sensor_pos[0] + offset_rank]

	return result

def stringify_pos(pos):
	return str(pos[0]) + ',' + str(pos[1])

def reduce_zone(zones):
	result = []
	tmp_zone = []

	zones.sort(key=lambda x: x[0])

	for zone in zones:
		if len(tmp_zone) == 0:
			tmp_zone = [zone[0], zone[1]]
		elif tmp_zone[1] >= zone[0]:
			if tmp_zone[1] <= zone[1]:
				tmp_zone[1] = zone[1]
		else:
			result.append(tmp_zone)
			tmp_zone = [zone[0], zone[1]]

	if len(tmp_zone) != 0:
		result.append(tmp_zone)

	return result

def level1(input):
	#input = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3\n'
	#rank = 10
	rank = 2000000
	zones = []
	to_remove = []

	for line in input.strip().split('\n'):
		nums = [int(x) for x in regex.findall(r'-?\d+', line)]
		tmp_zone = get_blank_zone([nums[0], nums[1]], [nums[2], nums[3]], rank)
		if len(tmp_zone) != 0:
			zones.append(tmp_zone)

		if nums[1] == rank:
			string = stringify_pos([nums[0], nums[1]])
			if not(string) in to_remove:
				to_remove.append(string)

		if nums[3] == rank:
			string = stringify_pos([nums[2], nums[3]])
			if not(string) in to_remove:
				to_remove.append(string)

	zones = reduce_zone(zones)
	count_blank = 0

	for zone in zones:
		count_blank += zone[1] - zone[0] + 1

	return count_blank - len(to_remove)

def level2(input):
	#input = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3\n'
	#max_rank = 20
	max_rank = 4000000
	zones = []
	to_remove = []

	for i in range(max_rank):
		zones.append([])

	for line in input.strip().split('\n'):
		nums = [int(x) for x in regex.findall(r'-?\d+', line)]
		for i in range(max_rank):
			tmp_zone = get_blank_zone([nums[0], nums[1]], [nums[2], nums[3]], i)
			if len(tmp_zone) != 0:
				zones[i].append(tmp_zone)

	result = []

	for i in range(max_rank):
		min_found = 0
		for zone in reduce_zone(zones[i]):
			if zone[0] <= min_found and zone[1] >= max_rank:
				continue
			elif zone[0] > min_found:
				result = [min_found, i]
				break
			else:
				min_found = zone[1] + 1

		if len(result) != 0:
			break

	return result[0] * max_rank + result[1]