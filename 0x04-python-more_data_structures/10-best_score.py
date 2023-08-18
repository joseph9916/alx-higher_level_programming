#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None:
    keys = list(a_dictionary.keys())
    largest_key = keys[0]
    for key in keys:
        if a_dictionary[key] > a_dictionary[largest_key]:
            largest_key = key
    return largest_key
