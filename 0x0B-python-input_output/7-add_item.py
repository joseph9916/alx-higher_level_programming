#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file:
"""


import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    with open("add_item.json", 'r', encoding="utf-8") as f:
        lst = json.load(f)
else:
    lst = list()
for i in range(1, len(sys.argv)):
    lst.append(sys.argv[i])
with open("add_item.json", 'w', encoding="utf-8") as f:
    json.dump(lst, f)
