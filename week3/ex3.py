#!/usr/bin/python3

'''3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.
'''

#read the file with Context Manager
with open("show_lldp_neighbors_detail.txt") as f:
	show_lldp = f.readlines()

#Initialize 2 Variables - now they have no values
(system_name, port_id) = (None, None)

#Loop through the file
for line in show_lldp:
	if 'Port id' in line:
		port_id = line.split("Port id: ")[1]
	
	if 'System Name' in line:
		system_name = line.split("System Name: ")[1]

	if port_id and system_name:
		break
print()
print (f"System name: {system_name}")
print (f"port ID: {port_id}")
print()
