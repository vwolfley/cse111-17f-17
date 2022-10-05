####################
# Date: 2022-10-01
# File: scene.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: Write a Python program that draws a semi-realistic outdoor scene in a computer window.
#####################

########
# Milestone 1
# Draws the sky
# Draw the ground
# Draw some clouds
########

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing,\
    draw_horizontal_gradient, draw_vertical_gradient
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    #### Call drawing functions here ####
    

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    # draw_straw(canvas,)
    draw_straw(canvas, scene_width, scene_height)

    draw_foliage(canvas, scene_width, scene_height)
    
    # draw_hay_bale(canvas, start, bottom, diameter, interval)
    draw_hay_bale(canvas, 550, 48, 196, 5)
    draw_hay_bale(canvas, 376, 88, 135, 4)
    draw_hay_bale(canvas, 134, 105, 98, 2)
    draw_hay_bale(canvas, 35, 135, 45, 1)
    draw_hay_bale(canvas, 288, 145, 28, 1)
  

    # draw_clouds(canvas, center, bottom, diameter)
    draw_clouds(canvas, scene_width, scene_height)

    ##### DRAW BIRDS ####
    draw_birds(canvas, scene_width, scene_height)

    draw_signature(canvas, scene_width, scene_height)
    
    ##### DRAW BARN #####
    #draw_barn(canvas)
    #####################
    
    #### Draw grid for testing only #####
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function in the draw2d.py library.
    finish_drawing(canvas)


#### Define functions here ####
# Draw the sky
def draw_sky(canvas, scene_width, scene_height):

    sky_start = int(scene_height / 3)
    lower_sky = (219,240,249)
    upper_sky = (8,66,118)

    # draw_vertical_gradient(canvas, x0, y0, color0, x1, y1, color1)
    draw_vertical_gradient(canvas, 0, sky_start, lower_sky, scene_width, scene_height, upper_sky)

# Draw the ground
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="wheat")

# Draw a hay bale
def draw_hay_bale(canvas, start, bottom, diameter, interval):
    
    for i in range(5):
        # draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")
        draw_oval(canvas, start, bottom , start + diameter, bottom + diameter, width=1, outline="wheat3", fill="wheat1")
        start += interval

    #for i in range(0, 5, 1):
    #    step = 15
     #   draw_oval(canvas, start + step*i, bottom + step*i, (start + diameter) - step*i, (bottom + diameter) - step*i, width=1, outline="wheat3", fill="wheat1")


# Draw Birds
def draw_birds(canvas, scene_width, scene_height, num_birds=15):
    #draw_arc(canvas, x0, y0, x1, y1, start=0, extent=90, width=1, outline="black", fill="")
    birds = num_birds 
    # Draw 15 birds, each with a random location.
    for i in range(birds):
        x = random.randint(0, scene_width-20 )
        y = random.randint(250, scene_height-55)
        draw_arc(canvas, x, y, x+25, y+15, start=360, extent=90, width=1, outline="gray20",)
        draw_arc(canvas, x+25, y, x+50, y+15, start=90, extent=90, width=1, outline="gray20",)

# Draw clouds
def draw_clouds(canvas, scene_width, scene_height):
    sky_height = (scene_height-55)
    min_diam = 100
    max_diam = 300
    # Draw 15 circles, each with a random location and diameter.
    for i in range(15):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(325, sky_height)
        diameter = random.randint(min_diam, max_diam)

        # draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")
        draw_oval(canvas, x, y, x + diameter, y + diameter/4, outline="white", fill="white")

# Draw straw
def draw_straw(canvas, scene_width, scene_height):
    # Draw radom blades of straw, each with a random location and height.
    ground_height = round(scene_height / 3)

    for i in range(5000):
        x = random.randint(0, scene_width - 1)
        y = random.randint(0, ground_height)
        height = random.randint(3, 6)
        # draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")
        draw_rectangle(canvas, x, y, x + 1, y + height, outline="goldenrod3", fill="wheat")

# Draw green grass
def draw_foliage(canvas, scene_width, scene_height):

    ground_height = round(scene_height / 3)
    
    for i in range(700):
        x = random.randint(0, scene_width - 1)
        y = ground_height
        height = random.randint(2, 9)
        # draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")
        draw_rectangle(canvas, x, y, x + 1, y + height, outline="darkGreen", fill="green") 

# Draw barn
def draw_barn(canvas):
      #draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")
    #draw_rectangle(canvas, 175, 135, 295, 210, width=1, outline="black", fill="firebrick4")

    x = [150, 250, 250, 150]
    y = [120, 115, 150, 152]

    a = [250, 320, 320, 285, 250]
    b = [115, 120, 155, 215, 150]

    f = [150, 250, 285, 180]
    g = [152, 150, 215, 215]

    # (x3,y3) = (f0,g0)
    # (x1, y1) = (a1, b1)
    # (x2, y2) = (a4, b4) = (f1, g1)
    # (a3, b3) = (f2, g2)
    # (a4, b4) = (f2, g2)


    #draw_polygon(canvas, x0, y0, x1, y1, x2, y2, … xn, yn,width=1, outline="black", fill="")
    #draw_polygon(canvas, 150, 120, 260, 115, 260, 210, 150, 205,  width=1, outline="black", fill="firebrick4")
    draw_polygon(canvas, x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], width=1, outline="black", fill="firebrick3")
    draw_polygon(canvas, a[0], b[0], a[1], b[1], a[2], b[2], a[3], b[3], a[4], b[4], width=1, outline="black", fill="firebrick4")
    draw_polygon(canvas, f[0], g[0], f[1], g[1], f[2], g[2], f[3], g[3], width=1, outline="black", fill="slateGray")


# Sign artwork with signature
def draw_signature(canvas, scene_width, scene_height):
    #draw_text(canvas, center_x, center_y, text, fill="black")
    draw_text(canvas, scene_width - 50, 15, "Vern Wolfley", fill="wheat4")

# Draw a grid on canvas for locating objects
# For Testing only - Remove for production
def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)



# Call the main function so that
# this program will start executing.
main()