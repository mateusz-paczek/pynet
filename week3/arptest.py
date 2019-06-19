#!/usr/bin/python3

mac = '1234567890AB'

new_mac = []

while len(mac) > 0:
	entry = mac[:2]
	mac = mac[2:]
	print (mac)
	new_mac.append(entry)

print (new_mac)
