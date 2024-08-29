'''
Amanda Jung
CSC 110
Project - 1
This program has several functions which return the areas of multiple different shapes
'''

def rectangle_area(base, height):
    '''
    This function returns the product of its' parameters
    Args:
      base: The measurment for the base of the rectangle
      height: The measurment for the height of the rectangle
    Returns: 
        rect_area: The area of the rectangle, base multiplied by height
    '''
    rect_area = base*height
    return rect_area

def triangle_area(a, b, c):
    '''
    This function gathers the 3 measurements given and uses them as lengths of a triangle, proceeding to find the area of that triangle
    Args:
        a = The first length of the triangle
        b = The second length of the triangle
        c = The third length of the triangle
    Returns:
        tri_area = The area of the triangle assuming a, b, and c are the triangle's lengths
    '''

    # x is a variable used in the equation in order to find the area of a triangle
    x = (a+b+c)/2
    tri_area = (x*(x-a)*(x-b)*(x-c))**(1/2)
    return tri_area

def trapezoid_area(base_1, base_2, height):
    '''
    This function finds the half of the sum of the 2 bases multiplied by the height of a trapezoid
    Args:
        base_1 = The first base of the trapezoid
        base_2 = The second base of the trapezoid
        height = The height of the trapezoid
    Returns:
        trap_area = The area of the trapezoid based on the given measurements
    '''
    trap_area = (1/2)*(base_1+base_2)*height
    return trap_area

def circle_area(radius):
    '''
    This function returns the area of a circle rounded to 2 decimal places
    Args:
        radius = The measure of the radius of the circle
    Returns:
       rounded_cir_area = The rounded area of the circle
    '''

    # cir_area is the circle's rounded area
    cir_area = 3.1415*radius**2
    rounded_cir_area = round(cir_area,2)
    return rounded_cir_area
