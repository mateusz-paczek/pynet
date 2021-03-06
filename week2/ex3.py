#!/usr/bin/python3

'''
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)


Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
'''

from pprint import pprint

#read the 'show_arp.txt' file

with open('show_arp.txt') as f:
	show_arp = f.readlines()

#output is now a list so we need to get rid of header (first line)
show_arp = show_arp[1:]

#use the sort() method to sort the list based on IP addresses
show_arp.sort()

#create a new list slice that is onlyu the frist three ARP entries
show_3_arp = show_arp[0:3]


#using the .join() method join this 3 ARP entries back together as a singe string using the newline character '\n' as the separator
show_3_arp_string = "\n".join(show_3_arp)


#write this string containing 3 ARP entries out to a file 
#I will use context manager

with open("arp_entries.txt",'w') as f:
	f.write(show_3_arp_string)

