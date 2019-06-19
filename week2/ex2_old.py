#!/usr/bin/python3.6
'''
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

# create empty list

ip_addr = []

# append IP Address
ip_addr.append("192.168.1.1")

# using extend() method to add 2 IP Addresses
ip_addr.extend(["10.1.1.1", "172.16.1.1"])

print (ip_addr)
print ("\n")

# using list concatenation to add 2 more IP Addresses

ip_addr = ip_addr + ["100.1.1.1", "200.1.1.1"]
print("Entire list")
print (ip_addr)

print ("First element")
print(ip_addr[0])

print ("Last element ")
print (ip_addr[-1])

print(ip_addr.pop(0))

print (ip_addr)

ip_addr.pop()

print ("Existing IP_Address list")
print (ip_addr)

ip_addr[0] = "2.2.2.2"

print (ip_addr)
