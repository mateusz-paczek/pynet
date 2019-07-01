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


#creating network device dictionary

network_device = {"ip_addr":"10.1.1.1", "vendor": "cisco", "username":"admin", "password":"admin123"}

#print ip_addr key from the dictionary
print(network_device['ip_addr'])

#check if 'vendor' key is 'cisco' or 'juniper' and then update dictinary with 'platform' key
if network_device['vendor'] == 'cisco':
    network_device.update(platform = 'ios')
elif network_device['vendor'] == 'juniper':
    network_device.update(platform = 'junos')


#creating bgp_fields dictionary

bgp_fields = {
    'bgp_as': 42,
    'peer_as': 100,
    'peer_ip': '172.16.31.100',
}

print (bgp_fields)

#add all bgp_fields key-value pairs to network_device dictionary
network_device.update(bgp_fields)
#print updated network_device dictionary
print(network_device)

#print all keys of network_device dictionary

print('---' * 30)
print("Loop through all dictionary keys \n")

for key in network_device:
    print(key)

#print all key-values using single loop

for k,v in network_device.items():
    print("{key:>15} ----> {value:>15}".format(key=k,value=v))
