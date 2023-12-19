"""
Author: Jaleel Rogers

Purpose: Creating a function that behaves like the built-in function Range() containing 1-3 argument
returning a list.

Last edit: 10/01/2021, 1:38 P.M.

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 5 - myRange
"""


def main():
    print(list(myRange(-18)))  # Executes code in the function myRange.


def myRange(start, end=None, increment=None):
    if increment is None and end is None:
        end = start  # end is equal to start in order to get the whole range output
        start = 0
        increment = -2
    result = []
    if increment < 0:
        while end < start:
            result.append(start)
            start += increment

    elif increment > 0:  # Created another loop for end number that is greater than starting number
        while end > start:
            result.append(start)
            start += increment

    return result


if __name__ == "__main__":
    main()
# Missions accomplished
