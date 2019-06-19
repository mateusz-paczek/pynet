#!/usr/bin/python3.6
'''
4. You have the following data structure:

arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]


Loop over this data structure and extract all of the MAC addresses. Process all of the MAC addresses to get them into a standard format. Print all of the new standardized MAC address to the screen. The standardized format should be as follows:

00:62:EC:29:70:FE

The hex digits should be capitalized. Additionally, there should be a colon between each octet in the MAC address.
'''
# define arp_table structure
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
             ('10.220.88.20', 'c89c.1dea.0eb6'),
             ('10.220.88.21', '1c6a.7aaf.576c'),
             ('10.220.88.28', '5254.aba8.9aea'),
             ('10.220.88.29', '5254.abbe.5b7b'),
             ('10.220.88.30', '5254.ab71.e119'),
             ('10.220.88.32', '5254.abc7.26aa'),
             ('10.220.88.33', '5254.ab3a.8d26'),
             ('10.220.88.35', '5254.abfb.af12'),
             ('10.220.88.37', '0001.00ff.0001'),
             ('10.220.88.38', '0002.00ff.0001'),
             ('10.220.88.39', '6464.9be8.08c8'),
             ('10.220.88.40', '001c.c4bf.826a'),
             ('10.220.88.41', '001b.7873.5634')]

# define empty table
mac_address_table = []
# loop through the whole structure
for entry in arp_table:
    mac_address_table.append(entry[1])

# loop through mac_address_table
for mac in mac_address_table:
    #split mac address
    mac = mac.split(".")
    #join mac address -> eg MAC looks like that: 001b78735634
    mac = "".join(mac)
    #use capital letter -> eg MAC looks like that: 001B78735634
    mac = mac.upper()
    #creating standard format like that: 00:1B:78:73:56:34
    new_mac = ":".join(mac[i:i + 2] for i in range(0, 12, 2))
    print (new_mac)
#print (mac_address_table)
