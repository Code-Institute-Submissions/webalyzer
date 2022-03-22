"""
    init run options
"""

from modules.validate.validate_input import Validate
from modules.validate.validate_code import Html, Css
from modules.prints import run_choices_screen


def run_choices(validated_url):
    """
        Function to run choices and
        send the url to the validation
        service depending on choice.
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
                validation = Html(response_num[1], validated_url)
                validation.err()

            elif response_num[1] == '2':
                validation = Css(response_num[1], validated_url)
                validation.err()

            else:
                validation = Javascript(response_num[1], validated_url)
                validation.err()
