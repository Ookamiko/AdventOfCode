#!/usr/bin/python

def dijkstra(city, size_y, start, end, min_step, max_step):
	pos = start
	direction = 0
	heat_loss = 0
	queue = {}
	visited = ['0/1', '0/-1', '0/' + str(size_y), '0/-' + str(size_y)]

	while pos != end:
		visited.append(str(pos) + '/' + str(direction))

		if abs(direction) != size_y:
			tmp_heat_loss = heat_loss
			for i in range(1, max_step + 1):
				tmp_pos = pos + (i * size_y)
				if tmp_pos >= len(city): break

				tmp_heat_loss += city[tmp_pos]
				if i < min_step: continue
				index = str(tmp_pos) + '/' + str(size_y)

				if not(index in visited):
					if not(index in queue) or tmp_heat_loss < queue[index]:
						queue[index] = tmp_heat_loss

			tmp_heat_loss = heat_loss
			for i in range(1, max_step + 1):
				tmp_pos = pos - (i * size_y)
				if tmp_pos < 0: break

				tmp_heat_loss += city[tmp_pos]
				if i < min_step: continue

				index = str(tmp_pos) + '/' + str(-1 * size_y)

				if not(index in visited):
					if not(index in queue) or tmp_heat_loss < queue[index]:
						queue[index] = tmp_heat_loss

		if abs(direction) != 1:
			tmp_heat_loss = heat_loss
			for i in range(1, max_step + 1):
				tmp_pos = pos + i
				if tmp_pos % size_y == 0: break

				tmp_heat_loss += city[tmp_pos]
				if i < min_step: continue

				index = str(tmp_pos) + '/' + str(1)

				if not(index in visited):
					if not(index in queue) or tmp_heat_loss < queue[index]:
						queue[index] = tmp_heat_loss

			tmp_heat_loss = heat_loss
			for i in range(1, max_step + 1):
				tmp_pos = pos - i
				if tmp_pos % size_y == size_y - 1: break

				tmp_heat_loss += city[tmp_pos]
				if i < min_step: continue

				index = str(tmp_pos) + '/' + str(-1)

				if not(index in visited):
					if not(index in queue) or tmp_heat_loss < queue[index]:
						queue[index] = tmp_heat_loss

		if len(queue.items()) == 0:
			break

		item_queue = sorted(queue.items(), key=lambda x: x[1])

		next_pos = item_queue.pop(0)
		tmp = [int(x) for x in next_pos[0].split('/')]
		pos = tmp[0]
		direction = tmp[1]
		heat_loss = next_pos[1]

		queue = dict(item_queue)

	return heat_loss


def level1(input):
	# Test value
	# input = '2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533\n'
	# input = '2413\n3215\n3255\n3446\n'
	print('Exec long')
	tmp = input.strip().split('\n')
	size_y = len(tmp[0])
	city = [int(x) for x in ''.join(tmp)]
	max_heat = sum(city) + 1

	return dijkstra(city, size_y, 0, len(city) - 1, 0, 3)

def level2(input):
	# Test value
	# input = '2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533\n'
	# input = '111111111111\n999999999991\n999999999991\n999999999991\n999999999991\n'
	# Plus petit que 812
	print('Exec long')
	tmp = input.strip().split('\n')
	size_y = len(tmp[0])
	city = [int(x) for x in ''.join(tmp)]

	return dijkstra(city, size_y, 0, len(city) - 1, 4, 10)