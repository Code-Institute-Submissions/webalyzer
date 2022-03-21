"""
    init utils module
"""
import sys
from time import sleep
# from getch import pause
from modules.slow_print import sprint
from modules.prints import WRONG, print_outro


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
        self.options = 'quit', 'new', 'y', 'n', '1', '2', '3', '4'

    def __str__(self):
        return self.answer.lower().strip().replace(' ', '')

    @classmethod
    def background_cls(cls, option_input=False):
        """
            Defining background classmethod for
            background input.
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
            read more input.
        """

        return cls(input("Want to read about "
                         "each option in more detail?"
                         "   ")), option_input

    @classmethod
    def urllink_cls(cls):
        """
            Defining urllink classmethod for
            url_link input.
        """

        return cls(input("Enter your url here: \n"))

    @classmethod
    def option_cls(cls, option_input=True):
        """
            Defining option classmethod for
            chosen number input.
        """

        return cls(input("Option:   ")), option_input

    def validate_input(self, answer, optin):
        """
            Function to check if then answer is valid.
            *optin is referring to option_input in the defined
            classmethod's, to target specific inputs.
        """

        result = str(answer) in self.options

        if not result:
            sleep(.2)
            sprint(WRONG)

            if optin:
                sleep(.6)
                del_last_lines_up(3)

            elif not optin:
                sleep(.6)
                del_last_lines_up(4)

            return False, str(answer)

        elif str(answer) == 'new':
            from modules.validate.validate_url import get_url_link
            get_url_link()

        elif str(answer) == 'quit':
            print_outro()
            sys.exit()

        return True, str(answer)
