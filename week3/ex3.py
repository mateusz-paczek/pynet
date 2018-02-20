#!/usr/bin/python3.6
'''
3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.
'''


# open file "show_lldp_neigbors_detail.txt"
with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.readlines()

# initaliza 2 variable - now they have no values
system_name, port_id = (None, None)
# loop through the lines

for line in show_lldp:
    # check if "System Name" is in line
    if "System Name" in line:
        # extract hostname
        system_name = line.split("Name: ")[1]
    elif "Port id" in line:
        port_id = line.split("id: ")[1]

    if system_name and port_id:
        break

print (f"System name: {system_name}")
print (f"Port ID: {port_id}")
