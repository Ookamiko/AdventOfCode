#!/usr/bin/python
import sys
import datetime

import adventofcode

try:
	if int(sys.argv[1]) < 2015:
		sys.exit("Year defined must be greater or equals to 2015.")

	if int(sys.argv[2]) not in range(1,26):
		sys.exit("Day defined must be a value between '1' and '25' inclusive.")

	if int(sys.argv[3]) not in [1,2]:
		sys.exit("Level defined must be either '1' or '2'")
except Exception as e:
	sys.exit("Method not called properly. " +
		"main.py [year (20xx)] [day (1-25)] [level (1..2)] expected.")

year = str(sys.argv[1])
day = str(sys.argv[2])
level = str(sys.argv[3])

print("Retrieving input for problem " + year + "-" + day + "-" + level + ".")

input = adventofcode.get_input(year, day)

start = datetime.datetime.now()
print("Start execution for problem " + year + "-" + day + "-" + level + ".")

print("Solution : " + str(adventofcode.solve(year, day, level, input)))

print("Executed in " + str((datetime.datetime.now() - start).total_seconds()) + "s")