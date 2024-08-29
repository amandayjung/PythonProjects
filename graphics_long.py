'''
File: graphics_long.py
Author: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of this program is to showcase
the ability to import graphics and use that to create 
a creative animation. The goal is to animate 4 stick
men dancing. This is done through various functions, 
which include making a background, bent and unbent 
dancing frames, etc. 
'''

import graphics

def background(win):
    '''
    The background which will be shown throughout
    the dance cycle. It is a sky, grass, and the sun
    Parameters:
        win: The graphics window
    Returns:
        None
    '''
    # The sky
    win.rectangle(0, 0, 500, 350, "light blue")
    # The grass
    win.rectangle(0, 350, 500, 500, "green")
    win.line(0, 350, 500, 350, "black", 1)
    # The sun
    win.ellipse(100, 100, 60, 60, "yellow")

def default_stick_man(win, x, y):
    '''
    Create the default stick man who
    is standing right side up
    Parameters:
        win: The graphics window
        x: The x coordinates for the stick man
        y: The y coordinates for the stick man
    Returns:    
        None
    '''
    # His head
    win.ellipse(x, y, 80, 80, "white")
    # His back
    win.line(x, y+40, x, y+180, "black", 1)
    # His arms
    win.line(x, y+60, x+40, y+130, "black", 1)
    win.line(x, y+60, x-40, y+130, "black", 1)
    # His legs
    win.line(x, y+180, x+40, y+250, "black", 1)
    win.line(x, y+180, x-40, y+250, "black", 1)

def bent_default_stick_man(win, x, y):
    '''
    Create the default stick man who
    is bending his knees
    Parameters:
        win: The graphics window
        x: The x coordinates for the stick man
        y: The y coordinates for the stick man
    Returns:    
        None
    '''
    # His head
    win.ellipse(x, y, 80, 80, "white")
    # His back
    win.line(x, y+40, x, 380, "black", 1)
    # His arms
    win.line(x, y+60, x+40, y+130, "black", 1)
    win.line(x, y+60, x-40, y+130, "black", 1)
    # His legs
    win.line(x-40, 400, x, 450, "black", 1)
    win.line(x+40, 400, x, 450, "black", 1)
    win.line(x, 380, x+40, 400, "black", 1)
    win.line(x, 380, x-40, 400, "black", 1)

def default_frame(win):
    '''
    Uses other functions to put together the default 
    frame in which 4 stick men are standing upright
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    default_stick_man(win, 100, 200)
    default_stick_man(win, 200, 200)
    default_stick_man(win, 300, 200)
    default_stick_man(win, 400, 200)

def bent_default_frame(win):
    '''
    Uses other functions to put together the default 
    frame in which 4 stick men are dancing with their
    knees bent
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    bent_default_stick_man(win, 100, 250)
    bent_default_stick_man(win, 200, 250)
    bent_default_stick_man(win, 300, 250)
    bent_default_stick_man(win, 400, 250)

def frame_y(win):
    '''
    The creates a frame in which the first 
    stick man is standing upright with his
    hands creating a "Y" and the rest of the
    men are standing upright
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    y_man(win)
    default_stick_man(win, 200, 200)
    default_stick_man(win, 300, 200)
    default_stick_man(win, 400, 200)

def bent_frame_y(win):
    '''
    The creates a frame in which the first 
    stick man is bending at the knees with his
    hands creating a "Y" and the rest of the
    men are bent at the knees
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    bent_y_man(win)
    bent_default_stick_man(win, 200, 250)
    bent_default_stick_man(win, 300, 250)
    bent_default_stick_man(win, 400, 250)

def y_man(win):
    '''
    Creates a man standing upright and making
    a "Y" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 100
    y = 200
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, y+180, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x, y+180, x+40, y+250, "black", 1)
    win.line(x, y+180, x-40, y+250, "black", 1)

def bent_y_man(win):
    '''
    Creates a man bending at the knees and
    making a "Y" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 100
    y = 250
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, 380, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x-40, 400, x, 450, "black", 1)
    win.line(x+40, 400, x, 450, "black", 1)
    win.line(x, 380, x+40, 400, "black", 1)
    win.line(x, 380, x-40, 400, "black", 1)

def frame_m(win):
    '''
    The creates a frame in which the first 
    stick man is standing upright with his
    hands creating a "Y", the second man is 
    upright with his arms making an "M" and 
    the rest of the men are standing upright
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    y_man(win)
    m_man(win)
    default_stick_man(win, 300, 200)
    default_stick_man(win, 400, 200)

def bent_frame_m(win):
    '''
    The creates a frame in which the first 
    stick man is bending at the knees with his
    hands creating a "Y", the second man is 
    bending with his arms making an "M" and 
    the rest of the men are bent at the knees
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    bent_y_man(win)
    bent_m_man(win)
    bent_default_stick_man(win, 300, 250)
    bent_default_stick_man(win, 400, 250)

