"""
Utils module
"""
import sys
from time import sleep
from art import tprint


def print_intro_welcome():
    """
    Print welcome intro
    """
    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.2)
    tprint("Websichanic", font="Small Slant", sep="\n")
    sleep(.5)


def print_brand_name():
    """
    Print brand name
    """
    tprint("Websichanic", font="Small Slant", sep="\n")
    sleep(.5)


def del_last_line():
    """
    Function to delete last line
    """

    # delete last line
    sys.stdout.write('\r\x1b[2K')


def del_last_lines_up(times):
    """
    Function to delete last line up(s)
    """
    for _ in range(times):
        # ACSII codes based on
        # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

        # Move one line up \r to the start of the line
        sys.stdout.write('\r\x1b[1A')

        # Delete the last line
        sys.stdout.write('\x1b[2K')
    print()
    sleep(1)
