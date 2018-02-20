#!/usr/bin/python3.6

mac = "c89c.1dea.0eb6"
mac = mac.split(".")
mac = "".join(mac)
mac = mac.upper()
#print (mac)

new_mac = []
while len(mac) > 0:
    entry = mac[:2]
    print (entry)
    mac = mac[2:]
    print (mac)
    new_mac.append(entry)
    print (new_mac)
