#/usr/bin/env python

import yaml

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '192.168.1.10'
my_list[-1]['attribs'] = range(7)

print my_list

print yaml.dump(my_list, default_flow_style=False)

print yaml.dump(my_list, default_flow_style=True)

#with open("some_file.yml", "w") as f:
#    f.write(yaml.dump(my_list, default_flow_style=False)
#)

with open("some_file.yml") as f:
    new_list1 = yaml.load(f)
    print new_list1
    print type(new_list1[-1])
    print type(new_list1)
