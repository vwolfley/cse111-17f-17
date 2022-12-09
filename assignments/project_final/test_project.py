####################
# Date: 2022-12-10
# File: test_project.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: Testing for project
#####################

from project import read_enrollment_ethnicity, add_schoolyear, change_column_names, check_length_of_data, check_for_nulls
import pandas as pd
import pytest


file_name = "schools_by_ethnicity.csv"

dictionary = {
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

def test_file_import():
    "Verify that the read_enrollment_ethnicity function works correctly."

    # Read the csv file into a pandas dataframe
    df = read_enrollment_ethnicity(file_name)
    # Verify that the dataframe contains at least one row.
    assert len(df.index) > 0
    # Verify that the dataframe contains all rows and columns expected
    assert df.shape == (2419, 13)

def test_change_column_names():
    "Verify that the column headers/names are all correct"

    # Original CSV column headers to test against
    org_col = ['Fiscal Year', 'LEA Name', 'LEA Entity ID', 'School Name',
               'School Entity ID', 'Asian', 'American Indian/Alaskan Native',
               'Black/African American', 'Hispanic/Latino', 'White',
               'Native Hawaiian/Pacific Islander', 'Multiple Races', 'Total']
    # New dataframe column headers to test against
    new_col = ["FiscalYear", "DistrictName", "DistrictEntityID", "SchoolName", "SchoolEntityID",
           "Asian", "NativeAmerican", "Black", "Hispanic", "White", "PacificIslander", "Multiracial", "Total"]
    # Read the csv file into a pandas dataframe
    # Only read in 5 rows of data and remove characters "*" and turn to NaN
    df = pd.read_csv(file_name, na_values=["*"], nrows=5)

    # Test original dataframe columns
    assert len(df.columns) == len(org_col)
    assert all([a == b for a, b in zip(df.columns, org_col)])
    # Test new dataframe columns
    ndf = change_column_names(df, dictionary)
    assert len(ndf.columns) == len(new_col)
    assert all([a == b for a, b in zip(ndf.columns, new_col)])
    

def test_check_length_of_data():
    """Verify that the column headers/names are all correct
    Checking_for_length function is dependent on the check_for_nulls function
    If nulls are found the in the check_for_length it will fail
    """

     # Read the csv file into a pandas dataframe
    # Only read in 5 rows of data and remove characters "*" and turn to NaN
    df = pd.read_csv(file_name, na_values=["*"])

    ndf = check_for_nulls(df)
    length = check_length_of_data(ndf)

    for x in length:
        assert x <= 100

def test_add_schoolyear():
    "Verify that the column is added and date is correct"

     # Read the csv file into a pandas dataframe
    # Only read in 5 rows of data and remove characters "*" and turn to NaN
    df = pd.read_csv(file_name, na_values=["*"])
    # Needs to have column names changed for add_schoolyear to work.
    ndf = change_column_names(df, dictionary)

    sdf = add_schoolyear(ndf)
    assert "SchoolYear" in sdf.columns

    # Verify that all the schoolyear numbers in the
    # SchoolYear column are the correct number.
    for value in df["SchoolYear"]:
        assert value == "2021-2022"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
