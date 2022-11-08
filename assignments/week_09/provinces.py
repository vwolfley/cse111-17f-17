####################
# Date: 2022-11-08
# File: provinces.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 09 Checkpoint: Text Files
# Writing a program that reads the contents of a text file
# into a list and then changes some of the values in the list.
#####################

""" 
1. Open the provinces.txt file for reading.
2. Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
3. Print the entire list.
4. Remove the first element from the list.
5. Remove the last element from the list.
6. Replace all occurrences of "AB" in the list with "Alberta".
7. Count the number of elements that are "Alberta" and print that number.
"""

def main():

    province_list = read_file("provinces.txt")
    
    # Print the entire list.
    print(province_list)

    # Remove the first element from the list.
    province_list.pop(0)
    # print()
    # print(province_list)

    # Remove the last element from the list.
    province_list.pop()
    # print()
    # print(province_list)

    # Replace all occurrences of "AB" in the list with "Alberta".
    for idx, item in enumerate(province_list):
        if item == "AB":
            province_list[idx] = "Alberta"
    print()
    print(province_list)

    # Count the number of elements that are "Alberta" and print that number.
    count = province_list.count("Alberta")
    print()
    print(count)

def read_file(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    print(filename)
    province_list = []

    with open(filename, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            province_list.append(clean_line)

    # Return the list that contains the lines of text.
    return province_list


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()