"""
Sorting an iterable where iterable must contain only compatible types.

This file contains my version of the list.sort()/sorted() functions that return a sorted iterable in ascending order.

>>> level_01_my_sort_bubble(obj): This uses standard for and while loops with my_len function to iterate over object (obj) and sort it.


Examples:
    See examples/notebooks folder for simple usage and interactive demo.

"""

from my_len import level_01_my_len as my_len
def level_01_my_sort_bubble(obj):
    """
    This sorts an iterable with integers and/or floats, strings.
    It uses a "for loop".

    Args:
        obj (list, tuple): An object zero or more numbers. 

    Returns:
        sorted_obj (int, float): Sorted object in ascending order.
    """

    k = 0
    if my_len(obj) >= 1:
        while k < my_len(obj):
            for i in range(my_len(obj)):
                for j in range(my_len(obj)):
                    if i != j and obj[i] < obj[j]:
                        obj[i], obj[j] = obj[j], obj[i]
            k += 1    
    sorted_obj = obj     
    return sorted_obj

# print(level_01_my_sort_bubble([1, 2, 5, 3, 9, 7]))