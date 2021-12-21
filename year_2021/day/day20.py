#!/usr/bin/python

import math

def DisplaySquare(square):
	size = int(math.sqrt(len(square)))
	for i in range(size):
		print(''.join(square[i * size: (i * size) + size]))

def IncreasePicture(picture, defaultChar='.'):
	baseSize = int(math.sqrt(len(picture)))
	newSize = baseSize + 4
	newPicture = []
	cursor = 0
	for i in range(newSize ** 2):
		if i < newSize * 2 or i >= (newSize ** 2) - newSize * 2 or i % newSize <= 1 or i % newSize >= newSize - 2:
			newPicture.append(defaultChar)
		else:
			newPicture.append(picture[cursor])
			cursor += 1
	return newPicture

def EnhancePicture(picture, algorithm):
	result = []
	size = int(math.sqrt(len(picture)))

	for i in range(len(picture)):
		if i < size or i >= (size ** 2) - size or i % size == 0 or i % size == size - 1:
			continue

		code = ''.join(picture[i-size-1:i-size+2] + picture[i-1:i+2] + picture[i+size-1:i+size+2])
		intCode = int(code.replace('.', '0').replace('#', '1'), 2)
		result.append(algorithm[intCode])

	return result 

def level1(input):
	#input = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#\n\n#..#.\n#....\n##..#\n..#..\n..###\n'
	instructions = input.strip().split('\n')
	algorithm = instructions[0]
	picture = list(''.join(instructions[2:]))
	for step in range(2):
		picture = IncreasePicture(picture, '.' if step % 2 == 0 else '#')
		picture = EnhancePicture(picture, algorithm)
	return picture.count('#')

def level2(input):
	#input = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#\n\n#..#.\n#....\n##..#\n..#..\n..###\n'
	instructions = input.strip().split('\n')
	algorithm = instructions[0]
	picture = list(''.join(instructions[2:]))
	for step in range(50):
		print('Step ' + str(step + 1))
		picture = IncreasePicture(picture, '.' if step % 2 == 0 else '#')
		picture = EnhancePicture(picture, algorithm)
	return picture.count('#')