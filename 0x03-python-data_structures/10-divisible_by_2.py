#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new = list(my_list)
    for i in new:
        if i % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return new
