#!/usr/bin/python

import re as regex

def CreateCulinaryValue(instructions):
	toReturn = {}
	reg = r'([A-Za-z]*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			toReturn[groups[0]] = {
				'capacity': int(groups[1]),
				'durability': int(groups[2]),
				'flavor': int(groups[3]),
				'texture': int(groups[4]),
				'calories': int(groups[5])
			}

	return toReturn

def CreateIngredientsList(instructions):
	toReturn = []
	reg = r'([A-Za-z]*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)'
	for current in instructions:
		matches = regex.match(reg, current)
		if matches:
			groups = matches.groups()
			toReturn.append(groups[0])

	return toReturn

def CalculTotalScore(culinaryValue, ingredients, spoonleft, currentValue):
	toReturn = 0
	if len(ingredients) == 1:
		tmpValues = {
			'capacity': currentValue['capacity'] + spoonleft * culinaryValue[ingredients[0]]['capacity'],
			'durability': currentValue['durability'] + spoonleft * culinaryValue[ingredients[0]]['durability'],
			'flavor': currentValue['flavor'] + spoonleft * culinaryValue[ingredients[0]]['flavor'],
			'texture': currentValue['texture'] + spoonleft * culinaryValue[ingredients[0]]['texture']
		}

		if tmpValues['capacity'] > 0 and tmpValues['durability'] > 0 and tmpValues['flavor'] > 0 and tmpValues['texture'] > 0:
			toReturn = tmpValues['capacity'] * tmpValues['durability'] * tmpValues['flavor'] * tmpValues['texture']
	else:
		for i in range(1, spoonleft + 1):
			sub = list(ingredients)
			currentIngredient = sub.pop()
			tmpValues = {
				'capacity': currentValue['capacity'] + i * culinaryValue[currentIngredient]['capacity'],
				'durability': currentValue['durability'] + i * culinaryValue[currentIngredient]['durability'],
				'flavor': currentValue['flavor'] + i * culinaryValue[currentIngredient]['flavor'],
				'texture': currentValue['texture'] + i * culinaryValue[currentIngredient]['texture']
			}
			tmpReturn = CalculTotalScore(culinaryValue, sub, spoonleft - i, tmpValues)
			toReturn = max(toReturn, tmpReturn)

	return toReturn

def CalculTotalScoreWithCalories(culinaryValue, ingredients, spoonleft, currentValue):
	toReturn = 0
	if len(ingredients) == 1:
		tmpValues = {
			'capacity': currentValue['capacity'] + spoonleft * culinaryValue[ingredients[0]]['capacity'],
			'durability': currentValue['durability'] + spoonleft * culinaryValue[ingredients[0]]['durability'],
			'flavor': currentValue['flavor'] + spoonleft * culinaryValue[ingredients[0]]['flavor'],
			'texture': currentValue['texture'] + spoonleft * culinaryValue[ingredients[0]]['texture'],
			'calories': currentValue['calories'] + spoonleft * culinaryValue[ingredients[0]]['calories']
		}

		if tmpValues['capacity'] > 0 and tmpValues['durability'] > 0 and tmpValues['flavor'] > 0 and tmpValues['texture'] > 0 and tmpValues['calories'] == 500:
			toReturn = tmpValues['capacity'] * tmpValues['durability'] * tmpValues['flavor'] * tmpValues['texture']
	else:
		for i in range(1, spoonleft + 1):
			sub = list(ingredients)
			currentIngredient = sub.pop()
			tmpValues = {
				'capacity': currentValue['capacity'] + i * culinaryValue[currentIngredient]['capacity'],
				'durability': currentValue['durability'] + i * culinaryValue[currentIngredient]['durability'],
				'flavor': currentValue['flavor'] + i * culinaryValue[currentIngredient]['flavor'],
				'texture': currentValue['texture'] + i * culinaryValue[currentIngredient]['texture'],
				'calories': currentValue['calories'] + i * culinaryValue[currentIngredient]['calories']
			}
			tmpReturn = CalculTotalScoreWithCalories(culinaryValue, sub, spoonleft - i, tmpValues)
			toReturn = max(toReturn, tmpReturn)

	return toReturn

def level1(input):
	culinaryValue = CreateCulinaryValue(input.strip().split('\n'))
	ingredients = CreateIngredientsList(input.strip().split('\n'))
	defaultValue = {
		'capacity': 0,
		'durability': 0,
		'flavor': 0,
		'texture': 0
	}
	return CalculTotalScore(culinaryValue, ingredients, 100, defaultValue)

def level2(input):
	culinaryValue = CreateCulinaryValue(input.strip().split('\n'))
	ingredients = CreateIngredientsList(input.strip().split('\n'))
	defaultValue = {
		'capacity': 0,
		'durability': 0,
		'flavor': 0,
		'texture': 0,
		'calories': 0
	}
	return CalculTotalScoreWithCalories(culinaryValue, ingredients, 100, defaultValue)