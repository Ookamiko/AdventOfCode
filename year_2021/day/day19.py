#!/usr/bin/python

HACK = ['scanner 5','scanner 11','scanner 20','scanner 18','scanner 4','scanner 7','scanner 12','scanner 13','scanner 3','scanner 10','scanner 14','scanner 15','scanner 16','scanner 1','scanner 2','scanner 17','scanner 22','scanner 26','scanner 27','scanner 6','scanner 28','scanner 30','scanner 8','scanner 31','scanner 32','scanner 19','scanner 23','scanner 24','scanner 33','scanner 34','scanner 35','scanner 9','scanner 25','scanner 29','scanner 21']

def SetRelative(scanner):
	for probe1 in scanner.keys():
		for probe2 in scanner.keys():
			if probe1 == probe2:
				continue

			if not('relative' in scanner[probe1].keys()):
				scanner[probe1]['relative'] = {}
			if not(probe2 in scanner[probe1]['relative'].keys()):
				scanner[probe1]['relative'][probe2] = {}
			scanner[probe1]['relative'][probe2]['x'] = scanner[probe2]['x'] - scanner[probe1]['x']
			scanner[probe1]['relative'][probe2]['y'] = scanner[probe2]['y'] - scanner[probe1]['y']
			scanner[probe1]['relative'][probe2]['z'] = scanner[probe2]['z'] - scanner[probe1]['z']

def IsSameRelativeDistance(probe1, probe2):
	return abs(probe1['x']) + abs(probe1['y']) + abs(probe1['z']) == abs(probe2['x']) + abs(probe2['y']) + abs(probe2['z']) and (abs(probe1['x']) == abs(probe2['x']) or abs(probe1['x']) == abs(probe2['y']) or abs(probe1['x']) == abs(probe2['z'])) and (abs(probe1['y']) == abs(probe2['x']) or abs(probe1['y']) == abs(probe2['y']) or abs(probe1['y']) == abs(probe2['z']))

def GetMatching(baseScanner, testScanner):
	result = {}
	for baseProbe in baseScanner.keys():
		for testProbe in testScanner.keys():
			result = {'matching': [baseProbe, testProbe], 'found': []}
			testMade = 0
			for testRelative in testScanner[testProbe]['relative'].keys():
				for baseRelative in list(baseScanner[baseProbe]['relative'].keys())[::-1]:
					if IsSameRelativeDistance(baseScanner[baseProbe]['relative'][baseRelative], testScanner[testProbe]['relative'][testRelative]):
						result['found'].append([baseRelative, testRelative])
						break
				testMade += 1
				if testMade + 11 - len(result['found']) > len(testScanner[testProbe]['relative'].keys()):
					break
			if len(result['found']) >= 11:
				return result
	return False

def InitialState(instructions):
	result = {}
	currentScanner = instructions[0].replace('-', '').strip()
	result[currentScanner] = {}
	i = 1
	while i < len(instructions):
		if instructions[i] == '':
			i += 1
			currentScanner = instructions[i].replace('-', '').strip()
			result[currentScanner] = {}
		else:
			coords = instructions[i].split(',')
			result[currentScanner]['probe ' + str(i)] = {'x': int(coords[0]), 'y': int(coords[1]), 'z': int(coords[2])}
		i += 1

	return result

def CorrectModifier(modifier, probe1, probe2):
	result = True
	for case in modifier:
		result &= probe1[case] == probe2[modifier[case]['case']] * modifier[case]['modif']

	return result

