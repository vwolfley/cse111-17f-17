####################
# Date: 2022-11-23
# File: pupils.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 11 Team Activity: Functional Programming
# Reinforce the concept that a function can be 
# passed as an argument into another function.
#####################

"""
Assignment
The CSV file named pupils.csv contains data about 100 students. 
Unfortunately, the data is not sorted. As a team, write a 
program that reads the contents of pupils.csv into a compound 
list, sorts the list by birthday from oldest to youngest, 
and then prints the list with the data about each student on a separate line.
"""

import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    try:
        # 4a - call function and read file into new list
        students_list = read_compound_list("pupils.csv")
        # print(students_list)

        # 4b - lambda function that will extract the birthdate from a student.
        # student_birthdate = lambda birthdays: birthdays[BIRTHDATE_INDEX]

        # Stretch Challenge 1
        # sorts the students_list by given name.
        student_given_name = lambda given_name: given_name[GIVEN_NAME_INDEX]
        # sorted_list = sorted(students_list, key=student_given_name)

        # Stretch Challenge 2
        # sorts the students_list by birth month and day
        def student_month_day(students_list):
            student_birthdate = students_list[BIRTHDATE_INDEX]
            student_month_day = student_birthdate[5:]
            return student_month_day

        sorted_list = sorted(students_list, key=student_month_day)

        # 4c - Write a call to the Python built-in sorted function that will 
        # sort the students_list by birthdate from oldest to youngest.
        # sorted_list = sorted(students_list, key=student_birthdate)

        # 4d - Print the students_list by calling the print_list function.
        print_list(sorted_list)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(list):
    """takes a list as a parameter and prints 
    each element of the list on a separate line

    Parameter list: 
    Return: prints each element on a separate line
    """
    for student in list:
        print(student)




if __name__ == "__main__":
    main()