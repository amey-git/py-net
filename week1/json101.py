#!/usr/bin/env python
import json

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '192.168.1.11'
my_list[-1]['attribs'] = range(5)

print my_list

print json.dumps(my_list)

#with open("some_json_file.json", "w") as f:
#    json.dump(my_list, f)
    
with open("some_json_file.json") as f:
    new_list = json.load(f)
    from pprint import pprint as pp
    pp(new_list)
