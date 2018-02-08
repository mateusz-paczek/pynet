#!/usr/bin/python3.6

'''

3.   Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

# define 3 variables
ip_address = "2001:db8:1234::1"
IP_ADDRESS = "2001:db8:1234::2"
IP_address123 = "2001:db8:1234::3"


print ("Checking if ip_address {} is equal to IP_ADDRESS {}. \nThe result is the following: {} ".format(ip_address, IP_ADDRESS, (ip_address == IP_ADDRESS)))

print ("Checking if ip_address {} is not equal to IP_address123 {}. \nThe result is the following: {} ".format(ip_address, IP_address123, (ip_address != IP_address123)))
