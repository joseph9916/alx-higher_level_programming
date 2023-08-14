#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for num in new_list:
        num = num % 2 
    return new_list
