'''
File: friends.py
Author: Amanda Jung
Course: CSC 120, Spring 2024
Purpose: This program organizes friendships between various
people into a linked list so that a user can find mutual friends
'''

from linked_list import *

def read_input_file(file_name):
    '''
    Reads input file and returns as a list
    Parameters:
        file_name: The imported file
    Returns: 
        friendships: A list of tuples for friendships
    '''
    file = open(file_name, 'r')
    friendships = []
    # Iterates through each line
    for line in file.readlines():
        friendships.append(line.strip().split())
    file.close()
    return friendships

def construct_linked_list(friendships):
    '''
    Creates a linked list
    Parameters:
        friendships: List of tuples for friendships
    Returns:
        linked_list: A linked list of friendships
    '''
    linked_list = LinkedList()
    # Iterates through each friendship tuple
    for friendship in friendships:
        name1, name2 = friendship
        # Adds name1 if not in list
        if name1 not in linked_list:
            linked_list.add(name1)
        # Adds name2 if not in list
        if name2 not in linked_list:
            linked_list.add(name2)
        node1 = linked_list.find(name1)
        node2 = linked_list.find(name2)
        node1.friends.add(name2)
        node2.friends.add(name1)
    return linked_list

def find_mutual_friends(name1, name2, linked_list):
    '''
    Find mutual friends given 2 people
    Parameters:
        name1: A string name of the first person
        name2L A string name of the second person
        linked_list: A linked list of friendships
    Returns:
        None
    '''
    # Error if name1 not in list
    if name1 not in linked_list:
        print("ERROR: Unknown person", name1)
        return
    # Error if name2 not in list
    if name2 not in linked_list:
        print("ERROR: Unknown person", name2)
        return
    mutual_friends = []
    node1 = linked_list.find(name1)
    node2 = linked_list.find(name2)
    # Iterate through friends
    for friend in node1.friends:
        # If friend of both, add to mutual friends list
        if friend in node2.friends:
            mutual_friends.append(friend)
    # If list not empty, print all mutual friends
    if mutual_friends:
        print("Friends in common:")
        for friend in sorted(mutual_friends):
            print(friend)
    else:
        return

def main():
    '''
    Main function to run the rest of the program
    Parameters: 
        None
    Returns: None
    '''
    file_name = input('Input file: ')
    friendships = read_input_file(file_name)
    linked_list = construct_linked_list(friendships)
    name1 = input('Name 1: ')
    name2 = input('Name 2: ')
    find_mutual_friends(name1, name2, linked_list)

main()
