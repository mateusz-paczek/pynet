#!/usr/bin/python3

'''
3.  Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version, serial number, and configuration register values.

Your output should look as follows:

OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
'''
import re

# Open file show_version.txt
with open("show_version.txt") as f:
	show_ver = f.read()

# Search for a OS Version
match = re.search(r"^Cisco IOS Software, .*, Version (.*),",show_ver, flags=re.M)
if match:
	os_version = match.group(1)

# Search for Serial Number
match = re.search(r"^Processor board ID (.*)\s*$",show_ver, flags=re.M)
if match:
	serial_number = match.group(1)

# Search for Configuration Register
match = re.search(r"^Configuration register is (.*)\s*$",show_ver, flags=re.M)
if match:
	config_reg = match.group(1)

print()
print (f"OS Version: {os_version:^15}")
print (f"Serial Number: {serial_number:^15}")
print (f"Configuration register: {config_reg:^15}")
