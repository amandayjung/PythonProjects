'''
File: second_largest_of_four_ints.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: Using repeated input from a user, the 
program will print the second largest number of the four
'''
first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())
# Largest and second largest are pre-set before anything
largest = max(first_number, second_number)
second_largest = min(first_number, second_number)
# Compare the other two numbers with largest and second
if third_number > largest:
    second_largest = largest
    largest = third_number
elif third_number > second_largest:
    second_largest = third_number
if fourth_number > largest:
    second_largest = largest
    largest = fourth_number
elif fourth_number > second_largest:
    second_largest = fourth_number
# Print the second largest
print(second_largest)
