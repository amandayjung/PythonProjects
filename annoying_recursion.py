'''
File: annoying_recursion.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
'''

def annoying_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4 * annoying_factorial(3)
    elif n == 5:
        return 5 * annoying_factorial(4)
    elif n == 6:
        return 6 * annoying_factorial(5)
    else:
        return n * annoying_factorial(n - 1)

def annoying_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    elif n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    elif n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    else:
        return annoying_fibonacci(n - 1) + annoying_fibonacci(n - 2)

def annoying_tree_of_tuples(n):
    if n == 0:
        return 0
    elif n == 1:
        return (0, 1, 0)
    elif n == 2:
        return ((0, 1, 0), 2, (0, 1, 0))
    elif n == 3:
        return (((0, 1, 0), 2, (0, 1, 0)), 3, ((0, 1, 0), 2, (0, 1, 0)))
    elif n == 4:
        return (annoying_tree_of_tuples(3), 4, annoying_tree_of_tuples(3))
    elif n == 5:
        return (annoying_tree_of_tuples(4), 5, annoying_tree_of_tuples(4))
    elif n == 6:
        return (annoying_tree_of_tuples(5), 6, annoying_tree_of_tuples(5))
    else:
        return (annoying_tree_of_tuples(n - 1), n, annoying_tree_of_tuples(n - 1))

def annoying_print_downUp(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
        annoying_print_downUp(0)
        print(1)
    elif n == 2:
        print(2)
        annoying_print_downUp(1)
        print(2)
    elif n == 3:
        print(3)
        annoying_print_downUp(2)
        print(3)
    elif n == 4:
        print(4)
        annoying_print_downUp(3)
        print(4)
    elif n == 5:
        print(5)
        annoying_print_downUp(4)
        print(5)
    elif n == 6:
        print(6)
        annoying_print_downUp(5)
        print(6)
    else:
        print(n)
        annoying_print_downUp(n - 1)
        print(n)
