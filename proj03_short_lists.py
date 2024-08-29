'''
File: proj03_short_lists.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
'''
import list_node

def list_to_array(head):
    array = []
    current = head
    while current is not None:
        array.append(current.val)
        current = current.next
    return array

def array_to_list(data):
    if not data:
        return None
    head = list_node.ListNode(data[0])
    current = head
    for value in data[1:]:
        current.next = list_node.ListNode(value)
        current = current.next
    return head

def list_length(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length

def split_list(old_head):
    if old_head is None:
        return (None, None)
    length = list_length(old_head)
    mid = (length // 2) + (length % 2)
    current = old_head
    prev = None
    count = 0
    while current is not None and count < mid:
        prev = current
        current = current.next
        count += 1
    if prev is not None:
        prev.next = None
    return (old_head, current)
