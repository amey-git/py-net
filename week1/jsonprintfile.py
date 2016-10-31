#!/usr/bin/env python

import sys
import yaml
import json

with open(sys.argv[1]) as f:
    list_yaml = yaml.load(f)
    
print "\nYAML format"
from pprint import pprint as pp
pp(list_yaml)

with open(sys.argv[2]) as f:
    list_json = json.load(f)

print "\nJSON format"
pp(list_json)
