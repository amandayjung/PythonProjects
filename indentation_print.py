'''
File: indentation_print.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: Read lines of input until user types "quit", 
counts spaces in each line, and print the count.
'''

# Infinite loop 
quit = False
while not quit:
    user_input = input()
    # Check if user wants to quit
    if user_input.strip() == "quit":
        quit = True
    else:
        # Count spaces and print
        spaces = len(user_input) - len(user_input.lstrip())
        print(spaces)
