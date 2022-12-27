#!/usr/bin/python

import re as regex
import sys

def log(string, file=False):
	print(string)
#	if file:
#		f = open("stats_19.log", "a")
#		f.write(string + '\n')
#		f.close()

def ordinal_state(step, r_ore, s_ore, r_clay, s_clay, r_obsi, s_obsi, r_geode, s_geode):
	return step + r_ore * (10 ** 2) + s_ore * (10 ** 4) + r_clay * (10 ** 6) + s_clay * (10 ** 8) + r_obsi * (10 ** 10) + s_obsi * (10 ** 12) + r_geode * (10 ** 14) + s_geode * (10 ** 16)

def get_max_opened_geode(blueprint, step, max_step, seen, r_ore, s_ore, r_clay=0, s_clay=0, r_obsi=0, s_obsi=0, r_geode=0, s_geode=0, prev_ore=False, prev_clay=False, prev_obsi=False, prev_geode=False):
	if step >= max_step:
		return s_geode

	if step <= max_step // 2:
		ord_state = ordinal_state(step, r_ore, s_ore, r_clay, s_clay, r_obsi, s_obsi, r_geode, s_geode)

		if ord_state in seen:
			log('\t' + str(step) + '\tQuit s\t\t' + str(len(seen)))
			return -1
		else:
			seen.append(ord_state)

	if blueprint['max_ore_need'] < r_ore:
		if step <= max_step // 2:
			log('\t' + str(step) + '\tQuit po\t\t' + str(len(seen)))
		return -1

	if blueprint['max_clay_need'] < r_clay:
		if step <= (max_step // 3) * 2:
			log('\t' + str(step) + '\tQuit pc\t\t' + str(len(seen)))
		return -1

	if blueprint['max_obsi_need'] < r_obsi:
		if step <= (max_step // 4) * 3:
			log('\t' + str(step) + '\tQuit pb\t\t' + str(len(seen)))
		return -1

	max_found = s_geode
	has_create_ore = prev_ore
	has_create_clay = prev_clay
	has_create_obsi = prev_obsi
	has_create_geode = prev_geode

	if s_ore >= blueprint['geode']['ore'] and s_obsi >= blueprint['geode']['obsi']:
		if not(prev_geode):
			if step <= max_step // 3:
				log(str(step) + '\tCreate geode\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)
			tmp_max = get_max_opened_geode(blueprint, step + 1, max_step, seen,
				r_ore, s_ore + r_ore - blueprint['geode']['ore'],
				r_clay, s_clay + r_clay,
				r_obsi, s_obsi + r_obsi - blueprint['geode']['obsi'],
				r_geode + 1, s_geode + r_geode)
			max_found = max(max_found, tmp_max)
			has_create_geode = True
	else:
		has_create_geode = False


	if s_ore >= blueprint['obsi']['ore'] and s_clay >= blueprint['obsi']['clay']:
		if not(prev_obsi):
			if step <= max_step // 3:
				log(str(step) + '\tCreate obsi\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)
			tmp_max = get_max_opened_geode(blueprint, step + 1, max_step, seen,
				r_ore, s_ore + r_ore - blueprint['obsi']['ore'],
				r_clay, s_clay + r_clay - blueprint['obsi']['clay'],
				r_obsi + 1, s_obsi + r_obsi,
				r_geode, s_geode + r_geode)
			max_found = max(max_found, tmp_max)
			has_create_obsi = True
	else:
		has_create_obsi = False

	if s_ore >= blueprint['clay']['ore']:
		if not(prev_clay):
			if step <= max_step // 3:
				log(str(step) + '\tCreate clay\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)
			tmp_max = get_max_opened_geode(blueprint, step + 1, max_step, seen,
				r_ore, s_ore + r_ore - blueprint['clay']['ore'],
				r_clay + 1, s_clay + r_clay,
				r_obsi, s_obsi + r_obsi,
				r_geode, s_geode + r_geode)
			max_found = max(max_found, tmp_max)
			has_create_clay = True
	else:
		has_create_clay = False

	if s_ore >= blueprint['ore']['ore']:
		if not(prev_ore):
			if step <= max_step // 3:
				log(str(step) + '\tCreate ore\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)
			tmp_max = get_max_opened_geode(blueprint, step + 1, max_step, seen,
				r_ore + 1, s_ore + r_ore - blueprint['ore']['ore'],
				r_clay, s_clay + r_clay,
				r_obsi, s_obsi + r_obsi,
				r_geode, s_geode + r_geode)
			max_found = max(max_found, tmp_max)
			has_create_ore = True
	else:
		has_create_ore = False

	if (not(step < 5 and has_create_ore and has_create_clay) and
	not(step < 13 and has_create_ore and has_create_clay and has_create_obsi) and
	not(step < 21 and has_create_ore and has_create_clay and has_create_obsi and has_create_geode)):
		if step <= max_step // 3:
			log(str(step) + '\tWait\t\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)
		tmp_max = get_max_opened_geode(blueprint, step + 1, max_step, seen,
			r_ore, s_ore + r_ore,
			r_clay, s_clay + r_clay,
			r_obsi, s_obsi + r_obsi,
			r_geode, s_geode + r_geode,
			has_create_ore, has_create_clay, has_create_obsi, has_create_geode)
		max_found = max(max_found, tmp_max)
	elif step <= max_step // 2:
		log(str(step) + '\tSkip wait\t' + str(max_found) + '\t' + str(len(seen)), step <= max_step // 5)

	return max_found


def level1(input):
	print('Exec long')
	sys.setrecursionlimit(10000)
	#input = 'Blueprint 1:Each ore robot costs 4 ore.Each clay robot costs 2 ore.Each obsidian robot costs 3 ore and 14 clay.Each geode robot costs 2 ore and 7 obsidian.\nBlueprint 2:Each ore robot costs 2 ore.Each clay robot costs 3 ore.Each obsidian robot costs 3 ore and 8 clay.Each geode robot costs 3 ore and 12 obsidian.\n'
	blueprints = []
	for line in input.strip().split('\n'):
		numbers = [int(x) for x in regex.findall(r'\d+', line)]
		blueprints.append(
			{
				'ore': {'ore': numbers[1], 'clay': 0, 'obsi': 0},
				'clay': {'ore': numbers[2], 'clay': 0, 'obsi': 0},
				'obsi': {'ore': numbers[3], 'clay': numbers[4], 'obsi': 0},
				'geode': {'ore': numbers[5], 'clay': 0, 'obsi': numbers[6]},
				'max_ore_need': max(numbers[2], numbers[3], numbers[5]),
				'max_clay_need': numbers[4],
				'max_obsi_need': numbers[6]
			}
		)

	result = 0
	for i in range(len(blueprints)):
		log("Blueprint " + str(i + 1), True)
		top = get_max_opened_geode(blueprints[i], 0, 24, [], 1, 0)
		log("Top\t" + str(top), True)
		result += top * (i + 1)
		log("-------------------", True)

	return result

def level2(input):
	print('Exec long')
	sys.setrecursionlimit(10000)
	#input = 'Blueprint 1:Each ore robot costs 4 ore.Each clay robot costs 2 ore.Each obsidian robot costs 3 ore and 14 clay.Each geode robot costs 2 ore and 7 obsidian.\nBlueprint 2:Each ore robot costs 2 ore.Each clay robot costs 3 ore.Each obsidian robot costs 3 ore and 8 clay.Each geode robot costs 3 ore and 12 obsidian.\n'
	blueprints = []
	for line in input.strip().split('\n'):
		numbers = [int(x) for x in regex.findall(r'\d+', line)]
		blueprints.append(
			{
				'ore': {'ore': numbers[1], 'clay': 0, 'obsi': 0},
				'clay': {'ore': numbers[2], 'clay': 0, 'obsi': 0},
				'obsi': {'ore': numbers[3], 'clay': numbers[4], 'obsi': 0},
				'geode': {'ore': numbers[5], 'clay': 0, 'obsi': numbers[6]},
				'max_ore_need': max(numbers[2], numbers[3], numbers[5]),
				'max_clay_need': numbers[4],
				'max_obsi_need': numbers[6]
			}
		)

	result = 1
	for i in range(min(len(blueprints), 3)):
		log("Blueprint " + str(i + 1), True)
		top = get_max_opened_geode(blueprints[i], 0, 32, [], 1, 0)
		log("Top\t" + str(top), True)
		result *= top
		log("-------------------", True)

	return result