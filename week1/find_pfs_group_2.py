#!/usr/bin/env python

import sys

from ciscoconfparse import CiscoConfParse

ciscocfg = CiscoConfParse(sys.argv[1])

crypto_map_entries = ciscocfg.find_objects(r"^crypto map CRYPTO")

print "Following are the total number of crypto maps found in the config:"

pfs_group2_1 = list()

#for i in range(len(crypto_map_entries)):
#    print crypto_map_entries[i]
j = 0
for crypto_map in crypto_map_entries:
    print crypto_map_entries[j]
    if crypto_map_entries[j].re_search_children(r"set pfs group2"):
            pfs_group2_1.append(crypto_map)
    j += 1    

from  pprint import pprint as pp
print "\nFollowing are the crypto maps containing pfs group2:"
pp(pfs_group2_1)

print "\nFollowing is the config for the above crypto maps:"
for map in pfs_group2_1:
    print map.text
    for child in map.children:
        print child.text

print '\n\nMethod-2: using find_objects_w_child(parentspec=r"^blabla", childspec=r"blahblah")'

pfs_group2_2 = ciscocfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="set pfs group2")

for vals in pfs_group2_2:
    print vals.text
