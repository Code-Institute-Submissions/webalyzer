"""
init run options
"""

# from time import sleep
# from getch import pause
# from modules.slow_print import sprint  # , wprint
# from modules.utils import delete_last_line
from modules.utils import Validate
from modules.validate.validate_code import Html
from modules.prints import run_choices_screen


def run_choices(validated_url):
    """
    Function to run choices
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
            (response_num[1] == '1' or '2' or '3')
        ):
            if response_num[1] == '1':
                validation = Html(validated_url)
                validation.err()

            elif response_num[1] == '2':
                validation = Css(validated_url)
                validation.err()

            else:
                validation = Javascript(validated_url)
                validation.err()
