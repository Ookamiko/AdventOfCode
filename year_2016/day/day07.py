#!/usr/bin/python

import re as regex

def level1(input):
	list_ips = input.strip().split('\n')
	tls_ip = 0

	reg_bracket = r'\[[a-z]+\]'

	for ip in list_ips:
		brac = ''.join(regex.findall(reg_bracket, ip))
		found = False

		for i in range(1, len(brac) - 4):
			if brac[i] == brac[i + 3] and brac[i + 1] == brac[i + 2] and brac[i] != brac[i + 1]:
				found = True
				break

		if found:
			continue

		wbrac = '-'.join(regex.split(reg_bracket, ip))

		for i in range(0, len(wbrac) - 3):
			if wbrac[i] == wbrac[i + 3] and wbrac[i + 1] == wbrac[i + 2] and wbrac[i] != wbrac[i + 1]:
				found = True
				tls_ip += 1
				break

	return tls_ip

def level2(input):
	list_ips = input.strip().split('\n')
	ssl_ip = 0

	reg_bracket = r'\[[a-z]+\]'

	for ip in list_ips:
		brac = ''.join(regex.findall(reg_bracket, ip))
		wbrac = '--'.join(regex.split(reg_bracket, ip))

		for i in range(0, len(wbrac) - 2):
			fchar = wbrac[i]
			schar = wbrac[i + 1]

			if fchar != schar and fchar == wbrac[i + 2] and ((schar + fchar + schar) in brac):
				ssl_ip += 1
				break

	return ssl_ip