"""
init validate URL
"""
import re
from time import sleep
from subprocess import run
import requests
from requests.exceptions import HTTPError
from modules.slow_print import sprint, wprint


# Regex Source:
# geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/
# Regex code to check URL
REGEX = ("((http|https)://)(\\w+)?" +
         "[a-zA-Z0-9@:%._\\+~#?&//=]" +
         "{2,256}\\.[a-z]" +
         "{2,6}\\b([-a-zA-Z0-9@:%" +
         "._\\+~#?&//=]*)")


def get_url_link():
    """
    Get website link input from the user
    """
    count = 0
    while True:
        if count > 0:
            run('clear', check=True)

        wprint(
            "The URL MUST include HTTP(s), domain and tld\n")
        sleep(.6)
        sprint("Example: https://en.wikipedia.org/wiki/"
               "Python_(programming_language)\n")
        sleep(1.3)
        url_link = input("Enter your url here: \n")

        if validate_url(url_link) and test_response_url(url_link):
            wprint("Response code: 200 => URL is valid")
            sleep(1)
            break

        count += 1

    return url_link


def validate_url(url):
    """
    Function to validate the url link entered
    """
    compiled_regex = re.compile(REGEX)
    try:
        if not re.search(compiled_regex, url):
            raise ValueError(
                f"URL Error! URL provided: {url}"
            )
    except ValueError as validate_error:
        sprint(f"\nInvalid link: {validate_error}, please try again.\n")
        sleep(4)
        return False

    return True


def test_response_url(url_link):
    """
    Function to test response of requested url
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
        sprint(f"Error: {http_err}, please try again \n")
        sleep(4)
        return False
    except requests.exceptions.ConnectionError:
        sprint("This site can't be reached, please try again \n")
        sleep(4)
        return False

    return True
