"""
init run options
"""
# from subprocess import run
# from time import sleep
from getch import pause
# from modules.slow_print import sprint  # , wprint
# from modules.utils import delete_last_line
from modules.utils import del_last_lines_up, Validate
from modules.prints import CHOICES, QUIT


def run_choices():
    """
    Function to run choices
    """
    print(QUIT)
    print()
    for line in CHOICES:
        print(line)
    print()

    while True:
        # Creating a new Validate object
        chosen_number = Validate.option()

        # Validating the input against valid items
        chosen_number_answer = chosen_number[0].validate_input(
            chosen_number[1])
        if (
            chosen_number_answer[0] and
            chosen_number_answer[1] == (
                '1' or '2' or '3' or '4' or 'quit')
        ):
            del_last_lines_up(13)
            pause("!!!")
            break
