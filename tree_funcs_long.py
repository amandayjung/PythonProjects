'''
File: tree_funcs_long.py
Name: Amanda Jung 
Course: CSC 120, Summer 2024
Purpose: The purpose of the program is to showcase various
skills and uses of code involving trees and BSTs. This includes 
searching, inserting, and traversal functions. Functions to find 
the maximum value of a tree (or BST) are also included in the 
program. 
'''

import tree_node

def bst_search_loop(root, val):
    '''
    Uses a loop to search for a specific value in a BST
    Parameters: 
        root: The root node of the BST
        val: The value to be found
    Returns: 
        None: The value was not found in the BST
        current: The node that matches the value
    '''
    current = root
    # Traverse the tree until hit "None"
    while current is not None:
        # Check if the current node is the right value
        if current.val == val:
            return current
        # If the value is less, go to the left
        elif val < current.val:
            current = current.left
        # If the value isn't less, go right
        else:
            current = current.right
    return None

def tree_search(root, val):
    '''
    Uses recursion to search for a specific value in a BST
    Parameters: 
        root: The root node of the BST
        val: The value to be found
    Returns: 
        None: The value was not found in the BST
        root: The node that matches the value is the root
        left_result: If value is found in the left of tree
        tree_search(root.right, val): If value is found in
        the right of the tree
    '''
    # If tree is empty, return None
    if root is None:
        return None
    # If value is found at root, return root
    if root.val == val:
        return root
    # Recursively search left 
    left_result = tree_search(root.left, val)
    # If found in the left, return
    if left_result is not None:
        return left_result
    # Return when value found on the right
    return tree_search(root.right, val)

def bst_insert_loop(root, val):
    '''
    Uses a loop to insert a value into a BST
    Parameters: 
        root: The root node of the BST
        val: The value to insert
    Returns: 
        None
    '''
    current = root
    # Loop until the value is inserted
    while True:
        # If the value is less, go to the left
        if val < current.val:
            # If left child is None, insert value
            if current.left is None:
                current.left = tree_node.TreeNode(val)
                return
            current = current.left
        # If the value is greater/equal, go to the right
        else:
            # If right child is None, insert value
            if current.right is None:
                current.right = tree_node.TreeNode(val)
                return
            current = current.right

def pre_order_traversal_print(root):
    '''
    Does a pre-order traversal of the tree and prints
    the value of each node as it goes along
    Parameters: 
        root: The root node of the tree
    Returns:    
        None
    '''
    # As long as the root isn't None, print the value
    if root is not None:
        print(root.val)
        # Recursively traverse left
        pre_order_traversal_print(root.left)
        # Recursively traverse right
        pre_order_traversal_print(root.right)

def in_order_traversal_print(root):
    '''
    Does a in-order traversal of the tree and prints
    the value of each node as it goes along
    Parameters: 
        root: The root node of the tree
    Returns:    
        None
    '''
    # If root is not None, traverse the left
    if root is not None:
        in_order_traversal_print(root.left)
        print(root.val)
        # Recursively traverse right
        in_order_traversal_print(root.right)

def post_order_traversal_print(root):
    '''
    Does a post-order traversal of the tree and prints
    the value of each node as it goes along
    Parameters: 
        root: The root node of the tree
    Returns:    
        None
    '''
    # If root is not None, traverse the left
    if root is not None:
        post_order_traversal_print(root.left)
        # Recursively traverse right
        post_order_traversal_print(root.right)
        print(root.val)

def in_order_vals(root):
    '''
    Does a in-order traversal of the tree and returns
    a list of the node values
    Parameters: 
        root: The root of the tree
    Returns: 
        []: If the tree is empty
        node_vals: A list of values in the tree in order
    '''
    # If tree is empty, return an empty list
    if root is None:
        return []
    # Recursively get values from the left, add the root value, 
    # and then get values from the right 
    node_vals = in_order_vals(root.left) + [root.val] + in_order_vals(root.right)
    return node_vals

def bst_max(root):
    '''
    Find the maximum value in a BST
    Parameters: 
        root: The root node of the BST
    Returns: 
        current.val: The maximum value in the BST
    '''
    current = root
    # Traverse the right nodes 
    while current.right is not None:
        current = current.right
    return current.val

def tree_max(root):
    '''
    Finds the maximum value in a tree
    Parameters: 
        root: The root node of the tree
    Returns: 
        None: If the tree is empty
        current_max: The maximum value in the tree
    '''
    # If the tree is empty, return None
    if root is None:
        return None
    # Recursively find the maximum left value
    left_max = tree_max(root.left)
    # Recursively find the maximum right value
    right_max = tree_max(root.right)
    current_max = root.val
    # Check if the left value is larger than the right
    if left_max is not None:
        current_max = max(current_max, left_max)
    # Check if the right value is larger than the left
    if right_max is not None:
        current_max = max(current_max, right_max)
    return current_max
