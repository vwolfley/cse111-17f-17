###########################
# Date: 2022-12-10
# File: schools_grades.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose:  Write a significant Python project
###########################

### Reference Docs
#     - https://towardsdatascience.com/advanced-tips-on-how-to-read-csv-files-into-pandas-84ebb170f6e5
#     - https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Data Reference
ethnicity_column_dict = {
    'Fiscal Year': ["FiscalYear","int64"], 
    'LEA Name': ["DistrictName","object"],
    'LEA Entity ID': ["DistrictEntityID","float64"],
    'School Name': ["SchoolName","object"],
    'School Entity ID': ["SchoolEntityID","float64"],
    'Asian': ["Asian","float64"],
    'American Indian/Alaskan Native': ["NativeAmerican","float64"],
    'Black/African American': ["Black","float64"],
    'Hispanic/Latino': ["Hispanic","float64"],
    'White': ["White","float64"],
    'Native Hawaiian/Pacific Islander': ["PacificIslander","float64"],
    'Multiple Races': ["Multiracial","float64"],
    'Total': ["Total", "float64"]
}


def main():

    try:
        ### Import files
        file_name = "schools_by_ethnicity.csv"
        import_date = date.today()

        ethnicity_df = read_enrollment_ethnicity(file_name)
        # shape = ethnicity_df.shape
        # print(shape)

        # Show first five rows of data
        # Check data structure and column names
        # print(ethnicity_df.head())

        # Call change_column_names
        e_df = change_column_names(ethnicity_df, ethnicity_column_dict)
        # print(e_df.head())

        # Call check_for_nulls
        ee_df = check_for_nulls(e_df)
        # print(ee_df.head())

        # Call check_length_of_data
        check_length_of_data(ee_df)
 
        # Call check_for_duplicates
        check_for_duplicates(ee_df)

        # Call count_unique_sites
        count_unique_sites(ee_df)

        # Call add_schoolyear
        add_schoolyear(ee_df)
        # print(ee_df.head())

        # Call add_county_fields
        add_county_fields(ee_df)
        # print(ee_df.head())

        # Call add_import_date 
        add_import_date(ee_df, import_date)
        print(ee_df.head())

        # Call export_to_csv
        export_to_csv(ee_df, file_name="schools_by_ethnicity_update")

    except (FileNotFoundError, PermissionError) as error:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist or does not have permissions for.
        print()
        print(type(error).__name__, error, sep=": ")
        print("Please choose a different file.\n")


def read_enrollment_ethnicity(file_name):
    """Read the contents of a cvs file into a dataframe and
    return the dataframe. Each element in the dataframe will contain
    one line of text from the csv file.

    Parameters
        filename: the name of the csv file to read
    Return: a dataframe that contains two-dimensional data and its corresponding labels.
    """
    # Read in file data
    # the CSV file indicates missing data with the "*" in the column
    # use na_values to filter out and add null
    df = pd.read_csv(file_name, na_values=["*"])
    # Print out the dataframe info
    print(df.info())
    # Return the dataframe that contains the lines from csv.
    return df

def change_column_names(dataframe, dictionary):
    """Change column names to standardized database names

    Parameters
        dataframe: the name of the dataframe to test
        dictionary: the name of the dictionary for data
    Return: a new dataframe with column names ready for database.
    """
    # define new dataframe for connivance
    df = dataframe
    # read ethnicity_column_dict and create names_dict
    NAME_INDEX = 0
    names_dict = {}
    for key, value in dictionary.items():
        names_dict[key] = value[NAME_INDEX]
    # change column headers based on dictionary values
    # Rename column names
    for key, value in names_dict.items():
        for name in df.columns:
            if name == key:
                df.rename(columns={name : value}, inplace=True)
    return df

