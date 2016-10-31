#!/usr/bin/env python

import sys

from ciscoconfparse import CiscoConfParse

ciscocfg = CiscoConfParse(sys.argv[1])

crypto_map_entries = ciscocfg.find_objects(r"^crypto map CRYPTO")

print "Following are the crypto maps found in the config:"

for i in range(len(crypto_map_entries)):
    print crypto_map_entries[i]

print "\nAnd following are the full crypto map config:"
for crypto_map_entry in crypto_map_entries:
    print crypto_map_entry.text
    for child in crypto_map_entry.children:
        print child.text