def FindModifiers(baseScanner, testScanner, matching):
	ALLMODIFIER = [{'x':{'case':'x','modif':1},'y':{'case':'y','modif':1},'z':{'case':'z','modif':1}},{'x':{'case':'x','modif':1},'y':{'case':'z','modif':1},'z':{'case':'y','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'x','modif':1},'z':{'case':'z','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'z','modif':1},'z':{'case':'x','modif':1}},{'x':{'case':'z','modif':1},'y':{'case':'x','modif':1},'z':{'case':'y','modif':1}},{'x':{'case':'z','modif':1},'y':{'case':'y','modif':1},'z':{'case':'x','modif':1}},{'x':{'case':'x','modif':-1},'y':{'case':'y','modif':1},'z':{'case':'z','modif':1}},{'x':{'case':'x','modif':-1},'y':{'case':'z','modif':1},'z':{'case':'y','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'x','modif':-1},'z':{'case':'z','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'z','modif':1},'z':{'case':'x','modif':-1}},{'x':{'case':'z','modif':1},'y':{'case':'x','modif':-1},'z':{'case':'y','modif':1}},{'x':{'case':'z','modif':1},'y':{'case':'y','modif':1},'z':{'case':'x','modif':-1}},{'x':{'case':'x','modif':1},'y':{'case':'y','modif':-1},'z':{'case':'z','modif':1}},{'x':{'case':'x','modif':1},'y':{'case':'z','modif':1},'z':{'case':'y','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'x','modif':1},'z':{'case':'z','modif':1}},{'x':{'case':'y','modif':-1},'y':{'case':'z','modif':1},'z':{'case':'x','modif':1}},{'x':{'case':'z','modif':1},'y':{'case':'x','modif':1},'z':{'case':'y','modif':-1}},{'x':{'case':'z','modif':1},'y':{'case':'y','modif':-1},'z':{'case':'x','modif':1}},{'x':{'case':'x','modif':1},'y':{'case':'y','modif':1},'z':{'case':'z','modif':-1}},{'x':{'case':'x','modif':1},'y':{'case':'z','modif':-1},'z':{'case':'y','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'x','modif':1},'z':{'case':'z','modif':-1}},{'x':{'case':'y','modif':1},'y':{'case':'z','modif':-1},'z':{'case':'x','modif':1}},{'x':{'case':'z','modif':-1},'y':{'case':'x','modif':1},'z':{'case':'y','modif':1}},{'x':{'case':'z','modif':-1},'y':{'case':'y','modif':1},'z':{'case':'x','modif':1}},{'x':{'case':'x','modif':-1},'y':{'case':'y','modif':-1},'z':{'case':'z','modif':1}},{'x':{'case':'x','modif':-1},'y':{'case':'z','modif':1},'z':{'case':'y','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'x','modif':-1},'z':{'case':'z','modif':1}},{'x':{'case':'y','modif':-1},'y':{'case':'z','modif':1},'z':{'case':'x','modif':-1}},{'x':{'case':'z','modif':1},'y':{'case':'x','modif':-1},'z':{'case':'y','modif':-1}},{'x':{'case':'z','modif':1},'y':{'case':'y','modif':-1},'z':{'case':'x','modif':-1}},{'x':{'case':'x','modif':-1},'y':{'case':'y','modif':1},'z':{'case':'z','modif':-1}},{'x':{'case':'x','modif':-1},'y':{'case':'z','modif':-1},'z':{'case':'y','modif':1}},{'x':{'case':'y','modif':1},'y':{'case':'x','modif':-1},'z':{'case':'z','modif':-1}},{'x':{'case':'y','modif':1},'y':{'case':'z','modif':-1},'z':{'case':'x','modif':-1}},{'x':{'case':'z','modif':-1},'y':{'case':'x','modif':-1},'z':{'case':'y','modif':1}},{'x':{'case':'z','modif':-1},'y':{'case':'y','modif':1},'z':{'case':'x','modif':-1}},{'x':{'case':'x','modif':1},'y':{'case':'y','modif':-1},'z':{'case':'z','modif':-1}},{'x':{'case':'x','modif':1},'y':{'case':'z','modif':-1},'z':{'case':'y','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'x','modif':1},'z':{'case':'z','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'z','modif':-1},'z':{'case':'x','modif':1}},{'x':{'case':'z','modif':-1},'y':{'case':'x','modif':1},'z':{'case':'y','modif':-1}},{'x':{'case':'z','modif':-1},'y':{'case':'y','modif':-1},'z':{'case':'x','modif':1}},{'x':{'case':'x','modif':-1},'y':{'case':'y','modif':-1},'z':{'case':'z','modif':-1}},{'x':{'case':'x','modif':-1},'y':{'case':'z','modif':-1},'z':{'case':'y','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'x','modif':-1},'z':{'case':'z','modif':-1}},{'x':{'case':'y','modif':-1},'y':{'case':'z','modif':-1},'z':{'case':'x','modif':-1}},{'x':{'case':'z','modif':-1},'y':{'case':'x','modif':-1},'z':{'case':'y','modif':-1}},{'x':{'case':'z','modif':-1},'y':{'case':'y','modif':-1},'z':{'case':'x','modif':-1}}]
	modifier = {}

	baseProbe = matching['matching'][0]
	testProbe = matching['matching'][1]

	for test in ALLMODIFIER:
		found = True
		for baseRelative, testRelative in matching['found']:
			if not(CorrectModifier(test, baseScanner[baseProbe]['relative'][baseRelative], testScanner[testProbe]['relative'][testRelative])):
				found = False
				break

		if found:
			modifier = test
			break

	return modifier

def IncrementProbe(baseScanner, baseProbe, relatives, modifier):
	for probe in relatives.keys():
		baseScanner[probe] = {}
		baseScanner[probe]['x'] = baseScanner[baseProbe]['x'] + (relatives[probe][modifier['x']['case']] * modifier['x']['modif'])
		baseScanner[probe]['y'] = baseScanner[baseProbe]['y'] + (relatives[probe][modifier['y']['case']] * modifier['y']['modif'])
		baseScanner[probe]['z'] = baseScanner[baseProbe]['z'] + (relatives[probe][modifier['z']['case']] * modifier['z']['modif'])

	SetRelative(baseScanner)

