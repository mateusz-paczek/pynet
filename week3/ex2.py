#!/usr/bin/python3

'''
2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.
'''

#read the "show_arp.txt"
with open("show_arp.txt") as f:
	show_arp_lines = f.readlines()

#Initialize two variables as a False
(found1, found2) = (False, False)

#Loop through the content of the file
for line in show_arp_lines:
	if "Protocol" in line:
		continue
        #extract IP address from the file
	ip_addr = line.split()[1]
	#extract MAC address from the file
	mac_addr = line.split()[3]

	#check the first condition
	if ip_addr == '10.220.88.1':
		print (f"Default gateway IP/MAC is: {ip_addr}/{mac_addr}")
		found1 = True
	
	#check second condition
	if ip_addr == '10.220.88.30':
		print (f"Arista3 IP/MAC is {ip_addr}/{mac_addr}")
		found2 = True
	if found1 and found2:
		print ("Exiting...")
		break

print()

	
