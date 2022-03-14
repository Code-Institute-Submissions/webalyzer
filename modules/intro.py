"""
init run intro
"""
# from subprocess import call
from modules.validate_requested_url import get_url_link


def print_intro():
    """
    Testing mapping
    """
    response = get_url_link()
    # call('clear')
    return response
