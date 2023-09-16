#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


import sys
def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError
    There should be no space at the beginning or at the
    end of each printed line
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            string += "{}{}".format(text[i], "\n" * 2)
            i += i < len(text) and 1
            while i < len(text) and text[i] in " \t":
                i += 1
        else:
            string += "{}".format(text[i])
            i += 1

    sys.stdout.write(string)
    

if __name__ == "__main__":
    import doctest
    doctest("tests/5-text_indentation.txt")
