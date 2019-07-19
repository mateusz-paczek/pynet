#!/usr/bin/python3

"""
Use Jinja2 templating to render the following:
vlan {{ vlan_id }}
   name {{ vlan_name }}
Your template should be inside of your Python program for simplicity.
The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
"""
import jinja2

#create vlan variables as a dictionary
vlan_vars = {
	"vlan_id": "400",
	"vlan_name": "red400",
}

# Defina vlan template
vlan_template = '''
vlan {{ vlan_id }}
  name {{ vlan_name }}
'''

t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))

