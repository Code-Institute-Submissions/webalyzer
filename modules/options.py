"""
init run options
"""
# from subprocess import run
# from time import sleep
# from getch import pause
# from modules.slow_print import sprint  # , wprint
# from modules.utils import delete_last_line
from modules.utils import Validate
from modules.validate.validate_code import Html
from modules.prints import CHOICES, QUIT


def run_choices(validated_url):
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
        chosen_num = Validate.option_cls()

        # Validating the input against valid items
        response_num = chosen_num[0].validate_input(
            chosen_num[0], chosen_num[1])
        if (
            response_num[0] and
            (response_num[1] == '1' or '2' or '3' or '4')
        ):
            if response_num[1] == '1':
                validation = Html(validated_url)
                result = validation.errors()
                print(result)
                break
