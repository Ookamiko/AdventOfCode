#!/usr/bin/python

from .day import *

def default(input):
	return "No function define for day/level passed as argument"

def get_solve_function(day, level):
	fct = default

	if day == "1":
		if level == "1":
			fct = day01.level1
		elif level == "2":
			fct = day01.level2
	elif day == "2":
		if level == "1":
			fct = day02.level1
		elif level == "2":
			fct = day02.level2
	elif day == "3":
		if level == "1":
			fct = day03.level1
		elif level == "2":
			fct = day03.level2
	elif day == "4":
		if level == "1":
			fct = day04.level1
		elif level == "2":
			fct = day04.level2
	elif day == "5":
		if level == "1":
			fct = day05.level1
		elif level == "2":
			fct = day05.level2
	elif day == "6":
		if level == "1":
			fct = day06.level1
		elif level == "2":
			fct = day06.level2
	elif day == "7":
		if level == "1":
			fct = day07.level1
		elif level == "2":
			fct = day07.level2
	elif day == "8":
		if level == "1":
			fct = day08.level1
		elif level == "2":
			fct = day08.level2
	elif day == "9":
		if level == "1":
			fct = day09.level1
		elif level == "2":
			fct = day09.level2
	elif day == "10":
		if level == "1":
			fct = day10.level1
		elif level == "2":
			fct = day10.level2
	elif day == "11":
		if level == "1":
			fct = day11.level1
		elif level == "2":
			fct = day11.level2
	elif day == "12":
		if level == "1":
			fct = day12.level1
		elif level == "2":
			fct = day12.level2
	elif day == "13":
		if level == "1":
			fct = day13.level1
		elif level == "2":
			fct = day13.level2
	elif day == "14":
		if level == "1":
			fct = day14.level1
		elif level == "2":
			fct = day14.level2
	elif day == "15":
		if level == "1":
			fct = day15.level1
		elif level == "2":
			fct = day15.level2
	elif day == "16":
		if level == "1":
			fct = day16.level1
		elif level == "2":
			fct = day16.level2
	elif day == "17":
		if level == "1":
			fct = day17.level1
		elif level == "2":
			fct = day17.level2
	elif day == "18":
		if level == "1":
			fct = day18.level1
		elif level == "2":
			fct = day18.level2
	elif day == "19":
		if level == "1":
			fct = day19.level1
		elif level == "2":
			fct = day19.level2
	elif day == "20":
		if level == "1":
			fct = day20.level1
		elif level == "2":
			fct = day20.level2
	elif day == "21":
		if level == "1":
			fct = day21.level1
		elif level == "2":
			fct = day21.level2
	elif day == "22":
		if level == "1":
			fct = day22.level1
		elif level == "2":
			fct = day22.level2
	elif day == "23":
		if level == "1":
			fct = day23.level1
		elif level == "2":
			fct = day23.level2
	elif day == "24":
		if level == "1":
			fct = day24.level1
		elif level == "2":
			fct = day24.level2
	elif day == "25":
		if level == "1":
			fct = day25.level1
		elif level == "2":
			fct = day25.level2

	return fct