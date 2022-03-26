"""
    This module handles validation
    of all inputs made by user and
    is responsible for providing
    inputs to user.
"""

import sys
from time import sleep
from modules.slow_print import sprint
from modules.prints import WRONG, print_outro, del_last_lines_up


class Validate:
    """
        Class to validate user input,
        for all inputs in one place. Validate
        class make use of classmethods to define
        the specific inputs for better targeting.

        Converts the string to lowercase,
        strips any before and after whitespace
        and replaces any spaces between the letters
        if any.
    """

    def __init__(self, answer):
        self.answer = answer
        self.options = 'quit', 'new', 'y', 'n', '1', '2'

    def __str__(self):
        return self.answer.lower().strip().replace(' ', '')

    @classmethod
    def background_cls(cls, option_input='bg'):
        """
            Defining background classmethod for
            background input.

            ....
            Args:
                str(answer)
            ....
            Returns:
                Function returns an input
                option_input: bool(False).
            ....
        """

        return cls(input(
            "\x1b[3m\x1b[33mWould you like to know what "
            "\x1b[0;0m\x1b[48;2;38;57;106m \x1b[1;97mWebalyzer "
            "\x1b[0;0;0;0;0m\x1b[3m\x1b[33m does?"
            "   \x1b[0;0m\x1b[23m")), option_input

    @classmethod
    def urllink_cls(cls):
        """
            Defining urllink classmethod for
            url_link input.

            ....
            Args:
                str(answer)
            ....
            Returns:
                Function returns an input.
            ....
        """

        return cls(input("Enter your url here: \n"))

    @classmethod
    def option_cls(cls, option_input=True):
        """
            Defining option classmethod for
            chosen number input.

            ....
            Args:
                str(answer)
            ....
            Returns:
                Function returns an input and
                option_input: bool(True).
            ....
        """

        return cls(input("Option:   ")), option_input

    @classmethod
    def another_cls(cls, option_input='another'):
        """
            Defining another classmethod for
            choosing a another number input.

            ....
            Args:
                str(answer)
            ....
            Returns:
                Function returns an input and
                option_input: str('another').
            ....
        """

        return cls(input("Want to validate another option?\n"
                         "Use '\x1b[1;32my\x1b[0;0m' "
                         "for \x1b[1;32mYes\x1b[0;0m, "
                         "'\x1b[1;94mnew\x1b[0;0m' for a "
                         "'\x1b[1;94mnew URL\x1b[0;0m' "
                         "or '\x1b[1;31mn\x1b[0;0m' to "
                         "\x1b[1;31mQuit\x1b[0;0m:   ")), option_input

    def validate_input(self, answer, optin):
        """
            Function to check if then answer is valid.
            *optin is referring to option_input in the defined
            classmethod's, to target specific inputs.

            ....
            Args:
                str(answer and optin if (another_cls))
                bool: (optin) if any, is set to true or false
            ....
            Returns:
                Function returns an input.
            ....
        """

        result = str(answer) in self.options

        if (
            not result or
            (optin is True and str(answer) in ['y', 'n']) or
            (optin == 'bg' and str(answer) in ['new', 'quit'])
        ):
            sleep(.2)
            sprint(WRONG)

            if optin == 'bg':
                sleep(.6)
                del_last_lines_up(4)

            elif optin:
                sleep(.6)
                del_last_lines_up(3)

            elif not optin or optin == 'another':
                sleep(.6)
                del_last_lines_up(4)

            return False, str(answer)

        elif str(answer) == 'new':
            # pylint recommends adding import to the top
            # but adding this import to the top will result
            # in ImportError: cannot import name '...'
            # from partially initialized module '...'
            # (most likely due to a circular import)
            from modules.validate.validate_url import get_url_link
            get_url_link()

        elif (
            str(answer) == 'quit' or
            str(answer) == 'n' and optin == 'another'
        ):
            print_outro()
            sys.exit()

        elif str(answer) == 'y' and optin == 'another':
            del_last_lines_up(3)

        return True, str(answer)
