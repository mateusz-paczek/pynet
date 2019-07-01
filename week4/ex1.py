#!/usr/bin/python3
'''
1. Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
'''

# Create dict representing a network device
net_device = {
	"ip_addr": '10.1.1.1',
	"vendor": "cisco",
	"username": "admin",
	"password": "cisco123"
}

# Print out the "ip_addr" key from the dictionary
#print (net_device["ip_addr"])
print (f"IP Address is: {net_device['ip_addr']}")
print()

# If the "vendor" key is "cisco" set "platform" to "ios", if the "vendor" key is "juniper" set "platform" to "junos"
if net_device["vendor"].lower() == "cisco":
	net_device["platform"] = "ios"
elif net_device["vendor"].lower() == "juniper":
	net_device["platform"] = "junos"


# Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.
bgp_fields = {
	"bgp_as": "100",
	"peer_as": "200",
	"peer_ip": "10.1.1.2"
}

# Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.
net_device.update(bgp_fields)

# Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
for key in net_device:
	print(f"The key is: {key}")

# Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
for key,value in net_device.items():
	print (f"For KEY {key} VALUE is: {value}")
