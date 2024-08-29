'''
File: simple_classes.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of the whole program is to define 
several smaller classes in one big python file. The Simplest
class holds 3 fields and initializes them. The Rotate class 
rotates 3 values in a "round-robin" fashion. The Band class 
represents a band with a singer, drummer, and guitar players. 
It includes functions to get and set the singer and drummer, 
add and remove guitar players, and simulate the band playing 
music. Finally, the color class represents RGB values while 
including functions to ensure the color values are within
valid bounds, format them into a string and HTML hex, set 
to standard colors, and remove the red component. 
'''

class Simplest:
    '''
    A class to hold 3 public fields
    '''

    def __init__(self, a, b, c):
        '''
        Initializes the class with 3 public fields
        Parameters:
            self: Self
            a: The first value
            b: The second value
            c: The third value
        Returns: 
            None
        '''
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    '''
    Rotates the 3 values in a "round-robin" fashion
    '''

    def __init__(self, first, second, third):
        '''
        Initializes the 3 values
        Parameters:
            self: Self
            first: The first value
            second: The second value
            third: The third value
        Returns: 
            None
        '''
        self.values = [first, second, third]

    def get_first(self):
        '''
        Returns the first value
        Parameters:
            self: Self
        Returns: 
            self.values[0]: The first value
        '''
        return self.values[0]

    def get_second(self):
        '''
        Returns the second value
        Parameters:
            self: Self
        Returns: 
            self.values[2]: The second value
        '''
        return self.values[1]

    def get_third(self):
        '''
        Returns the third value
        Parameters:
            self: Self
        Returns: 
            self.values[2]: The third value
        '''
        return self.values[2]

    def rotate(self):
        '''
        Rotates the 3 values in a "round-robin" fashion
        Parameters: 
            self: Self
        Returns: 
            None
        '''
        # Moves the first value to the end
        self.values.append(self.values.pop(0))

class Band:
    '''
    A class that represents a band
    '''

    def __init__(self, singer):
        '''
        Initializes the band singer
        Parameters:
            self: Self
            singer: The band singer
        Returns: None
        '''
        self.singer = singer
        self.drummer = None
        self.guitar_players = []

    def get_singer(self):
        '''
        Returns the singer's name
        Parameters: 
            self: Self
        Returns: 
            self.singer: The singer's name
        '''
        return self.singer

    def set_singer(self, new_singer):
        '''
        Sets a new singer
        Parameters: 
            self: Self
            new_singer: The new singer's name
        Returns: 
            None
        '''
        self.singer = new_singer

    def get_drummer(self):
        '''
        Returns the drummer's name
        Parameters: 
            self: Self
        Returns: 
            self.drummer: The drummer's name
        '''
        return self.drummer

    def set_drummer(self, new_drummer):
        '''
        Sets a new drummer
        Parameters: 
            self: Self
            new_drummer: The new drummer's name
        Returns: 
            None
        '''
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        '''
        Adds a new guitar player to the band
        Parameters: 
            self: Self
            new_guitar_player: The name of the new guitar player
        Returns: 
            None
        '''
        self.guitar_players.append(new_guitar_player)

    def fire_all_guitar_players(self):
        '''
        Removes all the guitar players from the band
        Parameters:
            self: Self
        Returns: 
            None
        '''
        self.guitar_players = []

    def get_guitar_players(self):
        '''
        Returns a list of all guitar players in the band
        Parameters:
            self: Self
        Returns: 
            self.guitar_players[:]: All the guitar players in the band
        '''
        return self.guitar_players[:]

    def play_music(self):
        '''
        Simulates the band playing music
        Parameters:
            self: Self
        Returns: 
            None
        '''
        # Check if singer is Frank Sinatra
        if self.singer == "Frank Sinatra":
            print("Do be do be do")
        # Checks if singer is Kurt Cobain
        elif self.singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        # Checks if band has a drummer
        if self.drummer is not None:
            print("Bang bang bang!")
        # For every guitar player in the band, strum
        for x in self.guitar_players:
            print("Strum!")

class Color:
    '''
    A class representing a color
    '''

    def __init__(self, r, g, b):
        '''
        Initializes RGB values
        Parameters:
            self: Self
            r: Red value
            g: Green value
            b: Blue value
        Returns:
            None
        '''
        self.r = self.bound_value(r)
        self.g = self.bound_value(g)
        self.b = self.bound_value(b)

    def bound_value(self, value):
        '''
        Bounds the colors within a certain range
        Parameters:
            self: Self
            value: The color value to bound
        Returns: 
            0: If the color's value is less than 0
            255: If the color's value is more than 255
            value: The bounded color's value
        '''
        if value < 0:
            return 0
        elif value > 255:
            return 255
        else:
            return value

    def __str__(self):
        '''
        Returns the color as a string 
        Parameters: 
            self: Self
        Returns: 
            The color formatted as a string
        '''
        return "rgb(" + str(self.r) + "," + str(self.g) + "," + str(self.b) + ")"

    def html_hex_color(self):
        '''
        Returns the color in HTML hex
        Parameters: 
            self: Self
        Returns: 
            The color formatted in HTML hex
        '''
        r_hex = hex(self.r)[2:].upper()
        g_hex = hex(self.g)[2:].upper()
        b_hex = hex(self.b)[2:].upper()
        # Makes sure it's 2 digits
        if len(r_hex) < 2:
            r_hex = '0' + r_hex
        if len(g_hex) < 2:
            g_hex = '0' + g_hex
        if len(b_hex) < 2:
            b_hex = '0' + b_hex
        return "#" + r_hex + g_hex + b_hex

    def get_rgb(self):
        '''
        Returns the RGB values of the color
        Parameters: 
            self: Self
        Returns:
            A tuple with RGB values
        '''
        return (self.r, self.g, self.b)

    def set_standard_color(self, name):
        '''
        Sets color to standard color 
        Parameters:
            name: The name of the standard color
        Returns: 
            None
        '''
        colors = {
            "red": (255, 0, 0),
            "yellow": (255, 255, 0),
            "white": (255, 255, 255),
            "black": (0, 0, 0)
        }
        color = colors.get(name.lower())
        # Update if valid color 
        if color:
            self.r, self.g, self.b = color

    def remove_red(self):
        '''
        Removes the red part from the color
        Parameters:
            self: Self
        Returns:
            None
        '''
        self.r = 0