def check_for_nulls(dataframe):
    """Check columns that are not float or int for null values.

    Parameters
        dataframe: the name of the dataframe to test
    Return: a new dataframe with column names ready for database.
    """
    # define new dataframe for connivance
    df = dataframe

    for column in df:
        types = df[column].dtypes
        if types != "float" and types != "int":
            # Find the row and column in dataframe with null values
            nu = df[df[column].isnull()]
            # print(column)
            # print(nu)
            # Replace null values with blanks
            df[column] = df[column].fillna('')
            # print(df.head())

    return df

def check_length_of_data(dataframe):
    """Check the max length of the data length in columns 
    that are not float or int for null values.
    This insures that they will load into database correctly.

    Parameters
        dataframe: the name of the dataframe to test
    Return: NOTHING
    """
    # define new dataframe for connivance
    df = dataframe
    length_list = []
    for name in df.columns:
        ob = list(df.select_dtypes(include=['object']).columns)
        if name in ob:
            length = df[name].map(len).max()
            length_list.append(length)
            print(f"Column: {name:>8}, length = {length}")
    print()
    print(df.info())
    return length_list

def check_for_duplicates(dataframe):
    """Check for duplicate values in columns SchoolEntityID and DistrictEntityID
    This is a data integrity check.

    Parameters
        dataframe: the name of the dataframe to test
    Return: NOTHING
    """
    # define new dataframe for connivance
    df = dataframe

    # identify duplicate rows
    # count duplicate values in points column
    print()
    sl = len(df["SchoolEntityID"])-len(df["SchoolEntityID"].drop_duplicates())
    dl = len(df["DistrictEntityID"])-len(df["DistrictEntityID"].drop_duplicates())
    print(f"DistrictEntityID # Duplicate Values: {dl}")
    print(f"SchoolEntityID # Duplicate Values: {sl}")
    print()

def count_unique_sites(dataframe):
    """Find the number of unique values in columns SchoolEntityID and DistrictEntityID
    This is a data integrity check.

    Parameters
        dataframe: the name of the dataframe to test
    Return: NOTHING
    """
    # define new dataframe for connivance
    df = dataframe
    print()
    schools = len(df["SchoolEntityID"].unique())
    districts = len(df["DistrictEntityID"].unique())
    print(f"Schools Count: {schools}")
    print(f"Districts Count: {districts}")
    print()

def add_schoolyear(dataframe):
    """Add the column named "SchoolYear" and the data to dataframe
    Data should be the data from column "FiscalYear" ["FiscalYear -1"- "FiscalYear"]

    Parameters
        dataframe: the name of the dataframe
    Return: new dataframe
    """
    # define new dataframe for connivance
    df = dataframe

    currentfy = df["FiscalYear"].unique()
    lastyear = currentfy[0]-1
    schoolyear = f"{lastyear}-{currentfy[0]}"
    df["SchoolYear"] = schoolyear

    return df

def add_county_fields(dataframe):
    """Add the columns named "CountyEntityID" and "CountyName" to the dataframe
    Empty data fields

    Parameters
        dataframe: the name of the dataframe
    Return: new dataframe
    """
    # define new dataframe for connivance
    df = dataframe
    # Add fields to dataframe
    df["CountyEntityID"] = ""
    df["CountyName"] = ""

    return df

def add_import_date(dataframe, import_date):
    """Add the columns named "ImportDate" and the date to the dataframe
    The import date is the date the data was imported and checked.

    Parameters
        dataframe: the name of the dataframe
        import_date: the date of the import
    Return: new dataframe
    """
    # define new dataframe for connivance
    df = dataframe
    # Add field to dataframe
    # and import date to fill column
    df["ImportDate"] = import_date

    return df

def export_to_csv(dataframe, file_name):
    """Export the final dataframe to csv file

    Parameters
        dataframe: the name of the dataframe
    Return: csv file
    """
    # define new dataframe for connivance
    df = dataframe

    # Add file name
    # Drop the dataframe index = index=False
    # Add specific encoding sencoding='utf-8'
    csv = df.to_csv(file_name, encoding='utf-8', index=False)

    return csv

# If this file was executed like this:
# > project.py
# then calls the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
