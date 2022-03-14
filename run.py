"""
Init the app
"""
from time import sleep
from art import tprint
from modules.intro import print_intro


tprint("Welcome to", font="Small Slant", sep="\n")
sleep(.2)
tprint("Websichanic", font="Small Slant", sep="\n")
sleep(.5)


def start_intro():
    """
    Initialize intro
    """
    print(print_intro())


start_intro()
