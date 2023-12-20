"""
Author: Jaleel Rogers

Purpose: Have a text file named book containing strings and record the word and location of word in book.
Then afterwards put output to a text file called index.

Last edit: 09/24/2021, 6:29 P.M.

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 4 - Index
"""
import string

TEXT_FILE = open("index.txt", "w")
text = open("book.txt", "r")
d = dict()  # All words in dictionary

for line in text:  # Helps to organize the string such as taking out uppercase and punctuation
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")

    # number_of_lines += 1
    # Make each word into a list

    for word in words:
        if word in d:
            d[word] = d[word] + 1

        else:
            d[word] = 1


def strings_in_file(text, list_of_strings):
    line_number = 0
    list_of_results = []

    with open(text, 'r') as read_obj:
        # Reading all lines in the file one by one by iteration
        for line in read_obj:
            line_number += 1
            # Checking each line, if the line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is matched/found in line
                    # then we will append that line along with line number in the list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Returning the list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results


# search for given strings in the file 'sample.txt'
matched_lines = strings_in_file('book.txt',
                                ['a', 'if', 'is', 'of', 'peck', 'peppers', 'peter', 'picked', 'pickled', 'piper', 'the',
                                 'where'])

for elem in matched_lines:
    print('Word = ', elem[0], "|", 'Line Number = ', elem[1])  # Word location, word, and line are recorded

for i in sorted(d):  # Just the output same thing located in index.txt
    print(("Word " + i, "Occurrences:" + str(d[i])), end=" ", )
    TEXT_FILE.write(i + "| " + "Number of Occurrences " + str(d[i]) + "\n")
# Can't add more than one argument to a text file
TEXT_FILE.close()

# Was not able to add line number to index.txt
