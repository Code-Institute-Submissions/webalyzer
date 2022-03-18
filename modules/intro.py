"""
init run intro
"""
from time import sleep
from subprocess import run
from getch import pause
from modules.utils import (del_last_line, del_last_lines_up,
                           print_brand_name, print_about,
                           print_yes_no, Validate)
from modules.prints import BINARY
from modules.options import run_choices


def print_intro():
    """
    Function to print intro and
    begin choices
    """
    print(BINARY)

    for i in range(101):
        # Loop to print from 0 - 100% without newline
        # on previous line
        print(f"\r\x1b[1;34mInitializing\x1b[0;0m: {i}% \x1b[?25l", end="")
        print("\x1b[?25h", end="")
        sleep(.05)

    del_last_line()
    sleep(1)

    while True:
        print_yes_no()
        sleep(.3)

        # Creating a new Validate object
        background = Validate.background()

        # Validating the input against valid letters
        background_answer = background.validate_input()
        if (
            background_answer[0] and
            background_answer[1] == 'y'
        ):
            run('clear', check=True)
            print_brand_name()
            print_about()

            sleep(2)
            while True:
                print_yes_no()

                # Creating a new Validate object
                read_more = Validate.read_more()

                # Validating the input against valid letters
                read_more_answer = read_more.validate_input()
                if (
                    read_more_answer[0] and
                    read_more_answer[1] == 'y'
                ):
                    del_last_lines_up(21)
                    print("run help")
                    pause("!!!")
                    break

                elif read_more_answer[1] == 'n':
                    break

            break

        elif background_answer[1] == 'n':
            break

    run('clear', check=True)
    print_brand_name()
    run_choices()
