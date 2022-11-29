####################
# Date: 2022-11-29
# File: fruit.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 12 Checkpoint: Using Objects
# Improve your ability to write object-oriented code.
#####################



def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"\nOriginal: {fruit_list}")

    # Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")

    # Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"Append: {fruit_list}")

    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(f"Insert: {fruit_list}")

    # Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"Remove: {fruit_list}")

    # Add code to pop the last element from fruit_list and print the popped element and the list.
    remove = fruit_list.pop()
    print(f"Removed Element: {remove}")
    print(f"New List: {fruit_list}")

    # Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    # Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f"Cleared: {fruit_list}")

    # At the bottom of your program write a call to the main function.

# If this file is executed like this:
# then skip the call to main.
if __name__ == "__main__":
    main()