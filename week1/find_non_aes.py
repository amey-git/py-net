#!/usr/bin/env python

import sys

from ciscoconfparse import CiscoConfParse

ciscocfg = CiscoConfParse(sys.argv[1])

crypto_map_entries = ciscocfg.find_objects(r"^crypto map CRYPTO")

print "Following are the total number of crypto maps found in the config:"

non_aes = list()

#for i in range(len(crypto_map_entries)):
#    print crypto_map_entries[i]
j = 0
for crypto_map in crypto_map_entries:
    print crypto_map_entries[j]
    if crypto_map_entries[j].re_search_children(r"transform-set AES"):
        j += 1    
        continue
    else:
        non_aes.append(crypto_map)
        j += 1    

from  pprint import pprint as pp
print "\nFollowing are the crypto maps not using AES encryption:"
pp(non_aes)
final_set = list()
print "\nFollowing is the config for the above crypto maps:"
for map in non_aes:
    print map.text
    for child in map.children:
        print child.text
        temp = child.text.split(' ')
        k = 0
        for i in temp:
            k += 1
            if i == 'transform-set':
                final_set.append({map.text : temp[k]})
            

print final_set

#print '\n\nMethod-2: using find_objects_w_child(parentspec=r"^blabla", childspec=r"blahblah")'

#pfs_group2_2 = ciscocfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="set pfs group2")

#for vals in pfs_group2_2:
#    print vals.text
