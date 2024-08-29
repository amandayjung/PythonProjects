'''
File: linked_list_long.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: 
'''

import list_node

def is_sorted(head):
    '''
    Checks if the linked list is sorted from 
    the smallest to the largest number
    Parameters:
        head: The head of the linked list
    Returns: 
        True or False: 
    '''
    # Check if list empty or has 1 elemenet
    if head is None or head.next is None:
        return True
    current = head
    # Go through the list
    while current.next is not None:
        # Checks if element is greater than next one
        if current.val > current.next.val:
            return False
        current = current.next
    return True

def list_sum(head):
    '''
    Finds the sum of everything in the 
    linked list
    Parameters:
        head: The head of the linked list
    Returns: 
        total: The sum of every element in 
        the linked list
    '''
    total = 0
    current = head
    # Goes through the list
    while current is not None:
        # Adds each element to the total
        total += current.val
        current = current.next
    return total

def partition_list(head):
    '''
    Parts the list into 2 lists
    Parameters:
        head: The head of the linked list
    Returns: 
        A tuple of the 2 new heads
    '''
    # Checks if the list is empty
    if head is None:
        return None, None
    list1_head = list1_tail = None
    list2_head = list2_tail = None
    current = head
    # Toggles between the lists
    toggle = True 
    # Goes through the list
    while current is not None:
        # Saves the next node
        next_node = current.next
        # Add to the first list
        if toggle:
            if list1_tail is None:
                list1_head = list1_tail = current
            else:
                list1_tail.next = current
                list1_tail = current
        # Add to the second list
        else:
            if list2_tail is None:
                list2_head = list2_tail = current
            else:
                list2_tail.next = current
                list2_tail = current
        toggle = not toggle
        current.next = None  
        current = next_node
    return list1_head, list2_head

def accordion_3(head, start_pos):
    '''
    Creates a new list with every 3rd element
    considering a starting position
    Parameters:
        head: The head of the list
        start_pos: The position to start at
    '''
    # If list is empty
    if head is None:
        return None
    current = head
    # Go to starting position
    for _ in range(start_pos):
        # Checks if starting position is empty
        if current is None:
            return None
        current = current.next
    new_head = new_tail = current
    count = 0
    # Go through the list
    while current is not None:
        # Save the next node
        next_node = current.next
        count += 1
        # Checks if multiple of 3
        if count % 3 == 0:
            new_tail.next = next_node
            new_tail = next_node
        current = next_node
    if new_tail is not None:
        new_tail.next = None
    return new_head

def pair(list1, list2):
    '''
    Pairs elements from 2 lists into one list
    Parameters: 
        list1: The first list to pair
        list2: The second list to pair
    Returns: 
        big_head.next: The head of the new list
    '''
    big_head = list_node.ListNode(None)
    tail = big_head
    current1 = list1
    current2 = list2
    # Goes through list
    while current1 is not None and current2 is not None:
        # Creates new node with paired values
        new_node = list_node.ListNode((current1.val, current2.val))
        # Appends new node into the big list
        tail.next = new_node
        tail = new_node
        current1 = current1.next
        current2 = current2.next
    return big_head.next
