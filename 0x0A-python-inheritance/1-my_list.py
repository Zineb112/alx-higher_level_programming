#!/usr/bin/python3


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
