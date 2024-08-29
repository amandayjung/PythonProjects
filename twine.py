'''
File: twine.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The purpose of this program is to simulate the
journey of a person as they travel through the forest and 
unroll a ball of twine along their travels. Current position, 
previous positions, and obstables are mapped out. 
'''

def print_prompt(position, history):
    '''
    Prints current position, position history, 
    and asks the user for the next command
    Parameters:
        position: The current coordinate position
        history: A list of previous coordinates
    Returns:
        None
    '''
    print("Current position:", position)
    print("Your history:    ", history)
    print("What is your next command?")

def move(position, direction):
    '''
    Finds the new position coordinates based on
    the direction
    Parameters:
        position: The current position coordinates
        direction: The direction of movement
    Returns: 
        A new pair of coordinates indicating position
    '''
    x, y = position
    # Check which direction to move
    if direction == 'n':
        return (x, y + 1)
    elif direction == 's':
        return (x, y - 1)
    elif direction == 'e':
        return (x + 1, y)
    elif direction == 'w':
        return (x - 1, y)
    else:
        return position

def print_error(message):
    '''
    Prints the formatted error message
    Parameters:
        message: The error message to print
    Returns:    
        None
    '''
    print("ERROR:", message)

def crossings_count(history, position):
    '''
    Counts the number of times a specific position
    is repeated in the history of coordinates
    Parameters: 
        history: A list of coordinates previously visited
        position: The position to be checked for repitition
    Returns: 
        count: The number of times the position is
        in the history
    '''
    count = 0
    # For every time the position is seen, add to count
    for p in history:
        if p == position:
            count += 1
    return count

def print_map(history, position, obstacles):
    '''
    Prints the map of positions, history, and obstacles
    Parameters:
        history: List of previously visited positions
        position: Current position coordinates
        obstacles: Coordinates of obstance positions
    Retuns:
        None
    '''
    grid_size = 11
    origin = (0, 0)
    offset = grid_size // 2
    grid = []
    # Initialize grid
    for x in range(grid_size):
        row = []
        # Fill rows with spaces
        for y in range(grid_size):
            row.append(' ')
        grid.append(row)
    # History of positions
    for (x, y) in history:
        grid_y = y + offset
        grid_x = x + offset
        # Check if in bounds
        if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
            grid[grid_y][grid_x] = '.'
    # Obstacle positions
    for (x, y) in obstacles:
        grid_y = y + offset
        grid_x = x + offset
        # Check if in bounds
        if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
            grid[grid_y][grid_x] = 'X'
    px, py = position
    grid[py + offset][px + offset] = '+'
    # If currently not ar origin
    if position != origin:
        grid[offset][offset] = '*'
    print("+-----------+")
    # Print each row
    for row in reversed(grid):
        print("|" + "".join(row) + "|")
    print("+-----------+")

def print_ranges(history):
    '''
    Prints the range of movement of the twine, 
    regardless of the direction
    Parameters:
        history: A list of coordinates previously
        visited
    Returns: 
        None
    '''
    x_positions = []
    y_positions = []
    # Collect all positions in history
    for pos in history:
        x_positions.append(pos[0])
        y_positions.append(pos[1])
    min_x = min(x_positions)
    max_x = max(x_positions)
    min_y = min(y_positions)
    max_y = max(y_positions)
    print("The furthest West your twine goes is " + str(min_x))
    print("The furthest East your twine goes is " + str(max_x))
    print("The furthest South your twine goes is " + str(min_y))
    print("The furthest North your twine goes is " + str(max_y))

def read_obstacles(filename):
    '''
    Reads and returns positions of obstacles
    Parameters:
        filename: The name of the file
        which contains obstacle positions
    Returns: 
        obstacles: Coordinates of the obstacle positions
    '''
    obstacles = set()
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    # For every line in the file
    for line in lines:
        parts = line.split()
        # Checks for 2 parts
        if len(parts) == 2:
            x, y = int(parts[0]), int(parts[1])
            obstacles.add((x, y))
    return obstacles

def main():
    '''
    The main function to run the rest of the program and
    ensure there are no errors
    Parameters: 
        None
    Returns: 
        None
    '''
    print("Please give the name of the obstacles filename, or - for none:")
    obstacle_filename = input().strip()
    obstacles = set()
    # Checks for obstacles
    if obstacle_filename != '-':
        obstacles = read_obstacles(obstacle_filename)
    history = [(0, 0)]
    position = (0, 0)
    while True:
        print_prompt(position, history)
        try:
            user_data = input()
        except:
            break
        # Checks for empty input
        if not user_data:
            print("You do nothing.\n")
            continue
        parts = user_data.split()
        # Checks for valid command
        if len(parts) != 1:
            print_error("Invalid command format")
            continue
        cmd = parts[0]
        # Checks for valid direction
        if cmd in ['n', 's', 'e', 'w']:
            new_position = move(position, cmd)
            # Checks if new position is obstacle
            if new_position in obstacles:
                print("You could not move in that direction, because there is an obstacle in the way.")
                print("You stay where you are.")
            else:
                history.append(new_position)
                position = new_position
        # Checks if back
        elif cmd == 'back':
            if len(history) > 1:
                history.pop()
                position = history[-1]
                print("You retrace your steps by one space")
            else:
                print("Cannot move back, as you are at the start!")
        # Checks if crossing
        elif cmd == 'crossings':
            count = crossings_count(history, position)
            print("There have been " + str(count) + " times in the history when you were at this point.")
        # Checks if map
        elif cmd == 'map':
            print_map(history, position, obstacles)
        # Checks if ranges
        elif cmd == 'ranges':
            print_ranges(history)
        # Print error if invalid command
        else:
            print_error("Invalid command: " + cmd)
        print()  

main()
