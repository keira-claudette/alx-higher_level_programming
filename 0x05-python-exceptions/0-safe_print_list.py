#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print('{}'.format(my_list[i - 1]), end='')
            if i == x:
                break
    except:
        pass
    print()
    return i
