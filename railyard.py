'''
File: railyard.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: The program simulates managing a train yard where you 
sort and move train cars and locomotives between tracks. 
Each track can hold a mix of cars and one locomotive, and the 
locomotive is always to the right of the cars. Commands are for 
moving cars and locomotives between tracks, automatically leaving 
if all cars on a track are going to the same place. The program 
reads a file, performes commands from a user, and prints the 
trainyard, alerting when a train leaves or if errors happen.
'''

def read_file(filename):
    '''
    Reads the text file and retrieves the tracks
    Parameters: 
        filename: The name of the file
    Returns: 
        tracks: The tracks taken from the file
    '''
    tracks = []
    try:
        file = open(filename, "r")
        # Loops each line in the file and appends after stripping
        for part_of_tracks in file:
            tracks.append(part_of_tracks.strip("\n"))
    except: 
        print("ERROR: Could not open the yard file")
    return tracks

def check_lowercase(string):
    '''
    Checks to see if a string has only lowercase letters
    Parameters:
        string: The string to be checked
    Returns: 
        only_lower: A true or false of whether the string 
        constains lowercase letters or not
    '''
    in_a_row = 0
    # If string is empty
    if not string:
        return False
    char_bunch = ''.join(string)
    # If string has 1 character
    if len(char_bunch) == 1:
        return True
    current = char_bunch[0]
    # Loops through each character in the string
    for string in char_bunch:
        # Check if lowercase
        if string.islower():
            # Check if the same as previous
            if string == current:
                in_a_row += 1
            else:
                return False
        else:
            return False  
    only_lower = in_a_row >= 1
    return only_lower

def track_info(track):
    '''
    Gets the information from a track without the dashes
    Parameters:
        track: The track in the form of a string
    Returns: 
        data: A list of characters in the track
    '''
    data = []
    index = 0
    # Skip dashes at start of track
    while index < len(track) and track[index] == '-' :
        index += 1
    no_dash_track = track[index:-1]
    # Loop each letter in the dash-less string
    for letter in no_dash_track:
        data.append(letter)
    # Reverse list
    data = data[::-1]
    return data

def dump(tracks):
    '''
    Prints a detailed formatted track
    Parameters:
        tracks: A list of tracks
    Returns: 
        None
    '''
    # Loops through each track
    for track in range(len(tracks)):
        content = track_info(tracks[track])
        print("Track #" + str(track))
        print(" Length: " + str(len(tracks[track]) - 2))
        print(" Contents: " + str(content) + "\n")

def check_command(command, tracks):
    '''
    Checks for a valid user command
    Parameters: 
        command: A command to check if valid
        tracks: A list of tracks
    Returns:
        None: None if there is no problem with the command
        ERROR: An Error message
    '''
    user_cmd = command[0]
    # Checks if user command is valid
    if user_cmd.lower() not in ["quit", "dump", "move"]:
        return "ERROR: The only valid command formats are (where each \
            X represents an integer):\nmove X X X\nquit\n"
    # Checks if quit command is valid
    if user_cmd == "quit":
        if len(command) != 1:
            return "ERROR: The only valid command formats are (where each \
            X represents an integer):\nmove X X X\nquit\n"
        return None
    # Checks if move command is valid
    if user_cmd == "move":
        if len(command) != 4:
            return "ERROR: The only valid command formats are (where each \
            X represents an integer):\nmove X X X\nquit\n"
        return check_move_command(command, tracks)
    return None

def check_move_command(command, tracks):
    '''
    Checks if the "move" command is valid
    Parameters:
        command: A command to check if valid
        tracks: A list of tracks
    Returns: 
        None: None if there is no problem with the command
        ERROR: An Error message
    '''
    try:
        to_move, curr_location, move_to_loc = int(command[1]), int(command[2])\
            , int(command[3])
        # Checks track numbers
        if curr_location < 1 or move_to_loc < 1 or curr_location > len(tracks) or \
            move_to_loc > len(tracks):
            return "ERROR: The to-track or from-track number is invalid."
        # Check if current track has locomotive
        if track_info(tracks[curr_location - 1])[0] != "T":
            return "ERROR: Cannot move from track " + str(curr_location) + \
                " because it doesn't have a locomotive."
        # Checks if going to same track
        if curr_location == move_to_loc:
            return "ERROR: The 'to' track is the same as the 'from' track."
        # Checks if track has locomotive
        if "T" in tracks[move_to_loc - 1]:
            return "ERROR: Cannot move to track " + str(move_to_loc) + \
                " because it already has a locomotive."
        # Check for enough cars to move
        if to_move > len(track_info(tracks[curr_location - 1])) - 1:
            return "ERROR: Cannot move " + str(to_move) + " cars from track " \
                + str(curr_location) + " because it doesn't have that many cars."
        # Checks for negative number of cars to move
        if to_move < 0:
            return "ERROR: Cannot move a negative number of cars."
        contents_of_other_line = track_info(tracks[move_to_loc - 1])
        leftover = (len(tracks[0]) - 2) - len(contents_of_other_line)
        # Checks for enough space in future track
        if to_move >= leftover:
            return "ERROR: Cannot move " + str(to_move) + " cars to track " +\
                  str(move_to_loc) + " because it doesn't have enough space."
    except:
        return exception_for_move_command(command)
    return None

