#!/usr/bin/python3

"""
Using a conditional in a Jinja2 template, generate the following output:
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
The encryption of aes, and the Diffie-Hellman group should be variables in the template.
Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set
to True.
Your template should be inside your Python program for simplicity.
"""

import jinja2

# Defina vars that will be used in template creation
template_vars = {
	"isakamp_enable": True,
	"encryption": "aes",
	"dh_group": 5,
}

# Define actual template
crypto_template = '''
{% if isakamp_enable -%}
crypto isakamp policy 10
  encryption {{ encryption }}
  authentication pre-share
  group {{ dh_group }}
crypto isakamp key MY_KEY address 1.1.1.1 no-xauth
crypto isakamp keepalive 10 periodic
{% endif %}
'''
t = jinja2.Template(crypto_template)
print(t.render(template_vars))