def m_man(win):
    '''
    Creates a man standing upright and making
    an "M" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 200
    y = 200
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back 
    win.line(x, y+40, x, 380, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x-40, y-20, x, y, "black", 1)
    win.line(x+40, y-20, x, y, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x, y+180, x+40, y+250, "black", 1)
    win.line(x, y+180, x-40, y+250, "black", 1)

def bent_m_man(win):
    '''
    Creates a man bending at the knees and
    making an "M" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 200
    y = 250
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, 380, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x-40, y-20, x, y, "black", 1)
    win.line(x+40, y-20, x, y, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x-40, 400, x, 450, "black", 1)
    win.line(x+40, 400, x, 450, "black", 1)
    win.line(x, 380, x+40, 400, "black", 1)
    win.line(x, 380, x-40, 400, "black", 1)

def frame_c(win):
    '''
    The creates a frame in which the first 
    stick man is bending at the knees with his
    hands creating a "Y", the second man is 
    bent with his arms making an "M", the
    thirs man is bent with his arms making
    a "C", and the last man is bent. 
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    y_man(win)
    m_man(win)
    c_man(win)
    default_stick_man(win, 400, 200)

def bent_frame_c(win):
    '''
    The creates a frame in which the first 
    stick man is standing upright with his
    hands creating a "Y", the second man is 
    upright with his arms making an "M", the
    thirs man is upright with his arms making
    a "C", and the last man is standing upright
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    bent_y_man(win)
    bent_m_man(win)
    bent_c_man(win)
    bent_default_stick_man(win, 400, 250)

def c_man(win):
    '''
    Creates a man standing upright and making
    a "C" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 300
    y = 200
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, y+180, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y+130, "black", 1)
    win.line(x, y+60, x+40, y-10, "black", 1)
    # Legs
    win.line(x, y+180, x+40, y+250, "black", 1)
    win.line(x, y+180, x-40, y+250, "black", 1)

def bent_c_man(win):
    '''
    Creates a man bending at the knees and
    making a "C" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 300
    y = 250
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, 380, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y+130, "black", 1)
    win.line(x, y+60, x+40, y-10, "black", 1)
    # Legs
    win.line(x-40, 400, x, 450, "black", 1)
    win.line(x+40, 400, x, 450, "black", 1)
    win.line(x, 380, x+40, 400, "black", 1)
    win.line(x, 380, x-40, 400, "black", 1)

def frame_a(win):
    '''
    The creates a frame in which all the
    stick men are standing upright making their
    respective letters with their arms
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    y_man(win)
    m_man(win)
    c_man(win)
    a_man(win)

def bent_frame_a(win):
    '''
    The creates a frame in which all the
    stick men are bent over and making their
    respective letters with their arms
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    background(win)
    bent_y_man(win)
    bent_m_man(win)
    bent_c_man(win)
    bent_a_man(win)

def a_man(win):
    '''
    Creates a man standing upright and making
    an "A" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 400
    y = 200
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, y+180, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x-40, y-20, x, y-80, "black", 1)
    win.line(x+40, y-20, x, y-80, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x, y+180, x+40, y+250, "black", 1)
    win.line(x, y+180, x-40, y+250, "black", 1)

def bent_a_man(win):
    '''
    Creates a man bending at the knees and
    making an "A" with his arms
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # Coordinates
    x = 400
    y = 250
    # Head
    win.ellipse(x, y, 80, 80, "white")
    # Back
    win.line(x, y+40, x, 380, "black", 1)
    # Arms
    win.line(x, y+60, x+40, y-20, "black", 1)
    win.line(x-40, y-20, x, y-80, "black", 1)
    win.line(x+40, y-20, x, y-80, "black", 1)
    win.line(x, y+60, x-40, y-20, "black", 1)
    # Legs
    win.line(x-40, 400, x, 450, "black", 1)
    win.line(x+40, 400, x, 450, "black", 1)
    win.line(x, 380, x+40, 400, "black", 1)
    win.line(x, 380, x-40, 400, "black", 1)
    
def starting_frames(win):
    '''
    Loops through the starting sequence, which
    is simply the stick men standing and bending
    their knees in place without moving their arms
    Parameters:
        win: The graphics window
    Returns:
        None
    '''
    x = 0
    # Men stand and bend 3 times
    for x in range(3):
        default_frame(win)
        win.update_frame(2)
        win.clear()
        bent_default_frame(win)
        win.update_frame(2)
        win.clear()
        x += 1

def wait_and_wipe(win):
    '''
    Holds the frame for a moment before wiping
    the image to make room for the next one
    Parameters:
        win: The graphics window
    Returns: 
        None
    '''
    win.update_frame(2)
    win.clear()

def dance(win):
    '''
    Loops the dancing sequence until the window is closed
    Parameters: 
        win: The graphics window
    Returns: 
        None
    '''
    # While window isn't closed
    while not win.is_destroyed():
        starting_frames(win)
        frame_y(win)
        wait_and_wipe(win)
        bent_frame_y(win)
        wait_and_wipe(win)
        frame_m(win)
        wait_and_wipe(win)
        bent_frame_m(win)
        wait_and_wipe(win)
        frame_c(win)
        wait_and_wipe(win)
        bent_frame_c(win)
        wait_and_wipe(win)
        frame_a(win)
        wait_and_wipe(win)
        bent_frame_a(win)
        wait_and_wipe(win)

def main():
    '''
    The main function whichs allows the rest of
    the program to run smoothly. Creates the graphics
    window and calls to the dance. 
    Parameters:
        None
    Returns: 
        None
    '''
    win = graphics.graphics(500, 500, "Graphics Long (Dance)")
    dance(win)
    win.mainloop()

main()
