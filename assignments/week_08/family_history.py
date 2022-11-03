####################
# Date: 2022-11-03
# File: family_history.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 08 Team Activity: Dictionaries
# write a Python program that stores data about individuals
# in one dictionary and stores data about marriages in a 
# different dictionary. Your program must combine the data 
# in the two dictionaries and print the combined data so that 
# it is understandable to a user.
#####################

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    # print('\n{0:<14} {1}'.format('Name', 'Age at Death'))

    # print('\n{0:<14} {1:<12} {2:<2} {3}'.format('Name', 'Age at Death', "Born", "Died"))
    for key, value in people_dict.items():

        name = value[NAME_INDEX]
        birth = value[BIRTH_YEAR_INDEX]
        death = value[DEATH_YEAR_INDEX]

        # print(f"{name:<18} {death-birth}")

    # Stretch Challenges
    # Add code to the print_death_age function that prints the birth year and death year for each person.
        print(f"{name:<18} Age: {death-birth:<3} Born: {birth:<5} Died: {death}")

def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male = 0
    female = 0

    for key, value in people_dict.items():
        gender = value[GENDER_INDEX]

        if gender == "M":
            male += 1
        elif gender == "F":
            female += 1

    print(f'''
    Males = {male}
    Females = {female}''')

def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """

# The name and age in the wedding year of the husband
# The year of the wedding
# The name and age in the wedding year of the wife
    
    for key, value in marriages_dict.items():

        husband_key = value[HUSBAND_KEY_INDEX]
        wife_key = value[WIFE_KEY_INDEX]
        wedding_year = value[WEDDING_YEAR_INDEX]

        # find husband info from people dictionary
        husband = people_dict[husband_key]
        husband_name = husband[NAME_INDEX]
        husband_birth = husband[BIRTH_YEAR_INDEX]

        # find wife info from people dictionary
        wife = people_dict[wife_key]
        wife_name = wife[NAME_INDEX]
        wife_birth = wife[BIRTH_YEAR_INDEX]

        # husband age at wedding
        husband_age = wedding_year - husband_birth

        # wife age at wedding
        wife_age = wedding_year - wife_birth

        print(f"{husband_name} at age ({husband_age}) married {wife_name} at age ({wife_age}) in {wedding_year}")

# Stretch Challenge
# Add to your program a function named count_marriages that counts 
# and prints the number of marriages that each person had in his 
# or her lifetime. According to the data, who married the most times?

def count_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, 
    counts and prints the number of marriages that 
    each person had in his or her lifetime

    Parameters
    marriages_dict: a dictionary that contains data about
    marriages. Each item in the dictionary is in this format:
    marriage_key: [husband_key, wife_key, wedding_year]
    people_dict: a dictionary that contains data about people
    Each item in the dictionary is in this format:
    person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """

    # Add a new column to people_dict with value of 0
    for key, value in people_dict.items():
        value.append(0)
    # print(people_dict)
    
    # Name of new column index in people_dict
    NUM_MARRIAGES_INDEX = 4

    # Loop though marriage_dict, find names of husbands and wifes
    # Count how many marriages they were assigned and increment count
    for key, value in marriages_dict.items():

        husband_key = value[HUSBAND_KEY_INDEX]
        wife_key = value[WIFE_KEY_INDEX]

        # find husband info from people dictionary
        husband = people_dict[husband_key]
        husband_name = husband[NAME_INDEX]
        husband[NUM_MARRIAGES_INDEX] += 1

        # find wife info from people dictionary
        wife = people_dict[wife_key]
        wife_name = wife[NAME_INDEX]
        wife[NUM_MARRIAGES_INDEX] += 1

    for key, value in people_dict.items():
        name = value[NAME_INDEX]
        marriage_count = value[NUM_MARRIAGES_INDEX]
        
        print(f"{name} - {marriage_count}")

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
