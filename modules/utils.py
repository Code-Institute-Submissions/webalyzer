"""
Utils module
"""
import sys
from time import sleep
from art import tprint
from modules.slow_print import sprint  # , wprint


def print_intro_welcome():
    """
    Print welcome intro
    """
    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.2)
    tprint("Webalyzer", font="Small Slant", sep="\n")
    sleep(.5)


def print_brand_name():
    """
    Print brand name
    """
    tprint("Webalyzer", font="Small Slant", sep="\n")
    sleep(.5)


def print_yes_no():
    """
    Print use yes / no for input
    """
    sprint("Please use '\x1b[1;32my\x1b[0;0m' "
           "for \x1b[1;32mYes\x1b[0;0m and "
           "'\x1b[1;31mn\x1b[0;0m' for \x1b[1;31mNo\x1b[0;0m")


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


def validate_input_answer(options, answer):
    """
    Validates if input answer given aligns with
    the expected input options
    """
    result = answer in options
    if not result:
        sleep(1)
        print("\x1b[1;31mWrong answer please try again...\x1b[0;0m")
        del_last_lines_up(4)

        return True, result

    return False, result
