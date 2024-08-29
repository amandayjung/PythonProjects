'''
File: linked_list.py
Author: Amanda Jung
Course: CSC 120, Spring 2024
Purpose: Defines methods and classes for linked lists
'''

class Node:
    '''
    A node in a linked list
    '''
    def __init__(self, name):
        '''
        Initialize node with name
        Parameters:
            self: Self
            name: Name of node
        Returns: None
        '''
        self.name = name
        self.friends = LinkedList()
        self.next = None

class LinkedList:
    '''
    Represents linked list of nodes
    '''
    def __init__(self):
        '''
        Initializes new linked list
        Parameters:
            self: Self
        Returns: 
            None
        '''
        self.head = None

    def add(self, name):
        '''
        Adds new node to linked list
        Parameters:
            self: Self
            name: Name of new node
        '''
        new_node = Node(name)
        # Checks if linked list is empty
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Goes through list until last node
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, name):
        '''
        Finds and returns node given a name
        Parameters:
            self: Self
            name: Name to find
        Returns: 
            current: Node that matches given name
            None: None if no node is found
        '''
        current = self.head
        while current:
            # If name matches
            if current.name == name:
                return current
            current = current.next
        return None

    def __contains__(self, name):
        '''
        Checks if node exists 
        Parameters: 
            self: Self
            name: Name of node to find
        Returns: 
            is_in: Trur or false if name is found
        '''
        is_in = self.find(name) is not None
        return is_in

    def __iter__(self):
        '''
        Iterates over names in list
        Parameters: 
            self: Self
        Returns: 
            None
        '''
        current = self.head
        names = []
        while current:
            names.append(current.name)
            current = current.next
        iterated = iter(names)
        return iterated

    def __str__(self):
        '''
        String conversion of linked list
        Parameters:
            self: Self
        Returns: 
            result_string: Final string of linked list
        '''
        result_list = []  
        # Iterates over items
        for name in self:  
            result_list.append(str(name)) 
        result_string = ' -> '.join(result_list)  
        return result_string
