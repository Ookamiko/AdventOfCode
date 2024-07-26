#!/usr/bin/python

def get_dist_from_origin(way):
	min_se_nw = min(way['se'], way['nw'])
	way['se'] -= min_se_nw
	way['nw'] -= min_se_nw

	min_sw_ne = min(way['sw'], way['ne'])
	way['sw'] -= min_sw_ne
	way['ne'] -= min_sw_ne

	min_sw_se = min(way['sw'], way['se'])
	way['sw'] -= min_sw_se
	way['se'] -= min_sw_se
	way['s'] += min_sw_se

	min_nw_ne = min(way['nw'], way['ne'])
	way['nw'] -= min_nw_ne
	way['ne'] -= min_nw_ne
	way['n'] += min_nw_ne

	min_n_s = min(way['n'], way['s'])
	way['n'] -= min_n_s
	way['s'] -= min_n_s

	if way['n'] != 0 and (way['se'] != 0 or way['sw'] != 0):
		if way['se'] != 0:
			tmp_min = min(way['n'], way['se'])
			way['n'] -= tmp_min
			way['se'] -= tmp_min
			way['ne'] += tmp_min
		else:
			tmp_min = min(way['n'], way['sw'])
			way['n'] -= tmp_min
			way['sw'] -= tmp_min
			way['nw'] += tmp_min

	elif way['s'] != 0 and (way['ne'] != 0 or way['nw'] != 0):
		if way['ne'] != 0:
			tmp_min = min(way['s'], way['ne'])
			way['s'] -= tmp_min
			way['ne'] -= tmp_min
			way['se'] += tmp_min
		else:
			tmp_min = min(way['s'], way['nw'])
			way['s'] -= tmp_min
			way['nw'] -= tmp_min
			way['sw'] += tmp_min

	return way['n'] + way['s'] + way['ne'] + way['nw'] + way['se'] + way['sw']

def level1(input):
	# Test value
	# input = 'ne,ne,s,s'
	path = input.strip().split(',')
	way = {
		'n': path.count('n'),
		's': path.count('s'),
		'ne': path.count('ne'),
		'nw': path.count('nw'),
		'se': path.count('se'),
		'sw': path.count('sw')
	}

	return get_dist_from_origin(way)

def level2(input):
	result = 0
	path = input.strip().split(',')
	way = {
		'n': 0,
		's': 0,
		'ne': 0,
		'nw': 0,
		'se': 0,
		'sw': 0
	}

	for current in path:
		way[current] += 1
		result = max(result, get_dist_from_origin(way))

	return result