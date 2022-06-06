#!/usr/bin/python3
def no_c(my_string):
    temp = list(my_string)
    index = 0
    for i in temp:
        if i == 'c' or i == 'C':
            temp[index] = ""
        index += 1
    return "".join(temp)
