#!/usr/bin/python

import math

def found_border(poly, low, up):
	if low == 0 or up == len(poly) - 1:
		return low, up

	if poly[low - 1] != poly[up + 1] and poly[low - 1].lower() == poly[up + 1].lower():
		return found_border(poly, low - 1, up + 1)
	else:
		return low, up

def reduce_poly(poly):
	i = 0

	while i < len(poly) - 1:

		if poly[i] != poly[i + 1] and poly[i].lower() == poly[i + 1].lower():
			low, up = found_border(poly, i, i + 1)
			poly = poly[:low] + poly[up+1:]
			i = low
		else:
			i += 1

	return poly

def level1(input):
	#input = 'dabAcCaCBAcCcaDA\n'
	poly = input.strip()

	return len(reduce_poly(poly))

def level2(input):
	#input = 'dabAcCaCBAcCcaDA\n'
	units = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']
	poly = input.strip()

	best = math.inf

	for unit in units:
		if not(unit in poly or unit.upper() in poly):
			continue

		test_poly = poly.replace(unit, '').replace(unit.upper(), '')
		r_poly = reduce_poly(test_poly)

		best = min(best, len(r_poly))

	return best