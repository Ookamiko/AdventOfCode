#!/usr/bin/python

from datetime import datetime
import re as regex

def get_most_asleep(guard_dict):
	max_asleep = 0
	guard_id = 0

	for key in guard_dict.keys():
		if guard_dict[key]['sum'] > max_asleep:
			max_asleep = guard_dict[key]['sum']
			guard_id = key

	return guard_id

def get_most_minute_asleep(guard):
	max_asleep = 0
	minute = 0

	for i in range(0, 60):
		if guard['minutes'][i] > max_asleep:
			max_asleep = guard['minutes'][i]
			minute = i

	return minute

def get_most_asleep_guard_minute(minutes):
	max_asleep = 0
	guard_id = 0
	minute = 0

	for i in range(0, 60):
		for key in minutes[i].keys():
			if minutes[i][key] > max_asleep:
				guard_id = key
				minute = i
				max_asleep = minutes[i][key]

	return guard_id, minute

def level1(input):
	#input = '[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up\n'
	shift = input.strip().split('\n')
	shift.sort(key=lambda x: datetime.strptime(
		regex.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', x)[0], '%Y-%m-%d %H:%M')
	)

	guards = {}
	guard_id = 0
	start = -1
	end = -1

	for current in shift:
		re_id = regex.search(r'#(\d+)', current)

		if re_id:
			guard_id = int(re_id[0][1:])
			start = -1
			end = -1

			if not(guard_id in guards.keys()):
				guards[guard_id] = { 'minutes': [0] * 60, 'sum': 0 }

		elif current[19:] == 'wakes up':
			end = int(current[15:17])

			guards[guard_id]['sum'] += end - start

			for i in range(start, end):
				guards[guard_id]['minutes'][i] += 1
		else:
			start = int(current[15:17])

	gid = get_most_asleep(guards)
	minute = get_most_minute_asleep(guards[gid])

	return gid * minute

def level2(input):
	#input = '[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up\n'
	shift = input.strip().split('\n')
	shift.sort(key=lambda x: datetime.strptime(
		regex.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', x)[0], '%Y-%m-%d %H:%M')
	)

	minutes = []
	for i in range(60):
		minutes.append({})
	know_guard = []
	guard_id = 0
	start = -1
	end = -1

	for current in shift:
		re_id = regex.search(r'#(\d+)', current)

		if re_id:
			guard_id = int(re_id[0][1:])
			start = -1
			end = -1

			if not(guard_id in know_guard):
				know_guard.append(guard_id)
				for minute in minutes:
					minute[guard_id] = 0

		elif current[19:] == 'wakes up':
			end = int(current[15:17])

			for i in range(start, end):
				minutes[i][guard_id] += 1
		else:
			start = int(current[15:17])

	guard_id, minute = get_most_asleep_guard_minute(minutes)

	return guard_id * minute