"""
Author: Jaleel Rogers

Purpose: To encrypt information within a text file and output that encryption within another text file using a
caesar cipher in order to shift the original message a certain number of times.

Last edit: 09/15/2021, 9:37 P.M.

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 3 - Encrypter
"""

# Opens a text file called "message" and reads its contents
with open('message.txt') as f:
    lines = f.readlines()


# The encrypter
def CAESAR_CIPHER(RAW_TEXT, key):
    # Identifying the letters used to make message and encrypt message
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    CIPHER_TEXT = ""

    for i in range(len(RAW_TEXT)):
        char = RAW_TEXT[i]
        idx = alphabet.find(char.upper())

        if idx == -1:
            CIPHER_TEXT = CIPHER_TEXT + char
        # For uppercase letters
        elif char.isupper():
            CIPHER_TEXT += chr((ord(char) + key - 65) % 26 + 65)
        # For lowercase letters
        else:
            CIPHER_TEXT += chr((ord(char) + key - 97) % 26 + 97)

    return CIPHER_TEXT


print("Type in number of shifts:")
key = int(input())

# Made to just double check if inputs and outputs are correct
# Original message
print("Original Message: " + str(lines))
# Number of shifts
print("Shift: " + str(key))
# Encrypted message
print("Encrypted Message: " + CAESAR_CIPHER(str(lines), key))

# Open text file
TEXT_FILE = open("Encrypted.txt", "w")
# Write string to file
Letter = TEXT_FILE.write(str(lines))
# Close the file
TEXT_FILE.close()

# Program was made using CONSTANT_CASE