def GetPositionScanner(probe1, probe2, modifier):
	position = {}
	position['x'] = (probe2[modifier['x']['case']] - probe1['x'] * modifier['x']['modif']) * (-1 * modifier['x']['modif'])
	position['y'] = (probe2[modifier['y']['case']] - probe1['y'] * modifier['y']['modif']) * (-1 * modifier['y']['modif'])
	position['z'] = (probe2[modifier['z']['case']] - probe1['z'] * modifier['z']['modif']) * (-1 * modifier['z']['modif'])

	return position

def GetMaxManhattanDistance(allScanner):
	maxDistance = 0
	while len(allScanner) != 0:
		scanner = allScanner.pop()
		for current in allScanner:
			distance = abs(scanner['x'] - current['x']) + abs(scanner['y'] - current['y']) + abs(scanner['z'] - current['z'])
			maxDistance = max(maxDistance, distance)

	return maxDistance

def level1(input):
	#input = '--- scanner 0 ---\n404,-588,-901\n528,-643,409\n-838,591,734\n390,-675,-793\n-537,-823,-458\n-485,-357,347\n-345,-311,381\n-661,-816,-575\n-876,649,763\n-618,-824,-621\n553,345,-567\n474,580,667\n-447,-329,318\n-584,868,-557\n544,-627,-890\n564,392,-477\n455,729,728\n-892,524,684\n-689,845,-530\n423,-701,434\n7,-33,-71\n630,319,-379\n443,580,662\n-789,900,-551\n459,-707,401\n\n--- scanner 1 ---\n686,422,578\n605,423,415\n515,917,-361\n-336,658,858\n95,138,22\n-476,619,847\n-340,-569,-846\n567,-361,727\n-460,603,-452\n669,-402,600\n729,430,532\n-500,-761,534\n-322,571,750\n-466,-666,-811\n-429,-592,574\n-355,545,-477\n703,-491,-529\n-328,-685,520\n413,935,-424\n-391,539,-444\n586,-435,557\n-364,-763,-893\n807,-499,-711\n755,-354,-619\n553,889,-390\n\n--- scanner 2 ---\n649,640,665\n682,-795,504\n-784,533,-524\n-644,584,-595\n-588,-843,648\n-30,6,44\n-674,560,763\n500,723,-460\n609,671,-379\n-555,-800,653\n-675,-892,-343\n697,-426,-610\n578,704,681\n493,664,-388\n-671,-858,530\n-667,343,800\n571,-461,-707\n-138,-166,112\n-889,563,-600\n646,-828,498\n640,759,510\n-630,509,768\n-681,-892,-333\n673,-379,-804\n-742,-814,-386\n577,-820,562\n\n--- scanner 3 ---\n-589,542,597\n605,-692,669\n-500,565,-823\n-660,373,557\n-458,-679,-417\n-488,449,543\n-626,468,-788\n338,-750,-386\n528,-832,-391\n562,-778,733\n-938,-730,414\n543,643,-506\n-524,371,-870\n407,773,750\n-104,29,83\n378,-903,-323\n-778,-728,485\n426,699,580\n-438,-605,-362\n-469,-447,-387\n509,732,623\n647,635,-688\n-868,-804,481\n614,-800,639\n595,780,-596\n\n--- scanner 4 ---\n727,592,562\n-293,-554,779\n441,611,-461\n-714,465,-776\n-743,427,-804\n-660,-479,-426\n832,-632,460\n927,-485,-438\n408,393,-506\n466,436,-512\n110,16,151\n-258,-428,682\n-393,719,612\n-211,-452,876\n808,-476,-593\n-575,615,604\n-485,667,467\n-680,325,-822\n-627,-443,-432\n872,-547,-609\n833,512,582\n807,604,487\n839,-516,451\n891,-625,532\n-652,-548,-490\n30,-46,-14\n'
	scanners = InitialState(input.strip().split('\n'))
	for scanner in scanners.keys():
		SetRelative(scanners[scanner])

	baseScanner = scanners.pop(input.strip().split('\n')[0].replace('-', '').strip())
	while len(scanners.keys()) != 0:
		matching = {}
		nameFound = ''
		#for scanner in scanners.keys():
		for scanner in HACK:
			print('Test ' + scanner)
			tmpMatch = GetMatching(baseScanner, scanners[scanner])
			if tmpMatch:
				matching = tmpMatch
				nameFound = scanner
				break

		if nameFound == '':
			return 'error'
		else:
			print(nameFound)

		removedScanner = scanners.pop(nameFound)
		modifier = FindModifiers(baseScanner, removedScanner, matching)
		
		print('Modifier found')
		specificRelative = removedScanner[matching['matching'][1]]['relative']
		HACK.remove(scanner)
		for toRemove in [value[1] for value in matching['found']]:
			del specificRelative[toRemove]

		print('Start increment')
		IncrementProbe(baseScanner, matching['matching'][0], specificRelative, modifier)
		print('End increment')
		print('-------------')
		print(str(len(scanners.keys())) + ' left')
		print('-------------')
			
	return len(baseScanner.keys())

