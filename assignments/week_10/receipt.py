####################
# Date: 2022-11-19
# File: receipt.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 10 Prove Milestone: Handling Exceptions
# Prove that you can write a Python program that 
# handles exceptions, including FileNotFoundError, 
# PermissionError, and KeyError.
#####################

"""
Prove 09 - Part 1
1. Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
2. Prints the products_dict.
3. Opens the request.csv file for reading.
4. Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
    a. Use the requested product number to find the corresponding item in the products_dict.
    b. Print the product name, requested quantity, and product price.

Prove 10 - Part 2
1. Print the store name at the top of the receipt.
2. Print the list of ordered items.
3. Sum and print the number of ordered items.
4. Sum and print the subtotal due.
5. Compute and print the sales tax amount. Use 6% as the sales tax rate.
6. Compute and print the total amount due.
7. Print a thank you message.
8. Get the current date and time from your computer's operating system and print the current date and time.
9. Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""

import csv
from datetime import datetime
import random


# Bold ANSI 
bold_s = '\033[1m'
bold_e = '\033[0m'

store_name = (f''' 
{"*":*^50}
{bold_s}*{"Welcome to WolfCo":^48}*{bold_e}
{"*":*^50}\n''')

header = (f'''{bold_s}{"Item":<18}{"Quantity":<10}{"Price":<10}{"Subtotal"}{bold_e}''')

thank_you_message = (f'''{"":<8}{"Thank You for Shopping With Us!"}''')

footer_message = (f'''\n{"":<13}{"*** CUSTOMER COPY ***"}\n''')

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
# Example code - Wed Nov  4 05:10:30 2020
current_date_and_time = datetime.now()
time_stamp = (f'''{"":<12}{current_date_and_time:%a %b %w %H:%M:%S %Y}\n''')
day_of_week = current_date_and_time.weekday()
current_time = current_date_and_time.strftime("%H:%M:%S")

def main():

    try:
        PRODUCT_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1

        # Calls the read_dict function
        # Prints the products_dict
        products_dict = read_dict("products.csv", PRODUCT_INDEX)
        # print(products_dict)

        # Opens the request.csv file for reading
        request_list = read_list("request.csv")
        # print(request_list)

        print(store_name)
        print(header)

        coupon_list = []
        items_sold = 0
        sub_total = 0
        for pn in request_list:
            product_number = pn[PRODUCT_INDEX]
            # print(product_number)
            quantity = pn[QUANTITY_INDEX]
            
            if product_number in products_dict:
                name = products_dict[product_number][NAME_INDEX]
                price = products_dict[product_number][PRICE_INDEX]

            items_sold += int(quantity)
            quantity_sub_total = (int(quantity)*float(price)) 
            sub_total += quantity_sub_total

            coupon_list.append(products_dict[product_number][NAME_INDEX])

            # Print the product name, requested quantity, and product price.
            print(f"""{name:<20} {quantity:<5} @ ${price:<8} ${quantity_sub_total:,.2f}""")
        
        # Print the subtotal for order
        print(f'''\n{"":<28}{"SUBTOTAL":<10} ${sub_total:,.2f}''')

        # Discount for day of week Tuesday=1 or Wednesday = 2
        if (day_of_week == 1 or day_of_week == 2):
            discount = round(sub_total * 0.10, 2)
            sub_total = sub_total - discount
            print(f'''{"":<12}{"Day of the Week Discount":<26} ${discount:,.2f}''')
        
        # Discount for time of day - before 11:00 am and not on Tuesday or Wednesday
        if ((day_of_week != 1 and day_of_week != 2) and current_time < "11:00:00"):
            discount = round(sub_total * 0.10, 2)
            sub_total = sub_total - discount
            print(f'''{"":<12}{"Time of Day Discount":<26} ${discount:,.2f}''')

        # Compute sales tax @ 6%
        tax_rate = .06
        sales_tax_total = sub_total * tax_rate
        print(f'''{"":<18}{"Sales Tax":<12}{"@ 6%":<8} ${sales_tax_total:,.2f}''')

        # Compute sale total
        total = sub_total + sales_tax_total
        print(f'''{"":<28}{"TOTAL":<10} ${total:,.2f}''')

        # Total items sold
        print(f'''\n{"":<15}{"# ITEMS SOLD":<5} {items_sold}\n''')

        # get unique item from request list
        # randomly, create a coupon for it
        coupon_item = coupon_code(coupon_list)
        print(f"""\n{"":<5}{"25% Off Next Purchase of "}{coupon_item.title()}\n""")

        print(thank_you_message)
        print(time_stamp)
        print(footer_message)


    except (FileNotFoundError, PermissionError) as error:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist or does not have permissions for.
        print()
        print(type(error).__name__, error, sep=": ")
        print("Please choose a different file.\n")
        
    except KeyError as error:
        print()
        print(type(error).__name__, error, sep=": ")
        print("Unknown product ID in the request.csv file\n")



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

def coupon_code(list):
    """Get the unique values from request.csv.
    Parameter
        list:  a list of all the values from request.csv
    Return: random item from unique_list
    """
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return random.choice(unique_list)


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

