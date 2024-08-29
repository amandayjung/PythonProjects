'''
File: linked_list_recursion_long.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of the program is to showcase various
uses of recursion with linked lists. array_to_list_recursive(data) 
uses recursion to convert an array into a linked list. accordion_recursive(head)
uses recursion to remove every other node from a linked list. Finally, 
pair_recursive(head1,head2) uses recursion to take nodes from 2 different linked
lists and pair them into tuples before putting them into a new linked list. 
'''

import list_node

def array_to_list_recursive(data):
    '''
    Uses recursion to convert an array into a linked_list
    Parameters:
        data: A list of data to turn into linked list nodes
    Returns: 
        head: The head of the new linked list
    '''
    # Checks if data is empty
    if not data:
        return None
    head = list_node.ListNode(data[0])
    # Checks if there's only one thing in data
    if len(data) > 1:
        head.next = array_to_list_recursive(data[1:])
    return head

def accordion_recursive(head):
    '''
    Uses recursion to remove every other node from a linked list
    Parameters:
        head: Head of the linked list
    Returns: 
        None: None if the list is empty
        new_head: The head of the accordion list
    '''
    # Checks if the linked list is empty
    if head is None or head.next is None:
        return None
    new_head = head.next
    new_head.next = accordion_recursive(head.next.next)
    return new_head

def pair_recursive(head1, head2):
    '''
    Uses recursion to pair elements from two different
    linked lists into pairs of tuples
    Parameters: 
        head1: The head of the first linked list
        head2: The head of the second linked list
    Returns: 
        new_head: The head of the new linked list with
        pairs of tuples in it
    '''
    # Checks if either list is empty
    if not head1 or not head2:
        return None
    new_head = list_node.ListNode((head1.val, head2.val))
    new_head.next = pair_recursive(head1.next, head2.next)
    return new_head
