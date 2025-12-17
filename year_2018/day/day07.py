#!/usr/bin/python

import re as regex
import math

def create_plan(instructions, time_added=60):

	plan = {}

	for line in instructions:
		m = regex.match(r'^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$', line)

		first = m.group(1)
		second = m.group(2)

		if not(first in plan.keys()):
			plan[first] = {
				'required': 0,
				'unlock': [second],
				'time': ord(first) - 64 + time_added
			}
		else:
			plan[first]['unlock'].append(second)

		if not(second in plan.keys()):
			plan[second] = {
				'required': 1,
				'unlock': [],
				'time': ord(second) - 64 + time_added
			}
		else:
			plan[second]['required'] += 1

	return plan


def level1(input):
	#input = 'Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin.\n'

	plan = create_plan(input.strip().split('\n'))

	to_proceed = []
	result = ''

	for key, value in plan.items():
		if value['required'] == 0:
			to_proceed.append(key)

	while len(to_proceed) > 0:
		print('-----')
		print(to_proceed)
		to_proceed.sort()
		print(to_proceed)

		key = to_proceed.pop(0)
		result += key

		for next_key in plan[key]['unlock']:
			plan[next_key]['required'] -= 1

			if plan[next_key]['required'] == 0:
				to_proceed.append(next_key)

	return result

def level2(input):
	#input = 'Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin.\n'
	#nbr_worker = 2
	#adding_time = 0

	nbr_worker = 5
	adding_time = 60

	plan = create_plan(input.strip().split('\n'), adding_time)

	to_proceed = []
	result = 0

	for key, value in plan.items():
		if value['required'] == 0:
			to_proceed.append(key)

	working_on = []

	while len(to_proceed) > 0 or len(working_on) > 0:

		# reorder next step
		to_proceed.sort()

		print('----')
		print(f"p:{to_proceed}")
		print(f"w:{working_on}")

		# define task for elf
		task_to_take = nbr_worker - len(working_on)
		working_on += to_proceed[:task_to_take]
		to_proceed = to_proceed[task_to_take:]

		# define minimum time/task
		min_time = math.inf
		min_key = ''

		for key in working_on:
			if plan[key]['time'] < min_time:
				min_time = plan[key]['time']
				min_key = key
			elif plan[key]['time'] == min_time:
				print(f"e:{min_time}")
		print(min_time)

		# reduce working time by min time
		for key in working_on:
			plan[key]['time'] -= min_time

		# add time taken, remove completed from working
		# and watch next to proceed
		result += min_time
		working_on.remove(min_key)

		for next_key in plan[min_key]['unlock']:
			plan[next_key]['required'] -= 1

			if plan[next_key]['required'] == 0:
				to_proceed.append(next_key)


	return result