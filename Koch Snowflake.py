"""
Author: Jaleel Rogers

Purpose: To create what is known as a "Koch Snowflake", and shape made of straight lines and triangles of varying
sizes and lengths in order to make a whole, colored shape. However, there will be different iterations such as
iteration zero just being a straight line.

Last edit: 10/08/21 10:13 P.M.

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 6 - Koch Snowflake
"""

# graphics library for python
from turtle import *


def main():
    # defining the speed of the turtle
    # Maxing speed
    speed(99999999999999999999999999999999999999)

    # Adjusts the amount of line given to the graphic
    length = 300.0

    # Pull the pen up – no drawing when moving
    penup()

    # Move the turtle backward by distance,
    # opposite to the direction the turtle is headed
    backward(length / 2.0)

    # Pull the pen down – drawing when moving
    pendown()
    for i in range(3):
        kochSnowflake(length, 4)
        right(120)
    # Ends coloring
    end_fill()
    # To control the closing windows of the turtle


# Decides the color of inside of shape
fillcolor("green")
# Starts coloring
begin_fill()


# function to create koch snowflake or koch curve
def kochSnowflake(size, iteration):
    if iteration == 0:
        forward(size)
        return  # Else statement would also suffice
    size /= 3.0
    kochSnowflake(size, iteration - 1)  # experiment with the level numbers
    left(60)
    kochSnowflake(size, iteration - 1)
    right(120)
    kochSnowflake(size, iteration - 1)
    left(60)
    kochSnowflake(size, iteration - 1)


# main function
if __name__ == "__main__":
    main()  # Attaches the loop to the main function
    mainloop()  # Keeps window open after drawing is completed
# End of program
