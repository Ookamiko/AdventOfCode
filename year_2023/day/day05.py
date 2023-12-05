#!/usr/bin/python

import re as regex

def create_map_road(lines):
	result = []
	current_map = []

	for line in lines:
		if line == '':
			current_map = sorted(current_map, key=lambda x: x['ss'])
			result.append(current_map)
			current_map = []
		elif line[0].isnumeric():
			tmp = line.split(' ')
			current_map.append({'sd': int(tmp[0]), 'ss': int(tmp[1]), 'es': int(tmp[1]) + int(tmp[2]) - 1})

	current_map = sorted(current_map, key=lambda x: x['ss'])
	result.append(current_map)

	return result

def next_pos(source, roads_map):
	result = source

	for road in roads_map:
		if source >= road['ss'] and source <= road['es']:
			result = road['sd'] + (source - road['ss'])
			break

	return result


def next_pos_advance(source, roads_map):
	result = []
	current_start = source['s']
	end = source['e']

	for road in roads_map:

		if road['es'] < current_start:
			continue

		elif road['ss'] > end:
			break

		elif road['ss'] <= current_start and road['es'] <= end:
			low_diff = current_start - road['ss']
			up_diff = road['es'] - road['ss']
			result.append({'s': road['sd'] + low_diff, 'e': road['sd'] + up_diff})

		elif road['ss'] > current_start and road['ss'] < end and road['es'] <= end:
			result.append({'s': current_start, 'e': road['ss'] - 1})

			up_diff = road['es'] - road['ss']
			result.append({'s': road['sd'], 'e': road['sd'] + up_diff})

		elif road['ss'] > current_start and road['ss'] <= end and road['es'] > end:
			if current_start < road['ss']:
				result.append({'s': current_start, 'e': road['ss'] - 1})

			diff = end - road['ss']
			result.append({'s': road['sd'], 'e': road['sd'] + diff})

		else:
			low_diff = current_start - road['ss']
			up_diff = end - road['ss']
			result.append({'s': road['sd'] + low_diff, 'e': road['sd'] + up_diff})

		current_start = road['es'] + 1
		if current_start > end:
			break

	if current_start <= end:
		result.append({'s': current_start, 'e': end})

	return result

def link_adjacent(source):
	sorted_source = sorted(source, key=lambda x: x['s'])
	result = [sorted_source[0]]

	for current in sorted_source[1:]:
		if result[-1]['e'] + 1 == current['s']:
			result[-1]['e'] = current['s']
		else:
			result.append(current)

	return result

def level1(input):
	# Test value
	# input = 'seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4\n'
	lines = input.strip().split('\n')
	seeds = [int(x) for x in regex.findall(r'\d+', lines[0])]

	all_road = create_map_road(lines[2:])

	for road in all_road:
		for i in range(len(seeds)):
			seeds[i] = next_pos(seeds[i], road)

	return min(seeds)

def level2(input):
	# Test value
	# input = 'seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4\n'
	lines = input.strip().split('\n')
	seeds = []
	nbrs = [int(x) for x in regex.findall(r'\d+', lines[0])]

	for i in range(0, len(nbrs), 2):
		seeds.append({'s': nbrs[i], 'e': nbrs[i] + (nbrs[i + 1] - 1)})

	seeds = link_adjacent(seeds)
	all_road = create_map_road(lines[2:])

	for road in all_road:
		new_seeds = []
		for current in seeds:
			new_seeds += next_pos_advance(current, road)

		seeds = link_adjacent(new_seeds)

	return seeds[0]['s']