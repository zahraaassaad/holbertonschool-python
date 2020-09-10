#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i=0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end = "") # if i != x - 1 else "\n")
    except:
        print()
        return i
    print()
    return i+1
