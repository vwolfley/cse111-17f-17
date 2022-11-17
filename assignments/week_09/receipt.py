####################
# Date: 2022-11-12
# File: receipt.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 09 Prove Milestone: Text Files
# Prove that you can write a Python program that
# reads CSV files and creates, populates, and uses a dictionary.
#####################

"""
1. Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
2. Prints the products_dict.
3. Opens the request.csv file for reading.
4. Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
    a. Use the requested product number to find the corresponding item in the products_dict.
    b. Print the product name, requested quantity, and product price.
"""


import csv

def main():

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    QUANTITY_INDEX = 1

    products_dict = read_dict("products.csv", PRODUCT_INDEX)
    print(products_dict)
    print()

    request_list = read_list("request.csv")
    # print(request_list)

    for pn in request_list:
        product_number = pn[PRODUCT_INDEX]
        # print(product_number)
        quantity = pn[QUANTITY_INDEX]
        
        if product_number in products_dict:
            name = products_dict[product_number][NAME_INDEX]
            price = products_dict[product_number][PRICE_INDEX]

        print(f"""{name:<15} {quantity:<2} @ ${price}""")
            


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

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    request_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)

        # Read the contents of the text
        # file one line at a time.
        for line in reader:

            # Append the clean line of text
            # onto the end of the list.
            request_list.append(line)

    # Return the list that contains the lines of text.
    return request_list



# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

