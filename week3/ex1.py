#!/usr/bin/python3.6
from pprint import pprint
'''
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
 '''

# define empty vlan_list
vlan_list = []
# open "show_vlan.txt" file
with open("show_vlan.txt") as f:
    show_vlan = f.readlines()

# print (show_vlan)

# loop through each line
for line in show_vlan:
    # omit lines that don't show vlans
    if "VLAN" in line or "-----" in line or line.startswith('   '):
        continue
    #extract vlan ID
    vlan_id = line.split()[0]
    #extract vlan name
    vlan_name = line.split()[1]
    #create vlan_list by appending (vlan_id, vlan_name) tuple
    vlan_list.append((vlan_id, vlan_name))

pprint(vlan_list)
