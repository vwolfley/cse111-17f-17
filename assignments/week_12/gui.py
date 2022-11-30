####################
# Date: 2022-11-29
# File: fruit.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 12 Team Activity: Using Objects
# As a team, write a Python program named gui.py
# that gets user input from a GUI, performs a
# simple calculation, and displays the result in a GUI.
#####################

"""
Core Requirements
    1. Your program must include a GUI that opens when you run your program.
    2. The GUI must allow a user to enter input.
    3. When the user enters valid input, your program must compute correct results and display those results in the GUI.

Stretch Challenges
    1. Add a "Clear" button to your GUI that clears all inputs and outputs when the user clicks it.
    2. Add a label that acts as a status bar at the bottom of your GUI. Your program should display 
    an error message in the status bar when the user enters invalid input. Your program should clear 
    the status bar when the user enters valid input.
"""

import math
import tkinter as tk
import number_entry as nent


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Volume of Cone")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a labels
    lbl_radius = tk.Label(frm_main, text="Radius:")
    lbl_height = tk.Label(frm_main, text="Height:")
    lbl_volume = tk.Label(frm_main, text="Volume:")

    # Create a entry box where the user will enter the radius.
    ent_radius = nent.FloatEntry(frm_main, 12, 100, width=5)
    ent_height = nent.FloatEntry(frm_main, 12, 100, width=5)

    # Create labels that will display the results.
    lbl_result = tk.Label(frm_main, width=8, anchor="w")

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=2, sticky="e")
    ent_radius.grid(row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_height.grid(row=1, column=0, padx=3, pady=2, sticky="e")
    ent_height.grid(row=1, column=1, padx=3, pady=2, sticky="w")
    lbl_volume.grid(row=3, column=0, padx=3, pady=2, sticky="e")
    lbl_result.grid(row=3, column=1, padx=3, pady=2, sticky="w")
    btn_clear.grid(row=3, column=2, padx=3, pady=2)

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's input.
            radius = ent_radius.get()
            height = ent_height.get()

            # Call the cone_volume function to compute the volume
            # for the radius and height that came from the user.
            # vol = cone_volume(radius, height)
            # vol = (math.pi * radius**2) * height / 3
            # print(vol)
            vol = cone_volume(radius, height)

            # Display the volume rounded to one place after the decimal for user to see
            lbl_result.config(text=f"{vol:.1f}")

        except ValueError:
            # When the user deletes all the digits in the volume & height
            # entry box, clear the slowest and fastest labels.
            lbl_result.config(text="")

    def cone_volume(radius, height):
        """Compute and return the volume of a right circular cone."""
        volume = math.pi * radius**2 * height / 3
        return volume

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.delete(0, tk.END)
        ent_height.delete(0, tk.END)
        lbl_result.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the age entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)
    ent_height.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python gui.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
