"""
    init validate URL
"""
import re
from time import sleep
from subprocess import run
import requests
import urllib3
from requests.exceptions import HTTPError
from modules.slow_print import sprint, wprint
from modules.prints import print_brand_name, del_last_lines_up
from modules.regex import FULL_URL
from modules.validate.validate_input import Validate
from modules.options import run_choices


def test_response_url(url_link):
    """
        Function to test response of requested url
        handle and give back feedback incase of any known
        errors.
    """

    sleep(.2)
    sprint("Checking website...")
    sleep(2)
    try:
        response = requests.get(url_link).status_code
        if not response == 200:
            raise HTTPError(
                f"Response: {response}"
            )
    except HTTPError as http_err:
        sprint(f"Error: {http_err}, please try again.")
        sleep(2)
        del_last_lines_up(5)
        return False

    except requests.exceptions.InvalidURL:
        sprint(f"{url_link}: URL has an invalid label.")
        sleep(2)
        del_last_lines_up(5)
        return False

    except urllib3.exceptions.LocationParseError:
        sprint(f"Failed to parse: '{url_link}'")
        sleep(2)
        del_last_lines_up(5)
        return False

    except requests.exceptions.ConnectionError:
        sprint("This site can't be reached, please try again.")
        sleep(2)
        del_last_lines_up(5)
        return False

    return True


def validate_url(url):
    """
        Function to validate the url link entered
        by user against predefined REGEX code and
        if valid, sends the url to test_response_url
    """

    compiled_regex = re.compile(FULL_URL)
    try:
        if not re.search(compiled_regex, str(url)):
            raise ValueError(
                f"URL Error! URL provided: {url}"
            )
    except ValueError as validate_error:
        sprint(f"\nInvalid link: {validate_error}, please try again.")
        sleep(1.4)
        del_last_lines_up(5)
        return False

    return True


def get_url_link():
    """
        Function to ask for a URL and sends
        the URL to REGEX test and response test
        then over to run_choices() function in
        options.py
    """

    run('clear', check=True)
    print_brand_name()

    wprint(
        "The URL MUST include HTTP(s), DOMAIN and TLD")
    sprint("\nExample: https://en.wikipedia.org/wiki/"
           "Python_(programming_language)\n")
    sleep(1.3)

    while True:
        url_link = Validate.urllink_cls()

        if validate_url(url_link) and test_response_url(url_link):
            wprint("Response code: 200 => URL is valid")
            print()
            sleep(.4)
            break

    del_last_lines_up(8)
    return run_choices(url_link)
