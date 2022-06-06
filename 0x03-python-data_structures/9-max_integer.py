#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum = 0
    for index in my_list:
        if index > maximum:
            maximum = index
    return maximum
