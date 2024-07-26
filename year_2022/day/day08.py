#!/usr/bin/python

def init_forest(lines):
	forest = []

	for line in lines:
		row = [int(x) for x in line]
		forest.append(row)

	return forest

def is_visible(x, y, forest):
	tree_value = forest[x][y]
	max_width = len(forest[0])
	max_heigth = len(forest)

	visible = True

	# look from top
	for i in range(x - 1, -1, -1):
		if tree_value <= forest[i][y]:
			visible = False
			break

	if visible:
		return visible


	visible = True

	# look from bottom
	for i in range(x + 1, max_heigth):
		if tree_value <= forest[i][y]:
			visible = False
			break

	if visible:
		return visible

	visible = True

	# look from left
	for i in range(y - 1, -1, -1):
		if tree_value <= forest[x][i]:
			visible = False
			break

	if visible:
		return visible

	visible = True

	# look from right
	for i in range(y + 1, max_width):
		if tree_value <= forest[x][i]:
			visible = False
			break

	return visible

def get_scenic_score(x, y, forest):
	tree_value = forest[x][y]
	max_width = len(forest[0])
	max_heigth = len(forest)

	top = 0
	# look from top
	for i in range(x - 1, -1, -1):
		top += 1
		if tree_value <= forest[i][y]:
			break

	bottom = 0
	# look from bottom
	for i in range(x + 1, max_heigth):
		bottom += 1
		if tree_value <= forest[i][y]:
			break

	left = 0
	# look from left
	for i in range(y - 1, -1, -1):
		left += 1
		if tree_value <= forest[x][i]:
			break

	right = 0
	# look from right
	for i in range(y + 1, max_width):
		right += 1
		if tree_value <= forest[x][i]:
			break

	return top * bottom * right * left

def level1(input):
	#input = '30373\n25512\n65332\n33549\n35390\n'
	forest = init_forest(input.strip().split('\n'))
	count = len(forest) * 2 + (len(forest[0]) - 2) * 2

	for x in range(1, len(forest) - 1):
		for y in range(1, len(forest[0]) - 1):
			if is_visible(x, y, forest):
				count += 1

	return count

def level2(input):
	#input = '30373\n25512\n65332\n33549\n35390\n'
	forest = init_forest(input.strip().split('\n'))
	top_scenic = 0

	for x in range(1, len(forest) - 1):
		for y in range(1, len(forest[0]) - 1):
			top_scenic = max(top_scenic, get_scenic_score(x, y, forest))

	return top_scenic