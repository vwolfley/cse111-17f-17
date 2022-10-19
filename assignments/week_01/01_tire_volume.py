#####
# Date: 2022-09-17
# File: tire_volume.py
# Author: Vern Wolfley
# Purpose: Write a Python program named tire_volume.py 
# that reads from the keyboard the three numbers for 
# a tire and computes and outputs the volume of space 
# inside that tire.
#####

"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:
"""

"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches. 
"""

# Import math module
import math

# Print program description for user
print(f'This program computes and outputs the volume or space inside a tire.')

# User input
# User input needs to be a float value instead of an integer to allow for half sizes
tire_width = float(input("What is the tire width in mm: "))
tire_ratio = float(input("What is the tire aspect ratio: "))
tire_diameter = float(input("What is the tire diameter: "))

# Compute the volume of space inside the tire
# Answer expressed in liters
volume = (math.pi * tire_width**2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter))/10000000000

# Round the value of the volume
volume = round(volume, 2)

# Print result for user in liters
print(f"The volume inside the tire is: {volume} Liters")