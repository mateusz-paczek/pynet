#!/usr/bin/python3.6
from __future__ import print_function
# 1. Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). Print these three variables to standard output using a single print statement.

ip_addr1 = '192.168.1.1'
ip_addr2 = '10.1.1.1'
ip_addr3 = '172.16.30.1'

# Default printing for Python3
print("{:20}{:20}{:20}".format(ip_addr1, ip_addr2, ip_addr3))

print ("\n")

# previous printing methon
print ("%s %s %s" % (ip_addr1, ip_addr2, ip_addr3))

# printing using "f" string

print (f"{ip_addr1:20}{ip_addr2:20}{ip_addr3:20}")
