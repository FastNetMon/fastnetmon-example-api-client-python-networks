#!/usr/bin/python3

import requests
import os
import sys
import urllib.request, urllib.parse, urllib.error
import random

# Auth details
auth_data = ('admin', 'your_password_replace_it')

# Create random network for tests
new_network = "%d.%d.%d.%d/22" % (random.randint(1,254), random.randint(1,254), random.randint(1,254), random.randint(1,254))  

print("Add random network:", new_network)

# Encode any values which have spaces or '/' inside them
new_network_encoded = urllib.parse.quote_plus(new_network)

# Create networks_list entry
r = requests.put('http://127.0.0.1:10007/main/networks_list/' + new_network_encoded, auth=auth_data)

if r.status_code == 200:
    print("Correctly added new subnet")
else:
    print("Can't add new subnet", r.json()['error_text'])

# Show all networks list entries
r = requests.get('http://127.0.0.1:10007/main/networks_list', auth=auth_data)

if r.status_code != 200:
    print("API call failed")
    sys.exit(0)

print("Networks list with new network:", r.json())
r = requests.delete('http://127.0.0.1:10007/main/networks_list/' + new_network_encoded, auth=auth_data)

if r.status_code != 200:
    print("Cannot delete network from networks_list")
    sys.exit(0)
else:
    print("Correctly removed new subnet")
    sys.exit(0)
