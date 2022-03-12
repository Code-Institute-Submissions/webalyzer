import re
import sys
import time


def slow_print(string):
    """
    Function for slow typing in terminal
    Source: https://stackoverflow.com/a/54472904
    """
    for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)


slow_print('hello world')


def get_url_link():
    """
    Get website link input from the user
    """
    while True:
        slow_print("Please enter your URL")
        slow_print("The URL MUST include HTTP, subdomain, domain and tld\n")
        slow_print("Example: https://en.wikipedia.org/wiki/"
                   "Python_(programming_language)\n")

        url_link = input("Enter your url here: ")

        if validate_url(url_link):
            slow_print("URL is valid!")
            break

    return url_link


def validate_url(url):
    """
    Function to validate the url link entered
    """
    # Regex Source:
    # geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/
    # Regex code to check URL
    REGEX = ("((http|https)://)(\\w+)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    compiled_regex = re.compile(REGEX)
    try:
        if not re.search(compiled_regex, url):
            raise ValueError(
                f"URL Error! URL provided: {url}"
            )
    except ValueError as validate_error:
        slow_print(f"\nInvalid link: {validate_error}, please try again.\n")
        return False

    return True


valid_url = get_url_link()
