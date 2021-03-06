#!/usr/bin/python3
'''

iOpen showw_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).
'''

banner = '*' * 60

#open file
f = open("show_version.txt")

#read the file
output = f.read()

#print the file to the screen
print (banner)
print (output)
print (banner)
print (type(output))
print (banner)

#now we need to close the file
f.close()


#alternative and preferred way of opening the file
with open("show_version.txt") as f:
	output = f.readlines()

#print to the screen
print ("\n" + banner)
print (output)
print (banner)
print (type(output))

#there is no need to close file here

