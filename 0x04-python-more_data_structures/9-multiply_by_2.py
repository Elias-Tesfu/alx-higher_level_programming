#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dict = {}
    for i in a_dictionary:
        new = (a_dictionary.get(i)) * 2
        temp_dict.update({i: new})
    return (temp_dict)