def level2(input):
	#input = '--- scanner 0 ---\n404,-588,-901\n528,-643,409\n-838,591,734\n390,-675,-793\n-537,-823,-458\n-485,-357,347\n-345,-311,381\n-661,-816,-575\n-876,649,763\n-618,-824,-621\n553,345,-567\n474,580,667\n-447,-329,318\n-584,868,-557\n544,-627,-890\n564,392,-477\n455,729,728\n-892,524,684\n-689,845,-530\n423,-701,434\n7,-33,-71\n630,319,-379\n443,580,662\n-789,900,-551\n459,-707,401\n\n--- scanner 1 ---\n686,422,578\n605,423,415\n515,917,-361\n-336,658,858\n95,138,22\n-476,619,847\n-340,-569,-846\n567,-361,727\n-460,603,-452\n669,-402,600\n729,430,532\n-500,-761,534\n-322,571,750\n-466,-666,-811\n-429,-592,574\n-355,545,-477\n703,-491,-529\n-328,-685,520\n413,935,-424\n-391,539,-444\n586,-435,557\n-364,-763,-893\n807,-499,-711\n755,-354,-619\n553,889,-390\n\n--- scanner 2 ---\n649,640,665\n682,-795,504\n-784,533,-524\n-644,584,-595\n-588,-843,648\n-30,6,44\n-674,560,763\n500,723,-460\n609,671,-379\n-555,-800,653\n-675,-892,-343\n697,-426,-610\n578,704,681\n493,664,-388\n-671,-858,530\n-667,343,800\n571,-461,-707\n-138,-166,112\n-889,563,-600\n646,-828,498\n640,759,510\n-630,509,768\n-681,-892,-333\n673,-379,-804\n-742,-814,-386\n577,-820,562\n\n--- scanner 3 ---\n-589,542,597\n605,-692,669\n-500,565,-823\n-660,373,557\n-458,-679,-417\n-488,449,543\n-626,468,-788\n338,-750,-386\n528,-832,-391\n562,-778,733\n-938,-730,414\n543,643,-506\n-524,371,-870\n407,773,750\n-104,29,83\n378,-903,-323\n-778,-728,485\n426,699,580\n-438,-605,-362\n-469,-447,-387\n509,732,623\n647,635,-688\n-868,-804,481\n614,-800,639\n595,780,-596\n\n--- scanner 4 ---\n727,592,562\n-293,-554,779\n441,611,-461\n-714,465,-776\n-743,427,-804\n-660,-479,-426\n832,-632,460\n927,-485,-438\n408,393,-506\n466,436,-512\n110,16,151\n-258,-428,682\n-393,719,612\n-211,-452,876\n808,-476,-593\n-575,615,604\n-485,667,467\n-680,325,-822\n-627,-443,-432\n872,-547,-609\n833,512,582\n807,604,487\n839,-516,451\n891,-625,532\n-652,-548,-490\n30,-46,-14\n'
	scanners = InitialState(input.strip().split('\n'))
	for scanner in scanners.keys():
		SetRelative(scanners[scanner])

	baseScanner = scanners.pop(input.strip().split('\n')[0].replace('-', '').strip())
	allScanner = []
	while len(scanners.keys()) != 0:
		matching = {}
		nameFound = ''
		#for scanner in scanners.keys():
		for scanner in HACK:
			print('Test ' + scanner)
			tmpMatch = GetMatching(baseScanner, scanners[scanner])
			if tmpMatch:
				matching = tmpMatch
				nameFound = scanner
				break

		if nameFound == '':
			return 'error'
		else:
			print(nameFound)

		removedScanner = scanners.pop(nameFound)
		modifier = FindModifiers(baseScanner, removedScanner, matching)
		
		print('Modifier found')
		specificRelative = removedScanner[matching['matching'][1]]['relative']
		HACK.remove(scanner)
		for toRemove in [value[1] for value in matching['found']]:
			del specificRelative[toRemove]

		print('Start increment')
		IncrementProbe(baseScanner, matching['matching'][0], specificRelative, modifier)
		print('End increment')

		print('Acquire scanner position')
		posScanner = GetPositionScanner(baseScanner[matching['matching'][0]], removedScanner[matching['matching'][1]], modifier)
		print(posScanner)
		allScanner.append(posScanner)

		print('-------------')
		print(str(len(scanners.keys())) + ' left')
		print('-------------')

	return GetMaxManhattanDistance(allScanner)