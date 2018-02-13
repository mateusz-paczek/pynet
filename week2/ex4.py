#!/usr/bin/python3.6

'''
4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding MAC address associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.
'''

# reading show_ip_int_brief.txt file

with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()

#Loop through all elements
for element in show_ip_int_brief:
    #check if FastEthernet4 is in line
    if 'FastEthernet4' in element:
        intf_name = element.split()[0]
        ip_address = element.split()[1]
#Creating tuple 'result' that stores (intf_name, ip_address)
result = (intf_name, ip_address)
print (result)
