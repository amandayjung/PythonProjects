'''
File: swap.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: 
'''

def swap(string):
    '''
    This function strips the blank spaces from the front and
    end of the user input string. After that, it determines if
    the string can be split evenly or not. If it can, it switches
    the two halves. If it can't, it swaps it differently. 
    Parameters: 
        string: The user input string
    Returns: 
        None
    '''
    # Remove white spaces
    no_blank_string = string.strip()
    # Find string length
    length = len(no_blank_string)
    # Even split swap
    if length % 2 == 0:
        middle = length // 2
        swapped = no_blank_string[middle:] + no_blank_string[:middle]
    # Not even split swap
    else:
        middle = length // 2
        swapped = no_blank_string[middle+1:] + no_blank_string[middle]\
        + no_blank_string[:middle]
    # Print final swapped string
    print(swapped)

def main():
    '''
    This is the main function, which runs the rest of 
    the program and asks the user for an input. 
    Parameters: 
        None
    Returns: 
        None
    '''
    string = input("Please give a string to swap: ")
    swap(string)

main()
