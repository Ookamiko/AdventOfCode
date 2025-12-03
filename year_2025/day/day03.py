#!/usr/bin/python

def get_max_joltage(bank, nbr):
	if nbr == 0:
		return 0

	max_found = max(bank[:len(bank) - (nbr - 1)])
	index_max = bank.index(max_found)

	return max_found * pow(10, nbr - 1) + get_max_joltage(bank[index_max + 1:], nbr - 1)

def level1(input):
	#input = '987654321111111\n811111111111119\n234234234234278\n818181911112111\n'

	result = 0

	for bank_str in input.strip().split('\n'):
		bank = [int(x) for x in bank_str]

		max_joltage = get_max_joltage(bank, 2)

		result += max_joltage

	return result

def level2(input):
	#input = '987654321111111\n811111111111119\n234234234234278\n818181911112111\n'

	result = 0
	i = 0

	for bank_str in input.strip().split('\n'):
		bank = [int(x) for x in bank_str]

		i += 1
		print(f"Bank {i}")

		max_joltage = get_max_joltage(bank, 12)

		result += max_joltage

	return result