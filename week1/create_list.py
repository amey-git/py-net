#!/usr/bin/env python

import sys
import yaml
import json

print "Please provide 6 arguments for the list: hostname, IP_Addr, version, vendor, platform, location"
print sys.argv

if len(sys.argv) != 7:
    print "The number of arguments you entered is not 6. Please try again..."

my_list = [
{
'hostname': sys.argv[1],
'IP_Addr': sys.argv[2],
'OS version': sys.argv[3],
'Vendor': sys.argv[4],
'Platform': sys.argv[5],
'Device Location': sys.argv[6]
}
]

with open("yamllist.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("jsonlist.json", "w") as f:
    json.dump(my_list, f)
