"""
Counting the numeber of elements in an iterable.

This file contains my version of the len() function that counts the number of elements in an iterable.

>>> level_01_my_len(obj): This uses standard for loop to iterate over object (obj) and return the number of elements.


Examples:
    See examples/notebooks folder for simple usage and interactive demo.

"""


def level_01_my_len(obj):
    """
    This counts the number of elements in an iterable with integers and or floats.
    It uses a "for loop".

    Args:
        obj (list, tuple): An object zero or more numbers. 

    Returns:
        count (int, float): A value that represents the total elements in iterable
    """
    count = 0
    
    for item in obj:
        count += 1
        
    return count