def exception_for_move_command(command):
    '''
    Runs the exception for the unfinished "check_move_command" function
    Parameters: 
        command: A command to check if valid
    Returns: 
        None: None if there is no error
        ERROR: An Error message
    '''
    to_move, curr_location, move_to_loc = command[1], command[2]\
            , command[3]
    # Checks if to_move is a number
    if not to_move.isnumeric():
        return "ERROR: Could not convert the 'count' value to an integer: '" + \
            to_move + "'\n"
    # Checks if curr_location is a number
    if not curr_location.isnumeric():
        return "ERROR: Could not convert the 'from-track' value to an integer: '" + \
            curr_location + "'\n"
    # Checks if move_to_loc is a number
    if not move_to_loc.isnumeric():
        return "ERROR: Could not convert the 'to-track' value to an integer: '" \
            + move_to_loc + "'\n"
    return None

def track_print(tracks):
    '''
    Prints current tracks
    Parameters:
        tracks: A list of tracks
    Returns:
        None
    '''
    # Loops through each track
    for piece_of_track in range(len(tracks)):
        print(str(piece_of_track + 1) + ": " + str(tracks[piece_of_track]))

def move(count, start, final):
    '''
    Moves cars from one track to another and changes tracks
    to match the move
    Parameters: 
        count: The number of cars to move
        start: The track to move from
        final: The track to move to
    Returns: 
        old_and_new: A tuple with the old and new tracks
    '''
    starter = "".join(track_info(start))
    ender = "".join(track_info(final))
    counter = int(count)
    # Shows new and old tracks when no cars are moved
    if counter == 0:
        new = starter[0] + ender
        new += "-" * (len(start) - len(new) - 1)
        old = starter[1:] + "-" * (len(start) - len(starter[1:]) - 1)
    # Shows new and old tracks when cars are moved
    else:
        new = starter[:count + 1] + ender
        new += "-" * (len(start) - len(new) - 1)
        old = starter[count + 1:]
        old += "-" * (len(start) - len(old) - 1)
    old_and_new = old[::-1] + "-", new[::-1] + "-"
    return old_and_new

def leave(cars, track):
    '''
    Checks if the number of cars given can leave the track
    Parameters:
        cars: The number of cars
        track: The track to be checked
    Returns: 
        cars_equal_max: True or False if the number of cars equals the max
    '''
    track_to_check = track_info(track)
    curr = 1
    maximum = 1
    # Checks for empty track
    if len(track_to_check) <= 1 or "T" not in track_to_check:
        return False
    # Loops tracks to find maximum number of cars
    for  x in range(1, len(track_to_check)):
        if track_to_check[x] == track_to_check[x - 1]:
            curr += 1
        else:
            maximum = max(maximum, curr)
            curr = 1
    maximum = max(maximum, curr)
    cars_equal_max = cars == maximum
    return cars_equal_max

def clear_tracks(tracks):
    '''
    Checks if the tracks are clear of locomotives
    Parameters: 
        tracks: A list of tracks
    Returns: 
        True: If tracks are clear
        False: If tracks are not clear
    '''
    # Loops over all tracks
    for x in tracks:
    # If locomotive in track, it's not clear
        if 'T' in x:
            return False
    return True

def count_loco(tracks):
    '''
    Counts how many locomotives are on all the tracks
    Parameters: 
        tracks: A list of tracks
    Returns: 
        None
    '''
    counter = 0
    # Loops over all tracks
    for track in tracks:
        for letter in track:
        # Check for locomotive
            if letter == "T":
                counter += 1
    print("Locomotive count: " + str(counter))

def dest_count(track):
    '''
    Counts the number of destinations in all tracks
    Parameters:
        track: A track in the form of a string
    Returns: 
        None
    '''
    chars = set()
    # Loop over every letter in track
    for x in track:
        for letter in x:
            # Checks for lowercase destination letters
            if letter.islower():
                chars.add(letter)
    print("Destination count: " + str(len(chars)) + "\n")

def all_characters_are_dashes(list_of_strings):
    '''
    Checks if all characters in a list of strings are dashes
    Parameters: 
        list_of_strings: A list of strings to check for all dashes
    Returns:
        True: If all characters are dashes
        False: If not all characters are dashes
    '''
    # Iterate through all strings
    for x in list_of_strings:
        for char in x:
            # Checks if a character isn't a dash
            if char != '-':
                return False
    return True

def work_with_dump(tracks):
    '''
    Works with the dump command by printing information and track.
    Parameters:
        tracks: A list of tracks
    Returns:
        None
    '''
    print("DEBUG OUTPUT:")
    dump(tracks)
    track_print(tracks)
    count_loco(tracks)
    dest_count(tracks)

