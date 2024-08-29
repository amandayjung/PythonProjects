'''
File: count_items.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: This program reads a file which has a series of items and 
their corresponding counts. It organizes the information alphabetically
and prints it. 
'''

def read_file(filename):
    '''
    Reads a user inputted file filled with items
    and counts
    Parameters: 
        filename: The name of the file
    Returns: 
        items: A dictionary that has items for
        keys and counts for values
    '''
    items = {}
    file = open(filename, "r")
    # Reads each line
    for line in file:
        line = line.strip().split()
        # Keep going if line doesn't start with hashtag
        if line and not line[0].startswith('#'):
            item_key = line[0]
            item_val = int(line[1])
            # Checks if the item already exists
            if item_key in items:
                items[item_key] += item_val
            else:
                items[item_key] = item_val
    file.close()
    return items

def dict_sort(dictionary):
    '''
    Sorts the dictionary keys in alphabetical order
    Parameters: 
        dictionary: The dictionary that is being sorted
    Returns: 
        sorted_dictionary: The final sorted dictionary
    '''
    sorted_dictionary = {}
    sorted_dict_k = sorted(dictionary.keys())
    # Loops through the keys
    for key in sorted_dict_k:
        sorted_dictionary[key] = dictionary[key]
    return sorted_dictionary

def pair_items(items):
    '''
    Coverts the dictionary into a list of tuples
    Parameters:
        items: The dictionary that contains the information
        to be used in the list of tuples
    Returns: 
        pairs: A list of tuples that have the count of every item
    '''
    pairs = []
    alpha_sorted_items = dict_sort(items)
    # Loops through all the sorted items
    for key, val in alpha_sorted_items.items():
        tuple = (val, key) 
        pairs.append(tuple)
    return pairs

def print_pairs(pairs):
    '''
    Prints the steps and final list
    Parameters: 
        pairs: The list of tuples created earlier
    Returns: 
        None
    '''
    # Step 1
    print("STEP 1: THE ORIGINAL DICTIONARY")
    # Loops through tuples in pair list
    for key, value in pairs:
        print("Key: " + str(value) + " Value: " + str(key))
    print()
    # Step 2
    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    print(pairs)
    print()
    # Step 3
    pairs.sort()
    print("STEP 3: AFTER SORTING")
    print(pairs)
    print()
    # Step 4
    print("STEP 4: THE ACTUAL OUTPUT")
    # Loops through tuples
    for value, key in pairs:
        print(str(key) + " " + str(value))

def main():
    '''
    The main function which runs the rest of the program
    and also gets the input file 
    Parameters: 
        None
    Returns: 
        None
    '''
    input_file = input("File to scan: ")
    items = read_file(input_file)
    pairs = pair_items(items)
    print_pairs(pairs)

main()
