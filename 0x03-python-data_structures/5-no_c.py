#!/usr/bin/python3
def no_c(my_string):
    temp = list(my_string)
    i = 0
    for i in temp:
        if i == 'c' or i == 'C':
            temp[i] = ""
        i++
    return "".join(temp)
