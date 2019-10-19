'''
This project takes data from a file that contains information on a geographic location and presents different
options of manipulating the data or displaying it. The program prompts the users with a menu that lists the
different options available. Some examples of those options are printing the average daily, maximum, and low
temperature, or printing data for a random locality. Once one option is executed, the menu will pop back up allowing
the user to choose another function. The user may quit if they so please by enter 'Q' in the menu.

Coded by Kyle Hagerstrom
'''

import random

# Takes data from provided file and returns 2D list
def read_file_to_array(file_name):
    data = []
    infile = open(file_name)
    for line in infile:  # iterates through each line in the input file
        data.append(line.rsplit(", "))
    infile.close()
    return data


# Function will return the average daily temperature
def average_daily(data_arr):
    counter = 0
    average = 0

    for i in range(len(data_arr)):
        for j in range(1, 3):
            average += int(data_arr[i][j])
            counter += 1
    average /= counter
    return average

# Function will return the average high temperature
def average_high(data_arr):
    average = 0
    for entry in data_arr: # entry = sublist
        average += int(entry[2])

    average /= len(data_arr)
    return average

# Function will return the average low temperature
def average_low(data_arr):
    average = 0
    for entry in data_arr:
        average += int(entry[1])

    average /= len(data_arr)
    return average

# Function will return the maximum temperature
def max_temp(data_arr):
    max = -999999999
    for entry in data_arr:
        if int(entry[2]) > max:
            max = int(entry[2])
    return max

# Function will return the minimum temperature
def min_temp(data_arr):
    min = 999999999
    for entry in data_arr:
        if int(entry[1]) < min:
            min = int(entry[2])
    return min

# Function will return the data from a random locality
def random_loc(data_arr):
    ran = random.randint(0, 4)
    return data_arr[ran]

# Function will prompt user to enter a location and then will return data from that location
def get_location(data_arr):
    loc = input("Enter a location: ") # (loc = location)
    output = []
    found = False

    for entry in data_arr: # This is searching for a match between the user input and a location within the 2D list
        if loc.lower() == entry[0].lower(): # Both are lower case to prevent errors due to strange capitalization
            output = entry
            found = True

    while not found: # If the user's location is not found, this is used to make the user try again
        loc = input("Invalid location, enter a location again: ")
        # This is the same loop as the one above but it's used again because the original loop must
        # run through once before prompting the 'invalid message'.
        for entry in data_arr:
            if loc.lower() == entry[0].lower(): # 'checks if ....'
                output = entry
                found = True

    return output

# Menu that prompts the user with options
def menu(data):
    print("---------------------------------------------------")
    print("To find the average daily temperature,     enter 1")
    print("To find the average high temperature,      enter 2")
    print("To find the average low temperature,       enter 3")
    print("To find the maximum temperature,           enter 4")
    print("To find the minimum temperature,           enter 5")
    print("To find the data for a random locality,    enter 6")
    print("To get the weather information for a city, enter 7")
    print("To display all data,                       enter 8")
    print("Type Q to quit.")
    print("---------------------------------------------------")
    print()
    user_choice = input("Enter an option: ")
    print()

    # Compares user input with a number, then calls the function that corresponds with that number in the menu
    if user_choice == "1":
        print("The average daily temp is:", average_daily(data))
        print()
        return True
    if user_choice == "2":
        print("The average high temp is:", average_high(data))
        print()
        return True
    if user_choice == "3":
        print("The average low temp is:", average_low(data))
        print()
        return True
    if user_choice == "4":
        print("The maximum temp is:", max_temp(data))
        print()
        return True
    if user_choice == "5":
        print("The minimum temp is:", min_temp(data))
        print()
        return True
    if user_choice == "6":
        print("The data for a random locality:", random_loc(data))
        print()
        return True
    if user_choice == "7":
        print(get_location(data))
        print()
        return True
    if user_choice == "8":
        print(data)
        print()
        return True
    if user_choice.lower() == "q":
        return False
    else:
        print("Invalid input")
        print()
        return True

# Prompts user to enter file name. Keeps the program running until user enters 'Q' and makes run False
def main():
    data_file = input("Enter name of file: ")
    data = read_file_to_array(data_file)
    run = True
    while run:
        run = menu(data)
    print("Goodbye")


main()
