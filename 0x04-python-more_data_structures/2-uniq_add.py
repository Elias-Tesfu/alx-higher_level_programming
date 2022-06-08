#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp_list = []
    result = 0
    for item in my_list:
        if item not in temp_list:
            temp_list.append(item)
    for uniqs in temp_list:
        result = result + uniqs
    return result
