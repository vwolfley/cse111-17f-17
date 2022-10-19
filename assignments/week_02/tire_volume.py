# Import math module
import math
# Import datetime module
from datetime import date
# Import os module
import os.path

# Path to my directory
file_path = "../test-files/volumes.txt"

# Get current date
today = date.today()
#print(today)

# Common tire sizes
common_sizes = ["205/60R15","215/50R17","235/65R17","245/60R18","265/70R17","275/50R20"]
# Common tire prices
tire_prices = [151.00,171.00,195.00,211.00,235.00,315.00]
# Common tire names
tire_names = ["BFGOODRICH RADIAL T/A","YOKOHAMA GTX", "GOODYEAR ASSURANCE MAXLIFE", "MICHELIN PRIMACY TOUR A/S","MICHELIN DEFENDER LTX","PIRELLI SCORPION VERDE A/S"]

# Print program description for user
print(f'''
This program computes and outputs the volume
or space inside a tire to a text file - volumes.txt\n
''')

# User input
# User input needs to be a float value instead of an integer to allow for half sizes
tire_width = float(input("What is the tire width in mm: "))
tire_ratio = float(input("What is the tire aspect ratio: "))
tire_diameter = float(input("What is the tire diameter: "))

# Compute the volume of space inside the tire
# Answer expressed in liters
volume = (math.pi * tire_width**2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter))/10000000000

# Compute tire size as width/ratioRdiameter
# For this program we are ignoring that tires can have half sizes
tire_size = f"{tire_width:,.0f}/{tire_ratio:,.0f}R{tire_diameter:,.0f}"

# Output to user tire size and tire volume
print(f'''Your tire size is {tire_size} and your tire volume is {volume:,.2f}\n''')

# Look to see if user tire size is in common size list
if tire_size in common_sizes:
    #print(tire_size)
    #print(common_sizes.index(tire_size))
    
    # Find index of common_sizes
    i = common_sizes.index(tire_size)
    print(f'''
    We have your tire size, {tire_size} in stock.
    It is a {tire_names[i]} and sells for ${tire_prices[i]}.\n''')
    # Ask user if they would like to purchase a tire?
    sale = input("Would you like to purchase them? y/n \n")
    
    if sale == "y" or sale == "yes":
        # Ask user how many tires to purchase
        number_tire = int(input("How many do you want? "))
        # Compute total cost of tire purchase
        total_cost = number_tire * tire_prices[i]
        
        # Ask user for Phone number
        phone_num = input("Can I get a phone number for your sale? ")
        # Print total cost for user
        print(f"Your total cost for the tires will be ${total_cost:,.2f}")
        
        # Append-info to 
        # Output - volumes.txt file
        with open(file_path, "at") as file:
            file.write(f"{today}, {tire_size}, {volume:,.2f}L, {number_tire}, ${total_cost:,.2f}, {phone_num} \n")
        
    else:
        print("Ok, have a nice day!")
    
else:
    print(f'''Sorry your tire size, {tire_size} is not in stock.''')
    
    # Append-info to 
    # Output - volumes.txt file
    with open(file_path, "at") as file:  # append mode
        file.write(f"{today}, {tire_size}, {volume:,.2f}L, (out of stock) \n")
