####################
# Date: 2022-11-010
# File: students.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 09 Team Activity: CSV Files
# Writing a program that reads the contents of a text file
# into a list and then changes some of the values in the list.
#####################

"""
Core Requirements

1. Open the students.csv file for reading, skip the first line of text in the file 
    because it contains only headings, and read the other lines of the file into a dictionary. 
    The program must store each student I-Number as a key and each I-Number name pair or each 
    name as a value in the dictionary.
2. Get an I-Number from the user, use the I-Number to find the corresponding student name in 
    the dictionary, and print the name.
3. If a user enters an I-Number that doesn't exist in the dictionary, your program must print 
    the message, "No such student" (without the quotes).
"""

"""
Stretch Challenges

1. Add code to remove dashes from the I-Number that the user enters. This will allow the user to 
    enter I-Numbers with dashes or without dashes and still allow the computer to search in the dictionary.
2. When a user enters an I-Number, your program should ensure it is a valid I-Number.
    a. If there are too few digits in the I-Number, your program should print, "Invalid I-Number: too few digits" (without the quotes).
    b. If there are too many digits in the I-Number, your program should print, "Invalid I-Number: too many digits" (without the quotes).
    c. If the given I-Number contains any characters besides digits and dashes, your program should output "Invalid I-Number" (without the quotes).
3. Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.
"""

import csv

def main():
    NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict("students.csv", NUMBER_INDEX)
    # print(student_dict)
    
    student_number = None
    while True:
        student_number = input("Please enter the student ID number: ")
        # result = "323021604"
        # result = "323-021-60"

        # Stretch Challenge #1
        student_number = student_number.replace("-", "")
        # print(len(result))

        if not  student_number.isdigit():
            print("Invalid I-Number")
            continue  
        elif len(student_number) < 9:
            print("Invalid I-Number: too few digits")
            continue
        elif len(student_number) > 9:
            print("Invalid I-Number: too many digits")
            continue 
        elif student_number in student_dict:
            name = student_dict[student_number][NAME_INDEX]
            print(f"Student name is: {name}")
            break
        else:
            print("No such student")
            continue

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.

        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement 
        # skips the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary



# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()