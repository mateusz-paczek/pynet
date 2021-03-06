#!/usr/bin/python3

'''
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''

#read show_ip_bgp_summ.txt into program

with open("show_ip_bgp_summ.txt") as f:
	show_ip_bgp_summ = f.readlines()

as_number = show_ip_bgp_summ[0].split()[-1]
bgp_peer = show_ip_bgp_summ[-1].split()[0]

print (f"As number is: {as_number} and bgp_peer is {bgp_peer} \n")
