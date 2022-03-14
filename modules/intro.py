"""
init run intro
"""
from modules.validate_requested_url import print_message, get_url_link

message = print_message
print(message)


def print_intro():
    """
    Testing mapping
    """
    print("intro working")
    valid_url = get_url_link()

    return valid_url


run_intro = print_intro()
