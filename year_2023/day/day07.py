#!/usr/bin/python

def card_to_int(card):
	if card.isnumeric():
		return int(card)
	elif card == 'A':
		return 14
	elif card == 'K':
		return 13
	elif card == 'Q':
		return 12
	elif card == 'J':
		return 11
	elif card == 'T':
		return 10

def hand_to_int(hand, real_hand=''):
	if real_hand == '':
		real_hand = hand

	tmp_array = [x for x in hand]
	card_in_hand = list(set(tmp_array))
	value_hand = 10000000000

	if len(card_in_hand) == 1:
		value_hand *= 7
	elif len(card_in_hand) == 2:
		nbr_test = hand.count(card_in_hand[0])
		if nbr_test == 1 or nbr_test == 4:
			value_hand *= 6
		else:
			value_hand *= 5
	elif len(card_in_hand) == 3:
		nbr_1 = hand.count(card_in_hand[0])
		nbr_2 = hand.count(card_in_hand[1])
		nbr_3 = hand.count(card_in_hand[2])
		if nbr_1 == 3 or nbr_2 == 3 or nbr_3 == 3:
			value_hand *= 4
		else:
			value_hand *= 3
	elif len(card_in_hand) == 4:
		value_hand *= 2

	muli = 100000000

	for card in real_hand:
		value_hand += card_to_int(card) * muli
		muli /= 100

	return value_hand

def get_best_hand(hand):
	if not('J' in hand):
		return hand

	tmp_array = [x for x in hand.replace('J', '')]
	cards = sorted(list(set(tmp_array)), key=lambda x: hand.count(x))[::-1]

	if len(cards) == 0:
		cards.append('A')

	return hand.replace('J', cards[0])

def level1(input):
	# Test value
	# input = '32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483\n'
	games = []

	for current in input.strip().split('\n'):
		tmp = current.split(' ')
		games.append({'hand': hand_to_int(tmp[0]), 'bid': int(tmp[1])})

	games = sorted(games, key=lambda x: x['hand'])

	gain = 0

	for i in range(len(games)):
		gain += (i + 1) * games[i]['bid']

	return gain

def level2(input):
	# Test value
	# input = '32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483\n'
	games = []

	for current in input.strip().split('\n'):
		tmp = current.split(' ')
		best_hand = get_best_hand(tmp[0])
		games.append({'hand': hand_to_int(best_hand, tmp[0].replace('J', '1')), 'bid': int(tmp[1])})

	games = sorted(games, key=lambda x: x['hand'])

	gain = 0

	for i in range(len(games)):
		gain += (i + 1) * games[i]['bid']

	return gain