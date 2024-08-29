'''
File: strings_and_input.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of the program is to read an input from
a user, save it, and will print unformation on the input. 
Some of this information includes the length of the string,
the last 5 characters of the string, etc. 
'''

def str_info(string):
    '''
    This is the function which main() calls to. It
    prints out information on the string the user 
    provided in main()
    Parameters: 
        string: The user given string
    Returns: None
    '''
    # Print string length
    print(len(string))
    # Print second character
    print(string[1])
    # Print first 10 characters
    print(string[:10])
    # Print last 5 characters
    print(string[-5:])
    # Print totally uppercase
    print(string.upper())
    # Defines the first character
    char_one = string[0]
    # If first character is in QWERTY (upper or lower)...
    # ...print QWERTY
    if char_one in "qQwWeErRtTyY":
        print("QWERTY")
    # If first character is in uiop, print UIOP
    elif char_one in "uiop":
        print("UIOP")
    # If first character is any other letter, print LETTER
    elif char_one in "AaBbCcDdEFfGgHhIJjKkLlMmNnOPQRSsTUVvWXxYZz":
        print("LETTER")
    # If first character is a number, print DIGIT
    elif char_one in "0123456789":
        print("DIGIT")
    # If first character is anything else, print OTHER
    else:
        print("OTHER")
    

def main():
    '''
    This is the main function, which runs the rest of 
    the program and asks the user for an input. 
    Additionally, it prints the product of two numbers
    which are input by the user
    Parameters: 
        None
    Returns: 
        None
    '''
    string = input("input string: ")
    str_info(string)
    number_one = input()
    number_two = input()
    num_one_int = int(number_one)
    num_two_int = int(number_two)
    print(num_one_int * num_two_int)

main()
