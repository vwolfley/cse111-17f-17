####################
# Date: 2022-10-26
# File: random_numbers.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 07 Team Activity: Lists
# Demonstrates both default parameter 
# values and pass by reference.
#####################

"""
Assignment:
As a team, write a Python program named random_numbers.py that creates a 
list of numbers, appends more numbers onto the list, and prints the list. 
The program must have two functions named main and append_random_numbers.
1. main
    a. Has no parameters
    b. Creates a list named numbers like this:
        numbers = [16.2, 75.1, 52.3]
    c. Prints the numbers list
    d. Calls the append_random_numbers function with only one argument to add one number to numbers
    e. Prints the numbers list
    f. Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    g. Prints the numbers list
2. append_random_numbers
    a. Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1
    b. Computes quantity pseudo random numbers by calling the random.uniform function.
    c. Rounds the quantity pseudo random numbers to one digit after the decimal.
    d. Appends the quantity pseudo random numbers onto the end of the numbers_list.
At the bottom of your program, write an if statement that calls the main function. Then run your program and verify that your program works correctly.
"""

import random

def main():
    #####################
    # Core Requirements
    #####################
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers = {numbers}")

    append_random_numbers(numbers)
    print(f"numbers = {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers = {numbers}")

    #######################
    # Stretch Challenges
    #######################

    words = ["fun", "play", "football", "games"]
    print(f"words = {words}")

    append_random_words(words)
    print(f"words {words}")

    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    '''Appending random numbers to the numbers list
    Parameter
        numbers_list: a list of numbers
        quantity: an integer.
            The default is 1
    Return: none
    '''
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):
    '''Appending random words to the words list
    Parameter
        words_list: a list of words
        quantity: an integer.
            The default is 1
    Return: none
    '''
    new_words = ["bakery","ears","know","press","ten","ball","earth","ladies","price","test","bank","east","lady","private","text","base","easy","lake","probably","than","be","eat","land","problem","that","bear","edge","language","produce","the"]
    for _ in range(quantity):
        random_words = random.choice(new_words)
        words_list.append(random_words)




# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()