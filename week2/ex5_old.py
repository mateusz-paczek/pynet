#!/usr/bin/python3.6

'''
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''
#open show_ip_bgp_summ.txt file
with open("show_ip_bgp_summ.txt") as f:
    show_ip_bgp_summ = f.readlines()

#extract remote_as from first line
remote_as = show_ip_bgp_summ[0].split()[-1]
#extract neighbor IP from last line
neighbor_ip = show_ip_bgp_summ[-1].split()[0]

print (f"Remote AS: {remote_as}, Neighbor IP: {neighbor_ip}")
