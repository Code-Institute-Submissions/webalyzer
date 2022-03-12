import re


def get_url_link():
    """
    Get website link input from the user
    """
    print("Please enter your URL")
    print("The URL MUST include HTTP, subdomain, domain and tld\n")
    print("Example: https://en.wikipedia.org/wiki/Python_(programming_language)\n")

    url_link = input("Enter your url here: ")
    validate_url(url_link)


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
        print(f"\nInvalid link: {validate_error}, please try again.\n")


get_url_link()
