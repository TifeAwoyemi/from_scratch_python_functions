"""
Calculating Cumulative Sum.

This file contains different variations of the sum() function that calculates the sum of elements in an iterable.

>>> level_01_my_sum(obj): This uses standard for loop to iterate over object (obj) and return the sum.
>>> level_02_my_sum(obj): This uses the iter() and next() functions to iterate over object (obj) and return the sum.
>>> level_03_my_sum(obj): This uses the __iter__() and __next__() methods to iterate over object (obj) and return the sum.
>>> level_04_my_sum(obj): This uses custom functions to iterate over object (obj) and return the sum.
>>> Range_From_Scratch(): This class defines custom functions that iterate over an object and gets each element in the object.

Examples:
    See examples/notebooks folder for simple usage and interactive demo.


"""


def level_01_my_sum(obj):
    """
    This calculates the sum of all elements in an iterable with integers and or floats.
    It uses a "for loop".

    Args:
        obj (list, tuple): An object zero or more numbers. 

    Returns:
        cum_sum (int, float): A value that represents the sum of all elements in iterable
    """
    cum_sum = 0
    
    for i in obj:
        cum_sum += i
        
    return cum_sum

def level_02_my_sum(obj):
    """
    This calculates the sum of all elements in an iterable with integers and or floats.
    It uses the iter() and next() functions.

    Args:
        obj (list, tuple): An object zero or more numbers. 

    Returns:
        cum_sum (int, float): A value that represents the sum of all elements in iterable
    """
    
    cum_sum = 0
    given_obj = iter(obj)
    while True:
        try:
            cum_sum += next(given_obj)
        except StopIteration:
            break
    
    return cum_sum

def level_03_my_sum(obj):
    """
    This calculates the sum of all elements in an iterable with integers and or floats.
    It uses the __iter__() and __next__() methods.

    Args:
        obj (list, tuple): An object zero or more numbers. 

    Returns:
        cum_sum (int, float): A value that represents the sum of all elements in iterable
    """
    
    cum_sum = 0
    given_obj = obj.__iter__()
    while True:
        try:
            cum_sum += given_obj.__next__()
        except StopIteration:
            break
    
    return cum_sum

## Still in the works
class Range_From_Scratch():
    def __init__(self, start, stop, curr):
        self.start = start
        self.stop = stop
        self.curr = curr

    def __myiter__(self):
        
        return self

    def __mynext__(self, curr):
        
        return curr

    def myiter():
        pass

    def mynext():
        pass

# def level_04_my_sum(obj):
#     """
#     This calculates the sum of all elements in an iterable with integers and or floats.
#     It uses custom callables from class with __myiter__() and __mynext__() methods iter() and next() functions.

#     Args:
#         obj (list, tuple): An object zero or more numbers. 

#     Returns:
#         cum_sum (int, float): A value that represents the sum of all elements in iterable
#     """
    
#     cum_sum = 0
#     given_obj = myiter(obj)
#     while True:
#         try:
#             cum_sum += mynext(given_obj)
#         except StopIteration:
#             break
    
#     return cum_sum    
    


