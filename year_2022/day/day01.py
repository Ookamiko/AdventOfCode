#!/usr/bin/python

def level1(input):
	food_list = input.strip().split('\n')
	max_food = 0
	tmp_food = 0

	for food in food_list:
		if food == '':
			max_food = max(max_food, tmp_food)
			tmp_food = 0
		else:
			tmp_food += int(food)

	return max_food

def level2(input):
	food_list = input.strip().split('\n')
	all_foods = []
	tmp_food = 0

	for food in food_list:
		if food == '':
			all_foods.append(tmp_food)
			tmp_food = 0
		else:
			tmp_food += int(food)

	all_foods.sort(reverse=True)

	return all_foods[0] + all_foods[1] + all_foods[2]