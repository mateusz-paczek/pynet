#!/usr/bin/python3.6

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

with open("show_arp.txt") as f:
    show_arp = f.readlines()

# printing ARP Entries without header line
show_arp = show_arp[1:]
pprint(show_arp)

show_arp.sort()

# creating a new list that has first three ARP Entries
show_arp_3_entries = show_arp[:3]
print("\n\n")
pprint(show_arp_3_entries)

# joining 3 ARP Entries based on newline character
show_arp_3_entries = "\n".join(show_arp_3_entries)

with open("arp_entries.txt", "w") as f:
    f.write(show_arp_3_entries)
