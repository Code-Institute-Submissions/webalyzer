"""
    Utils module
"""
import sys
from time import sleep
from subprocess import run
# from getch import pause
from art import tprint
from modules.slow_print import sprint
from modules.prints import (WEBALYZER, YES_NO, WRONG,
                            BYE_TOP, BYE_BRAND,
                            BYE_MIDDLE, BYE_BOTTOM)


def print_yes_no():
    """
        Print "yes / no / quit" above input
    """

    sprint(YES_NO)


def print_brand_name():
    """
        Print brand name
    """

    tprint("Webalyzer", font="Small Slant", sep="\n")


def print_intro_welcome():
    """
        Print welcome intro
    """

    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.02)
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
    for line in BYE_TOP + BYE_BRAND + BYE_MIDDLE + BYE_BOTTOM:
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
        Function to delete lines up to (x times)
    """

    for _ in range(times):
        # ACSII codes based on
        # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

        # Move one line up \r to the start of the line
        sys.stdout.write('\r\x1b[1A')
        # Delete the last line
        sys.stdout.write('\x1b[2K')
    print()
    sleep(.2)


class Validate:
    """
        Validate class to validate user input,
        for all inputs in one place. Validate
        class make use of classmethods to define
        the input for each input for better targeting.
    """

    def __init__(self, answer):
        self.answer = answer
        self.options = 'quit', 'y', 'n', '1', '2', '3', '4'

    def __str__(self):
        return str(self.answer).lower().strip().replace(" ", "")

    @classmethod
    def background_cls(cls, option_input=False):
        """
            Defining background classmethod for
            background input in print_intro() in intro.py
        """

        return cls(input(
            "\x1b[3m\x1b[33mWould you like to know what "
            "\x1b[0;0m\x1b[48;2;38;57;106m \x1b[1;97mWebalyzer "
            "\x1b[0;0;0;0;0m\x1b[3m\x1b[33m does?"
            "   \x1b[0;0m\x1b[23m")), option_input

    @classmethod
    def read_more_cls(cls, option_input=False):
        """
            Defining read more classmethod for optional
            read more input under background input
            in print_intro() in intro.py
        """

        return cls(input("Want to read about "
                         "each option in more detail?"
                         "   ")), option_input

    @classmethod
    def option_cls(cls, option_input=True):
        """
            Defining option classmethod for
            chosen number input in run_choices() in options.py
        """

        return cls(input("Option:   ")), option_input

    def validate_input(self, optin):
        """
            Converts the string to lowercase,
            strips any before and after whitespace
            and replaces any spaces between the letters
            if any.

            Then checks if then answer is valid.

            *optin is referring to option_input in the defined
            classmethod's, to target specific inputs.
        """

        result = self.answer in self.options

        if not result:
            sleep(.2)
            sprint(WRONG)

            if optin:
                sleep(.6)
                del_last_lines_up(3)

            elif not optin:
                sleep(.6)
                del_last_lines_up(4)

            return False, self.answer

        elif self.answer == 'quit':
            print_outro()
            sys.exit()

        return True, self.answer
