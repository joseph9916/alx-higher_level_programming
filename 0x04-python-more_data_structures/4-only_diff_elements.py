#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = list()
    for char in set_1:
        if char not in set_2:
            new_list.append(char)
    for char in set_2:
        if char not in set_1:
            new_list.append(char)
    return new_list
