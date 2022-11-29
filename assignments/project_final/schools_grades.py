####################
# Date: 2022-11-23
# File: schools_grades.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose:
#####################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ethnicity_column_names = ["FiscalYear", "DistrictName", "DistrictEntityID", "SchoolName", "SchoolEntityID",
                     "Asian", "NativeAmerican", "Black", "Hispanic", "White", "PacificIslander", "Multiracial", 
                     "MissingEthnicity", "Total"]

column_names = ['Fiscal Year', 'LEA Name', 'LEA Entity ID', 'School Name', 'School Entity ID', 'Asian',
                'American Indian/Alaskan Native', 'Black/African American', 'Hispanic/Latino', 'White',
                'Native Hawaiian/Pacific Islander', 'Multiple Races', 'Total']

ethnicity_column_dic = {
    'Fiscal Year': "FiscalYear", 
    'LEA Name': "DistrictName",
    'LEA Entity ID': "DistrictEntityID",
    'School Name': "SchoolName",
    'School Entity ID': "SchoolEntityID",
    'Asian': "Asian",
    'American Indian/Alaskan Native': "NativeAmerican",
    'Black/African American': "Black",
    'Hispanic/Latino': "Hispanic",
    'White': "White",
    'Native Hawaiian/Pacific Islander': "PacificIslander",
    'Multiple Races': "Multiracial",
    'Total': "Total"

}


file_name = "schools_by_ethnicity.csv"

# Read in file data
df = pd.read_csv(file_name)

# Show first five rows of data
head = df.head()
# print(head)

# List column names
print(df.columns)
# for col in df.columns:
# print(col)

# Gives number of rows
count_row = df.shape[0]
print(f"Total number of rows {count_row}")
# Gives number of columns
count_col = df.shape[1]
print(f"Total number of columns {count_col}")


# Rename column names
for key, value in ethnicity_column_dic.items():
    for name in df.columns:
        if name == key:
            df.rename(columns={name : value}, inplace=True)

print(df.columns)
print(df.head())

# apply the dtype attribute
column_type = df.dtypes
print(column_type)


# dNameLen = df["DistrictName"].map(len).max()
# print(dNameLen)

# dNameLen = df["Asian"].map(len).max()
# print(f"column Asian = {dNameLen}")

# for name in df.columns:
#     if df.dtypes[name] == object:
#         # length = df[name].map(len).max()
#         # print(f"Column: {name} length = {length}")
#         print(f"Column: {name:>15}, {df[name].dtypes}, length = ")


df.replace("*", np.nan, inplace=True)
print(df.head())
print(df.dtypes)

catagories = ["Asian", "NativeAmerican", "Black", "Hispanic", "White", "PacificIslander", "Multiracial", "Total"]

# convert column from object to float
for name in catagories:
    df[name] = df[name].astype(float)

print(df.head())
# print(df.dtypes)


# identify duplicate rows
duplicateRows = df[df.duplicated(["SchoolEntityID"])]
# print(duplicateRows)

# print(df["SchoolEntityID"].where(df["SchoolEntityID"] == NaN))

# selecting rows based on condition 
rslt_df = df.loc[df["SchoolEntityID"].isnull()] 
    
print('\nResult dataframe :\n', 
      rslt_df)

# ax = df.hist(column='Total', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)


# df.plot(kind = 'scatter', x = 'Total', y = 'Hispanic')

df["Total"].plot(kind = 'hist', bins=500)

plt.show()