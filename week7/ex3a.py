#!/usr/bin/python3

"""
Create a YAML file that defines a list of interface names. Use the expanded form of YAML.
Use Python to read in this YAML list and print this to the screen.
The output of your Python script should look as follows:
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7',
 'Management1', 'Vlan1']
"""

import yaml

yaml_file = "ex3a.yml"

with open(yaml_file) as f:
	data = yaml.load(f, Loader=yaml.FullLoader)

print()
print(data)
print()
