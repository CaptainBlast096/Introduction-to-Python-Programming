"""
Author: Jaleel Rogers

Purpose: The purpose of the code is to be able to record names within string and int variables, calculate those
int variables, and combine int and string variables into a print statement.

Last edit: 8/27/2021, 11:10 A.M.

Course: Introduction to Programming Using Python - COP2034

Homework: Assignment 1 - Interactive Multiplier
"""
# Inputting and Outputting name
name = input("What's your name?" + "\n")
print("Hello " + name + ".")

# Inputting numbers and multiplying them
firstNumber = int(input("Please input a number." + "\n"))
secondNumber = int(input("Please input another number." + "\n"))
thirdNumber = firstNumber * secondNumber

""""
When you try to add Strings and Int together you'll get an error "can only concatenate str (not "int") to str.
In order to add both, you must convert the Int into a string.
"""
print("The product of " + str(firstNumber) + " and " + str(secondNumber) + " is " + str(thirdNumber) + ".")

# Variables were created using camelCase. Program works efficiently.
