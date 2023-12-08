#!/usr/bin/python

import re as regex
import math

def manhattan_dist(pos):
	return abs(pos[0]) + abs(pos[1]) + abs(pos[2])

def stringify_pos(pos):
	return str(pos[0]) + ',' + str(pos[1]) + ',' + str(pos[2])

def remove_collide(particules):
	pos_strs = {}

	for particule in particules:
		pos = stringify_pos(particule['pos'])
		if not(pos in pos_strs):
			pos_strs[pos] = []

		pos_strs[pos].append(particule['id'])

	to_remove = []

	for key in pos_strs.keys():
		tmp = pos_strs[key]
		if len(tmp) > 1:
			to_remove += tmp

	to_return = []
	for particule in particules:
		if not(particule['id'] in to_remove):
			to_return.append(particule)

	return to_return


def level1(input):
	# Test value
	# input = 'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>\np=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>\n'
	tmp = input.strip().split('\n')
	particules = []

	for i in range(len(tmp)):
		nbrs = regex.findall(r'-?\d+', tmp[i])
		particules.append({
			'id': i,
			'pos': [int(nbrs[0]), int(nbrs[1]), int(nbrs[2])],
			'vel': [int(nbrs[3]), int(nbrs[4]), int(nbrs[5])],
			'acc': [int(nbrs[6]), int(nbrs[7]), int(nbrs[8])],
			})

	while len(particules) > 1:
		for i in range(100):
			for particule in particules:
				particule['vel'][0] += particule['acc'][0]
				particule['vel'][1] += particule['acc'][1]
				particule['vel'][2] += particule['acc'][2]
				particule['pos'][0] += particule['vel'][0]
				particule['pos'][1] += particule['vel'][1]
				particule['pos'][2] += particule['vel'][2]

		particules = sorted(particules, key=lambda x: manhattan_dist(x['pos']))
		particules = particules[:math.ceil(len(particules) / 2)]

	return particules[0]['id']

def level2(input):
	# Test value
	# input = 'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\np=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>\n'
	tmp = input.strip().split('\n')
	particules = []

	for i in range(len(tmp)):
		nbrs = regex.findall(r'-?\d+', tmp[i])
		particules.append({
			'id': i,
			'pos': [int(nbrs[0]), int(nbrs[1]), int(nbrs[2])],
			'vel': [int(nbrs[3]), int(nbrs[4]), int(nbrs[5])],
			'acc': [int(nbrs[6]), int(nbrs[7]), int(nbrs[8])],
			})

	no_collide = 0

	while no_collide < 1000 and len(particules) > 1:
		no_collide += 1

		for particule in particules:
			particule['vel'][0] += particule['acc'][0]
			particule['vel'][1] += particule['acc'][1]
			particule['vel'][2] += particule['acc'][2]
			particule['pos'][0] += particule['vel'][0]
			particule['pos'][1] += particule['vel'][1]
			particule['pos'][2] += particule['vel'][2]

		test_collide = len(particules)
		particules = remove_collide(particules)

		if test_collide != len(particules):
			no_collide = 0

	return len(particules)