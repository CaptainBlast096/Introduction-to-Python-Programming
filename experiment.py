# Python program to print partial Koch Curve.
# importing the libraries : turtle standard
# graphics library for python
import turtle
from turtle import *

# col = input("Enter color value: r,g,b or name ")
fillcolor("green")
begin_fill()


# function to create koch snowflake or koch curve
def kochSnowflake(size, iteration):
    # turt does not necesarrily have to be define d in the function
    # Make levels equal to iteration and lengthside equal to size
    if iteration == 0:  # it seems levels controls the size
        forward(size)
        return  # Works the same with an else statement
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
    # defining the speed of the turtle
    speed(99999999999999999999999999999999999999)
    length = 300.0

    # Pull the pen up – no drawing when moving.
    penup()

    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()
    for i in range(3):
        kochSnowflake(length, 0)
        right(120)
    end_fill()
    # To control the closing windows of the turtle
    mainloop()
