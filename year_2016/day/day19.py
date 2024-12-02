#!/usr/bin/python

def level1(input):
	participants = int(input.strip())
	participants = 13
	indice = 1
	cycle = 1
	while participants > 1:
		if participants % 2 != 0:
			indice += 2 ** cycle
		cycle += 1
		participants = participants // 2

	return indice


## Solution from https://oeis.org/A334473 (Josephus problem)
def highest_power_of_3(n):
    option = 0
    while 3**option <= n:
        option +=1
    return 3 ** (option -1)

def answer(n):
    x = highest_power_of_3(n)
    if x == n:
        return x
    else:
        if n < 2 * x:
            return n%x
        else:
            return x + 2 * (n%x)

def level2(input):
	return answer(int(input.strip()))