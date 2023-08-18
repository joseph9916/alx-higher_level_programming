#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())
    for key in list_key:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
