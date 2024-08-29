'''
    File: battleship.py
    Author: Amanda Jung
    Course: CSC 120
    Purpose: Creates a game of battleship in which player one
    has set up ships on a grid and player 2 guesses the location
    of each ship. This is done using user inputs and lists.
'''

import sys

class GridPos:
    '''
        Describes the grid position
    '''

    def __init__(self, x, y):
        '''
        Initializes grid position
        Parameters:
            self: Self
            x: x coordinate
            y: y coordinate
        Returns:
            None
        '''
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False

    def __str__(self):
        '''
        Convertts into string
        Parameters:
            self: Self
        Return:
            None 
        '''
        return "({}, {})".format(self._x, self._y)

class Board:
    '''
        Tracks the progress of the 10x10 game board
    '''

    def __init__(self):
        '''
        Initializes board
        Parameters:
            self: Self
        Returns: 
            None
        '''
        self._grid = self.make_grid()
        self._ships = []

    def make_grid(self):
        '''
        Creates the 10x10 board
        Parameters:
            self: Self
        Returns:
            grid: The complete board
        '''
        grid = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(GridPos(x, y))
            grid.append(row)
        return grid

    def process_input_placement(self, line):
        '''
        Processes the input of the player
        Parameters:
            self: Self
            line: The line being checked
        Returns: 
            self._grid: The modified grid
        '''
        ship_type, x1, y1, x2, y2 = line.split()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # Checks if in grid
        if not (0 <= x1 < 10 and 0 <= y1 < 10 and 0 <=\
                 x2 < 10 and 0 <= y2 < 10):
            print("ERROR: ship out-of-bounds:", line)
            sys.exit(0)
        # Checks if verticle or horizontal
        if x1 != x2 and y1 != y2:
            print("ERROR: ship not horizontal or vertical:", line)
            sys.exit(0)
        size = abs(x2 - x1) + abs(y2 - y1) + 1
        # Checks size
        if ship_type == 'A' and size != 5:
            print("ERROR: incorrect ship size:", line)
            sys.exit(0)
        elif ship_type == 'B' and size != 4:
            print("ERROR: incorrect ship size:", line)
            sys.exit(0)
        elif ship_type in "S" and size != 3:
            print("ERROR: incorrect ship size:", line)
            sys.exit(0)
        elif ship_type in "D" and size != 3:
            print("ERROR: incorrect ship size:", line)
            sys.exit(0)
        elif ship_type == 'P' and size != 2:
            print("ERROR: incorrect ship size:", line)
            sys.exit(0)
        ship = Ship(ship_type, size, [x1, x2, y1, y2])
        # Checks if overlapping
        if x1 == x2:
            for y in range(size):
                min_val = min(y1, y2)
                if not self._grid[x1][min_val + y]._ship:
                    self._grid[x1][min_val + y]._ship = ship
                else:
                    print("ERROR: overlapping ship: ", line)
                    sys.exit(0)
        self._ships.append(ship)
        # Checks if overlapping
        if y1 == y2:
            for x in range(size):
                min_val = min(x1, x2)
                if not self._grid[min_val + x][y1]._ship:
                    self._grid[min_val + x][y1]._ship = ship
                else:
                    print("ERROR: overlapping ship: ", line)
                    sys.exit(0)
        return self._grid

    def fleet_composition(self):
        '''
        Checks for correct fleet composition
        Parameters:
            self: Self
        Returns: 
            None
        '''
        shipcount = {"A": 0, "P": 0, "D": 0, "B": 0, "S": 0}
        for placed_ship in self._ships:
            shipcount[placed_ship._ship_type] += 1
        if len(self._ships) != 5:
            print("ERROR: fleet composition incorrect")
            sys.exit()
        for count in shipcount.values():
            if count != 1:
                print("ERROR: fleet composition incorrect")
                sys.exit(0)
                
    def process_guess(self, line):
        '''
        Processes user 2's guess
        Parameters:
            self: Self
            line: The line being considered in the guess
        Returns: 
            None (Without illegal guessing)
        '''
        x, y = line.split()
        x,y = int(x), int(y)
        # Checks if in grid
        if not (0 <= x < 10 and 0 <= y < 10):
            print("illegal guess")
            return
        pos = self._grid[x][y]
        if pos._guessed:
            if pos._ship:
                print("hit (again)")
            else:
                print("miss (again)")
            return
        pos._guessed = True
        if not pos._ship:
            print("miss")
            return
        pos._ship._hits += 1
        if pos._ship._hits == pos._ship._size:
            print(f"{pos._ship._ship_type} sunk")
            self._ships.remove(pos._ship)
            if not self._ships:
                print("all ships sunk: game over")
                sys.exit(0)
        else:
            print("hit")

    def __str__(self):
        '''
        Converts board into string
        Parameters:
            self: Self
        Returns:
            result: 
                The current board
        '''
        result = ""
        for row in self._grid:
            for pos in row:
                if pos._ship:
                    result += pos._ship._ship_type
                else:
                    result += "."
                result += " "
            result += "\n"
        return result

class Ship:
    '''
        Represents a ship
    '''
    def __init__(self, ship_type, size, positions):
        '''
        Initializes ship
        Parameters:
            self: Self
            ship_type: The type of ship
            size: The ship size
            positions: The position of ship
        Returns: 
        '''
        self._ship_type = ship_type
        self._size = size
        self._positions = positions
        self._hits = 0

    def __str__(self):
        '''
        String conversion for ship
        Parameters:
            self: Self
        Returns:
            Formatted ship location
        '''
        return "({}, {})".format(self._x, self._y)
    
def main():
    '''
        The main function to run the program
    '''
    placement_file = input()
    file_name = open(placement_file, 'r')
    placement_lines = file_name.readlines()
    board = Board()
    for line in placement_lines:
        board.process_input_placement(line.strip())
    board.fleet_composition()
    guess_file = input()
    gfile_name = open(guess_file, 'r')
    guess_lines = gfile_name.readlines()
    for line in guess_lines:
        board.process_guess(line.strip())


main()
