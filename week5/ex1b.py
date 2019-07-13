#!/usr/bin/python3

'''
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
'''

# Define ssh_conn2 function
def ssh_conn2(ip_addr, username, password, device_type="cisco_ios"):
	print ("-" * 80)
	print(f"IP Address: {ip_addr}")
	print(f"Username: {username}")
	print(f"Password: {password}")
	print(f"Platform: {device_type}")

# Adding a default value
ssh_conn2("192.168.1.1", password="cisco123", username="admin")
ssh_conn2("192.168.1.1", password="cisco123", username="admin", device_type="nx_os")

# Calling using a dictionary
my_device = {
	"ip_addr": "172.16.1.1",
	"device_type": "cisco_xr",
	"username": "admin",
	"password": "cisco123"
}

ssh_conn2(**my_device)