def work_with_move(command, tracks):
    '''
    Works with the move command by moving cars from one track to another
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
    Returns:
        after_move: A tuple with tracks after the move
    '''
    cars_to_move = int(command[1])
    cars_to = tracks[int(command[3]) - 1]
    cars_from = tracks[int(command[2]) - 1]
    after_move = move(cars_to_move, cars_from, cars_to)
    # Update tracks
    tracks[int(command[2]) - 1] = after_move[0]
    tracks[int(command[3]) - 1] = after_move[1]
    return after_move

def move_alerts(command, tracks, after_move):
    '''
    Works with alerts and prints information for move 
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
        after_move: A tuple with tracks after the move
    Returns:
        True: If the last locomotive has left
        False: If the last locomotive hasn't left
    '''
    print("The locomotive on track", command[2], "moved", command[1], \
          "cars to track", command[3], ".\n")
    track_print(tracks)
    # Departing alert
    print("*** ALERT*** The train on track", command[3], ", which had", \
          len(track_info(after_move[1])) - 1, "cars, departs for destination", \
          track_info(after_move[1])[-1], ".\n")
    tracks[int(command[3]) - 1] = "-" * len(tracks[0])
    # Check if tracks are clear
    if clear_tracks(tracks):
        print("The last locomotive has departed!\n")
        track_print(tracks)
        count_loco(tracks)
        dest_count(tracks)
        return True
    track_print(tracks)
    count_loco(tracks)
    dest_count(tracks)
    return False

def handle_no_alerts(command, tracks, after_move):
    '''
    Works with move when no specific alert is triggered 
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
        after_move: A tuple with tracks after the move
    Returns:
        True: If the last locomotive has left
        False: If the last locomotive hasn't left
    '''
    endpoint = track_info(tracks[int(command[2]) - 1])[1]
    print("The locomotive on track", command[2], "moved", command[1], \
          "cars to track", command[3], ".\n")
    for track in range(len(tracks)):
        print(str(track + 1) + ": " + str(tracks[track]))
    new_len = len(track_info(after_move[1])) - 1
    # Departing alert
    print("*** ALERT*** The train on track", command[3], ", which had", \
          new_len, "cars, departs for destination", endpoint, ". \n")
    tracks[int(command[3]) - 1] = "-" * len(tracks[0])
    # Checks if tracks are clear
    if clear_tracks(tracks):
        print("The last locomotive has departed!\n")
        track_print(tracks)
        return True
    track_print(tracks)
    return False

def move_messages(command, tracks, after_move):
    '''
    Works with move messages and finds the right alert or status
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
        after_move: A tuple with tracks after the move
    Returns:
        True: If the last locomotive has left
        False: If the last locomotive hasn't left
    '''
    # Check if move causes alert
    if "T" in after_move[1] and check_lowercase(track_info(after_move[1])[1:]):
        return move_alerts(command, tracks, after_move)
    # Check if move causes no specific alert
    elif leave(int(command[1]), tracks[int(command[2]) - 1]) and \
        not check_lowercase(track_info(after_move[1])[1:]):
        return handle_no_alerts(command, tracks, after_move)
    else:
        # Print move details and statuses if no alert
        print("The locomotive on track", command[2], "moved", command[1], \
              "cars to track", command[3], ".")
        track_print(tracks)
        count_loco(tracks)
        dest_count(tracks)
        return False

def overall_move_command(command, tracks):
    '''
    Works with the move command by doing the move operation and 
    then getting the move messages
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
    Returns:
        resulting_move_messages
    '''
    after_move = work_with_move(command, tracks)
    resulting_move_messages = move_messages(command, tracks, after_move)
    return resulting_move_messages

def process_command(command, tracks):
    '''
    Processes commands by doing the action based on the command 
    Parameters:
        command: Commands from the user
        tracks: A list of tracks
    Returns:
        True: If command quitting or an overall move command is successful
        False: If there is an error 
    '''
    # Process dump command
    if command[0] == 'dump':
        work_with_dump(tracks)
    else:
        # Checks for error message
        error_message = check_command(command, tracks)
        # If there is an error message
        if error_message:
            print(error_message)
            track_print(tracks)
            count_loco(tracks)
            dest_count(tracks)
            return False
        # Process quit message
        elif command[0] == 'quit':
            print("Quitting!")
            return True
        # Process move command
        elif command[0] == 'move':
            if overall_move_command(command, tracks):
                return True
    return False

def main():
    '''
    The main function to help the rest of the program run smoothly
    Parameters:
        None
    Returns: 
        None
    '''
    filename = input("Please give the yard file: \n")
    tracks = read_file(filename)
    track_print(tracks)
    count_loco(tracks)
    dest_count(tracks)
    dont_quit = True
    while dont_quit:
        # Get/split up user command
        command = input("What is your next command?\n").strip().split()
        if process_command(command, tracks):
            # Exit loop during a successful quit command
            dont_quit = False

main()
