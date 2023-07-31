#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
    return i + 1 if x <= len(my_list) else len(my_list)
