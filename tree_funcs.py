'''
File: tree_funcs.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
'''

def tree_count(root):
    if root is None:
        return 0
    return 1 + tree_count(root.left) + tree_count(root.right)

def tree_count_1_child(root):
    if root is None:
        return 0
    count = 0
    if root.left is not None and root.right is None:
        count = 1
    elif root.left is None and root.right is not None:
        count = 1
    return count + tree_count_1_child(root.left) + tree_count_1_child(root.right)

def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

def tree_print(root):
    if root is None:
        return
    print(root.val)
    tree_print(root.left)
    tree_print(root.right)

def tree_print_leaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val)
    else:
        tree_print_leaves(root.left)
        tree_print_leaves(root.right)

def tree_search(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left_search = tree_search(root.left, val)
    if left_search is not None:
        return left_search
    return tree_search(root.right, val)

def tree_max(root):
    if root is None:
        return None
    left_max = tree_max(root.left)
    right_max = tree_max(root.right)
    max_val = root.val
    if left_max is not None:
        max_val = max(max_val, left_max)
    if right_max is not None:
        max_val = max(max_val, right_max)
    return max_val
