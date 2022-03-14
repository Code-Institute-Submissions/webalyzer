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
