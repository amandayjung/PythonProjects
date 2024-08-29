'''
File: population.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: Reads a file which has the names of places and
their populations. It prints out the population and its' 
corresponding state while also giving the total population.
'''

def read_population_file(file_name):
    ''' 
    Reads the population file. It determines which lines are
    important and formats the information
    Parameters:
        file_name: The name of the file 
    Returns:
        info_tuple: A tuple with locatoins and populations
    '''
    # Initializes important variables
    total_pop = 0
    locations = 0
    populations = []
    # Open and read file
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    # Goes through every line in the file
    for line in lines:
        line = line.strip()
        # Keep going if line doesn't start with hashtag
        if line and not line.startswith('#'):
            # Splits every line into 2 parts
            parts = line.split()
            if len(parts) >= 2:
                state_territory = ' '.join(parts[:-1])
                population_str = parts[-1]
                # Check if the population is a number
                if population_str.isdigit():
                    # Convert population to an integer
                    population = int(population_str)
                # Update count 
                    locations += 1
                    total_pop += population
                # Add the location and population to the list
                    populations.append((state_territory, population))
    info_tuple = populations, (locations, total_pop)
    return info_tuple

def print_population_info(location_populations, summary):
    '''
    Prints population information and summary
    Parameters:
        location_populations: List of location tuples
        summary: Tuple with the total number of places and total population
    Returns: 
        None
    '''
    # Print formatted location and population info
    for location_population in location_populations:
        state_territory = location_population[0]
        population = location_population[1]
        print("State/Territory:", state_territory)
        print("Population:", population)
        print()
    # Print formatted summary info
    print("# of States/Territories:", summary[0])
    print("Total Population:", summary[1])

def main():
    '''
    The main function which runs the rest of the program.
    Additionally, it asks for user input. 
    Parameters:    
        None
    Returns:
        None
    '''
    file_name = input("file: ").strip()
    populations_summary = read_population_file(file_name)
    populations = populations_summary[0]
    summary = populations_summary[1]
    print_population_info(populations, summary)

main()
