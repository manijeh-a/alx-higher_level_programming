#!/usr/bin/python3
"""Module append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each line,
    containing a specific string.
    """
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)

