#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = list()
    for char in set_1:
        if char in set_2:
            new_list.append(char)
    return new_list
