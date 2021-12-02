#!/usr/bin/python

def level1(input):
	count_inc = 0
	depth = input.strip().split('\n')
	for i in range(len(depth) - 1):
		if (int(depth[i]) < int(depth[i + 1])):
			count_inc += 1

	return count_inc

def level2(input):
	count_inc = 0
	depth = input.strip().split('\n')
	for i in range(len(depth) - 3):
		first_slide = int(depth[i]) + int(depth[i + 1]) + int(depth[i + 2])
		second_slide = int(depth[i + 1]) + int(depth[i + 2]) + int(depth[i + 3])
		if first_slide < second_slide:
			count_inc += 1

	return count_inc