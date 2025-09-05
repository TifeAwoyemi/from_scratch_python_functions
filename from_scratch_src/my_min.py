"""
Identifying the minimum value in an iterable where iterable must contain only compatible types.

This file contains my version of the min() function that returns the minimum element of an iterable.

>>> level_01_my_min(obj): This uses standard for and while loops with my_len function to iterate over object (obj) and return the minimum.


Examples:
    See examples/notebooks folder for simple usage and interactive demo.

"""

from my_len import level_01_my_len as my_len
def level_01_my_min(obj):
    """
    This counts the number of elements in an iterable with integers and/or floats, strings.
    It uses a "for loop".

    Args:
        obj (list, tuple): An object with zero or more numbers or strings. 

    Returns:
        min_element (int, float): A value that represents the minimum elements in the "obj" iterable
    """
    k = 0
    if my_len(obj) >= 1:
        while k < my_len(obj):
            for i in range(my_len(obj)):
                for j in range(my_len(obj)):
                    if i != j and obj[i] < obj[j]:
                        obj[i], obj[j] = obj[j], obj[i]
            k += 1            
    min_element = obj[0]  
    return min_element