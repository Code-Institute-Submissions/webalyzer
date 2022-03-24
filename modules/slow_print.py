"""
    This module handles slow printing
    on the terminal.
"""
import sys
import time


def sprint(string):
    """
        Function for slow typing in terminal
        Source: https://stackoverflow.com/a/54472904

        ....
        Args:
            str(string)
        ....
        Returns:
            Functions does not return anything
            but does return printing on terminal.
        ....
    """
    for letter in string + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(3./90)


def wprint(string):
    """
        Function to slow down words in terminal
        Based on the above function.

        ....
        Args:
            str(string)
        ....
        Returns:
            Functions does not return anything
            but does return printing on terminal.
        ....
    """
    split_string = string.split()
    for word in split_string:
        sys.stdout.write(word + ' ')
        sys.stdout.flush()
        time.sleep(.4)
