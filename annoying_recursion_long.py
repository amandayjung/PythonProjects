'''
File: annoying_recursion_long.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of the program is to use recursion to generate
a fibonacci sequence. annoying_fibonacci_sequence(n) returns the first
n numbers in the sequence.
'''

def annoying_fibonacci_sequence(n):
    '''
    Returns a specified amount of the fibonacci sequence
    Parameters: 
        n: How many numbers to be returned
    Returns: 
        []: If return no numbers
        [0]: If return 1 number
        [0,1]: If return 2 numbers
        result: A list containing the fibonacci sequence
        with the specified amount of numbers
    '''
    # If return no numbers
    if n == 0:
        return []
    # If return 1 number only
    if n == 1:
        return [0]
    # If return only 2 numbers
    if n == 2:
        return [0, 1]
    result = annoying_fibonacci_sequence(n - 1)
    result.append(result[-1] + result[-2])
    return result
