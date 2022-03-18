"""
    Utils module
"""
import sys
from time import sleep
from subprocess import run
from art import tprint
from modules.slow_print import sprint
from modules.prints import (WEBALYZER, WRONG,
                            BYE_TOP, BYE_BRAND,
                            BYE_MIDDLE, BYE_BOTTOM)


def print_yes_no():
    """
        Print "use yes / no" above input
    """
    sprint("Please use '\x1b[1;32my\x1b[0;0m' "
           "for \x1b[1;32mYes\x1b[0;0m and "
           "'\x1b[1;31mn\x1b[0;0m' for \x1b[1;31mNo\x1b[0;0m")


def print_brand_name():
    """
        Print brand name
    """
    tprint("Webalyzer", font="Small Slant", sep="\n")
    sleep(.5)


def print_intro_welcome():
    """
        Print welcome intro
    """
    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.2)
    print_brand_name()
    sleep(.5)


def print_about():
    """
        Prints Webalyzer's short story
    """

    for line in WEBALYZER:
        sleep(1)
        print(line)


def print_outro():
    """
        Prints Webalyzer's Outro
    """
    run('clear', check=True)
    for line in BYE_TOP:
        sleep(.02)
        print(line)
    for line in BYE_BRAND:
        sleep(.02)
        print(line)
    for line in BYE_MIDDLE:
        sleep(.02)
        print(line)
    for line in BYE_BOTTOM:
        sleep(.02)
        print(line)


def del_last_line():
    """
        Function to delete last line
    """

    # delete last line
    sys.stdout.write('\r\x1b[2K')


def del_last_lines_up(times):
    """
        Function to delete last lines up to (times)
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


class Validate:
    """
        Validates user input
    """
    options = 'quit', 'y', 'n', 1, 2, 3, 4

    def __init__(self, answer):
        self.answer = answer

    def validate_input(self):
        """
            Converts the string to lowercase,
            strips any before and after whitespace
            and replaces any spaces between the letters
            if any.

            Then checks in answer is valid.
        """
        converted = str(self.answer).lower().strip().replace(" ", "")
        print(converted)

        result = converted in self.options
        if not result:
            sleep(1)
            sprint(WRONG)
            del_last_lines_up(4)

            return False, converted

        elif converted == 'quit':
            print_outro()
            sys.exit()

        return True, converted
