"""
init slow print
"""
import sys
import time


def sprint(string):
    """
    Function for slow typing in terminal
    Source: https://stackoverflow.com/a/54472904
    """
    for letter in string + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(3./90)


def wprint(string):
    """
    Function to slow down words in terminal
    Based on the above function.
    """
    split_string = string.split()
    for word in split_string:
        sys.stdout.write(word + ' ')
        sys.stdout.flush()
        time.sleep(.4)
