#!/usr/bin/python
import re as regex

def ExecuteCommand(arg1, arg2, command):
	toReturn = 0;
	if(command == "AND"):
		toReturn = arg1 & arg2
	elif(command == "OR"):
		toReturn = arg1 | arg2
	elif(command == "LSHIFT"):
		toReturn = arg1 << arg2
	elif(command == "RSHIFT"):
		toReturn = arg1 >> arg2
	elif(command == "NOT"):
		toReturn = ~arg1 & 65535
	elif(command == ""):
		toReturn = arg1
	return toReturn

def level1(input):
	command_list = input.split("\n")
	tmp_list = []
	wires = {}
	stop = False
	reg = r"(\S*)\s*(\S*)\s*(\S*) -> (\S*)"
	while not(stop):
		stop = True
		for i in range(len(command_list)):
			stop = False
			matches = regex.match(reg, command_list[i])
			if(matches):
				group = matches.groups()
				if(group[1] == "" and group[2] == ""):
					if (regex.match(r'\d+', group[0]) != None):
						wires[group[3]] = int(group[0])
					else:
						if not(group[0] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						wires[group[3]] = wires[group[0]]
				elif(regex.match(r'[A-Z]+', group[0]) != None and group[2] == ""):
					if not(group[1] in wires.keys()):
						tmp_list.append(command_list[i])
						continue
					wires[group[3]] = ExecuteCommand(wires[group[1]], 0, group[0])
				else:
					arg1 = 0
					if (regex.match(r'\d+', group[0]) != None):
						arg1 = int(group[0])
					else:
						if not(group[0] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						arg1 = wires[group[0]]

					arg2 = 0
					if (regex.match(r'\d+', group[2]) != None):
						arg2 = int(group[2])
					else:
						if not(group[2] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						arg2 = wires[group[2]]

					wires[group[3]] = ExecuteCommand(arg1, arg2, group[1])
		command_list = tmp_list
		tmp_list = []

	return str(wires["a"])

def level2(input):
	command_list = input.split("\n")
	tmp_list = []
	wires = {"b" : int(level1(input))}
	stop = False
	reg = r"(\S*)\s*(\S*)\s*(\S*) -> (\S*)"
	while not(stop):
		stop = True
		for i in range(len(command_list)):
			stop = False
			matches = regex.match(reg, command_list[i])
			if(matches):
				group = matches.groups()
				if(group[1] == "" and group[2] == ""):
					if (regex.match(r'\d+', group[0]) != None):
						if(group[3] != "b"):
							wires[group[3]] = int(group[0])
					else:
						if not(group[0] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						wires[group[3]] = wires[group[0]]
				elif(regex.match(r'[A-Z]+', group[0]) != None and group[2] == ""):
					if not(group[1] in wires.keys()):
						tmp_list.append(command_list[i])
						continue
					wires[group[3]] = ExecuteCommand(wires[group[1]], 0, group[0])
				else:
					arg1 = 0
					if (regex.match(r'\d+', group[0]) != None):
						arg1 = int(group[0])
					else:
						if not(group[0] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						arg1 = wires[group[0]]

					arg2 = 0
					if (regex.match(r'\d+', group[2]) != None):
						arg2 = int(group[2])
					else:
						if not(group[2] in wires.keys()):
							tmp_list.append(command_list[i])
							continue
						arg2 = wires[group[2]]

					wires[group[3]] = ExecuteCommand(arg1, arg2, group[1])
		command_list = tmp_list
		tmp_list = []

	return str(wires["a"])