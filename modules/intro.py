"""
    This module prints the intro
    to the terminal.
"""

from time import sleep
from subprocess import run
from getch import pause
from modules.prints import del_last_line  # , del_last_lines_up
from modules.prints import (BINARY, print_brand_name,
                            print_about, print_yes_no)
from modules.validate.validate_url import get_url_link
from modules.validate.validate_input import Validate


def print_intro():
    """
        Function to print intro and
        check if user wants back story of
        Webalyzer and acts accordingly to
        the answer of the presented input.

        ....
        Args:
            None
        ....
        Returns:
            Functions does not explicity return
            anything but runs get_url_link().
        ....
    """
    print(BINARY)

    for i in range(101):
        # Loop to print from 0 - 100% without newline
        # using end="" and on previous line using \r
        print(f"\r\x1b[1;34mInitializing\x1b[0;0m: {i}% \x1b[?25l", end="")
        print("\x1b[?25h", end="")
        sleep(.05)

    del_last_line()
    sleep(1)

    while True:
        print_yes_no()
        sleep(.3)

        # Creating a new Validate object
        background = Validate.background_cls()

        # Validating the input against valid letters
        background_answer = background[0].validate_input(
            background[0], background[1])
        if (
            background_answer[0] and
            background_answer[1] == 'y'
        ):
            run('clear', check=True)
            print_brand_name()
            print_about()

            sleep(2)

            pause(message="\x1b[3mPress any key to continue...\x1b[23m")

            break

        elif background_answer[1] == 'n':
            break

    get_url_link()
