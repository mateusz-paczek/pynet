#!/usr/bin/python3

'''
2. Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

#creating list with 5 IPs

ip_addr = ['10.1.1.1', '172.16.1.1', '192.168.1.1', '224.0.0.1', '1.1.1.1']

#appending IP address to ip_addr list

ip_addr.append('100.1.1.1')
print (ip_addr)

#add two more IPs using extend() method
ip_addr.extend(['200.1.1.1', '4.2.2.2'])
print (ip_addr)

#add 2 more IPs using list concatenantion
ip_addr = ip_addr + ['8.8.8.8', '8.8.4.4']
print (ip_addr)

#print first element of the list
print ("\nThis is first element of the list")
print (ip_addr[0])

print ("\nThis is last element of the list ")
print (ip_addr[-1])

#using pop method remove first and last element of the list
ip_addr.pop(0)
ip_addr.pop()

#update first element with IP '2.2.2.2'
ip_addr[0] = '2.2.2.2'
print (ip_addr)
