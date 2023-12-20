"""
Author: Jaleel Rogers

Purpose: To find the maximum height of a bouncing ball with each bounce. The number of each bounce is dictated either
         randomly by the program or inputted by the user. If the ball has a bounce less than 0.1, the program stops
         counting.

Last edit: 9/10/2021, 11:40 A.M.

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 2 - Bouncing Ball
"""

# Program relied on the use of random
from random import uniform
import random as rand

# Equations
height = 10
COEFFICIENT_RESTITUTION = .8

# Each bounce should have a random number
mode = (input("Which mode should I use? "))

if mode == "height":
    # The number of bounces for height is undefined. Will stop recording bounce when height is less than 1
    for i in range(height):
        r = uniform(0.7, 1.0)
        height = COEFFICIENT_RESTITUTION * COEFFICIENT_RESTITUTION * r * height
        FORMATTED_HEIGHT = "{:.2f}".format(height)  # Changed the floating number to only have two decimal places
        if height >= 0.1:
            print("Bounce number " + str(i + 1) + " gave a height of " + str(FORMATTED_HEIGHT))

elif mode == "user":  # User inputs amount of bounces
    NUMBER_BOUNCES = int(input("How many bounces should there be? "))
    for i in range(NUMBER_BOUNCES):
        r = uniform(0.7, 1.0)
        height = COEFFICIENT_RESTITUTION * COEFFICIENT_RESTITUTION * r * height
        FORMATTED_HEIGHT = "{:.2f}".format(height)
        if height >= 0.1:
            print("Bounce number " + str(i + 1) + " gave a height of " + str(FORMATTED_HEIGHT))

# Some variables used CONSTANT_CASE.
