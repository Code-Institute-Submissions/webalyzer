"""
Init the app
"""
from subprocess import run
from modules.utils import print_intro_welcome
from modules.intro import print_intro


run('clear', check=True)
print_intro_welcome()


def start_intro():
    """
    Initialize intro
    """
    return print_intro()


start_intro()
