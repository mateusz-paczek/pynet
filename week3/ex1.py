#!/usr/bin/python3
from pprint import pprint

'''
1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''

#read the file
with open("show_vlan.txt") as f:
	show_vlan = f.readlines()


#create empty list
vlan_list = []

#loop through each line
for line in show_vlan:

	#omit lines where there is 'Name' or '----' 
	if 'VLAN' in line or '----' in line or line.startswith('   '):
		continue
        #extract vlan_id from the line
	vlan_id = line.split()[0]

	#extract vlan_name from the line
	vlan_name = line.split()[1]
	
	#create list that consist of tuples
	vlan_list.append((vlan_id, vlan_name))

        
pprint(vlan_list)

