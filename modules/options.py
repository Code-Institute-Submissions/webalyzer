"""
    init run options
"""
import os
import sys
from time import sleep
from modules.validate.validate_input import Validate
from modules.validate.validate_code import Html, Css
from modules.prints import run_choices_screen


def run_choices(validated_url):
    """
        Function to run choices and
        send the url to the validation
        service depending on choice.

        ....
        Args:
            str(url)
        ....
        Returns:
            Functions does not return anything
            as it contains a while loop set to run
            indefinitly, the loop exits when the
            user decides to exit, and can be
            achieved by typing 'quit' in the
            terminal.
        ....
    """

    run_choices_screen()

    while True:
        # Creating a new Validate object
        chosen_num = Validate.option_cls()

        # Validating the input against valid items
        response_num = chosen_num[0].validate_input(
            chosen_num[0], chosen_num[1])
        if (
            response_num[0] and
            (response_num[1] == '1' or '2')
        ):
            if response_num[1] == '1':
                validation = Html(response_num[1], validated_url)
                validation.err()

            elif response_num[1] == '2':
                validation = Css(response_num[1], validated_url)
                validation.err()

        else:
            # Because of how the app is structured, there's
            # checks and choices that makes this else block
            # never trigger, added this, just in case.
            print("Critical Error, rebooting app, sorry!")
            sleep(2)
            # Source for restarting app:
            # daniweb.com/programming/software-development/code/260268/restart-your-python-program
            python = sys.executable
            os.execl(python, python, * sys.argv)
