#!/usr/bin/python3.6

'''
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "


Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "


# remove whitespace from the string using strip() method
show_version = show_version.strip()

# print (show_version)

# split show_version variable, whitespace is a delimeter
show_version_table = show_version.split()

# print (show_version_table)

model = show_version_table[1]
serial_number = show_version_table[2]

#vendor_cisco = 'cisco' in model.lower()
#print (vendor_cisco)
if 'cisco' in model.lower() and '881' in model.lower():
    print ("Model is: {} ".format(model))
else:
    print ("No 'Cisco' or '881' in model")

print ("Serial number is: {}".format(serial_number))
