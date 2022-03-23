"""
    All prints to be printed at specific time.
    Prints made by @MTraveller
    https://github.com/MTraveller
"""

import sys
from subprocess import run
from time import sleep
from art import tprint
from modules.slow_print import sprint


BINARY = (
    "01001001 00100000 01101000 01101111 "
    "01110000 01100101 00100000 01111001 "
    "01101111 01110101 00100000 01100101 "
    "01101110 01101010 01101111 01111001 "
    "00100000 01010111 01100101 01100010 "
    "01100001 01101100 01111001 01111010 "
    "01100101 01110010 00100000 01100001 "
    "01110011 00100000 01101101 01110101 "
    "01100011 01101000 00100000 01100001 "
    "01110011 00100000 01001001 00100000 "
    "01100101 01101110 01101010 01101111 "
    "01111001 01100101 01100100 00100000 "
    "01101101 01100001 01101011 01101001 "
    "01101110 01100111 00100000 01101001 "
    "01110100 00100000 00111010 00101001 "
    "\n"
)


YES_NO = (
    "Please use '\x1b[1;32my\x1b[0;0m' "
    "for \x1b[1;32mYes\x1b[0;0m, "
    "'\x1b[1;31mn\x1b[0;0m' for \x1b[1;31mNo\x1b[0;0m "
    "or '\x1b[1;95mquit\x1b[0;0m' to \x1b[1;95mQuit\x1b[0;0m the app"
)


WEBALYZER = (
    "Webalyzer is a simple app that validates the "
    "HTML and CSS of a website. ",
    "The initial idea was inspired by TextMechanic, and "
    "was called Websichanic,", "but was rebranded to fit "
    "the form it has taken during development.\n",
    "HTML validates through validator.nu, ",
    "a clone of 'W3C' => World Wide Web Consortium. ",
    "CSS validates through the jigsaw.w3c.org validator.\n",
    "Webalyzer was made as part of Code Institutes "
    "3rd portfolio project assessment.", "\"Python Essentials\"\n",
    "The author @MTraveller - https://github.com/MTraveller,",
    "and can be reached at https://www.linkedin.com/in/mtantouri\n",
    "Webalyzer will ask you for a URL to validate, on the next screen.",
)


CHOICES = [
    "==============================",
    "  Please Choose By (Number)   ",
    "==============================",
    "\\*  (1): Validate HTML      */",
    "**       -------------      **",
    "/*  (2): Validate CSS       *\\",
    "==============================",
]


WRONG = "\x1b[1;31mWrong answer, please try again...\x1b[0;0m"


BYE_TOP = [
    "╔" + ("╦" * 78) + "╗",
    "║" + ("║" * 78) + "║",
    "║" + ("║" * 78) + "║",
    "╠" + ("╩" * 78) + "╣",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
]


BYE_BRAND = [
    "║" + (" " * 12) + " _      __        __          __" + (" " * 34) + "║",
    "║" + (" " * 12) +
    "| | /| / / ___   / /  ___ _  / /  __ __ ___ ___   ____" +
    (" " * 12) + "║",
    "║" + (" " * 12) +
    "| |/ |/ / / -_) / _ \\/ _ `/ / /  / // //_ // -_) / __/" +
    (" " * 12) + "║",
    "║" + (" " * 12) +
    "|__/|__/  \\__/ /_.__/\\_,_/ /_/   \\_, / /__/\\__/ /_/" +
    (" " * 15) + "║",
    "║" + (" " * 44) +
    "/___/              " + (" " * 15) + "║",
]


BYE_MIDDLE = [
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 17) +
    "We thank you for your visit and hope to see" + (" " * 18) + "║",
    "║" + (" " * 22) + "you soon again :) Have a great day." +
    (" " * 21) + "║",
    "║" + (" " * 78) + "║",
]


BYE_BOTTOM = [
    "║" + (" " * 78) + "║",
    "╠" + ("╦" * 78) + "╣",
    "║" + ("║" * 78) + "║",
    "║" + ("║" * 78) + "║",
    "╚" + ("╩" * 78) + "╝",
]


QUITORNEW = (
    "Did you know;\nTyping '\x1b[1;95mquit\x1b[0;0m'"
    " or '\x1b[1;94mnew\x1b[0;0m' any time,\n"
    "will \x1b[1;95mQuit\x1b[0;0m the app or"
    " validate a \x1b[1;94mNew\x1b[0;0m URL ;)"
)


def print_yes_no():
    """
        Prints "yes / no / quit" above input
    """

    sprint(YES_NO)


def print_brand_name():
    """
        Prints brand name
    """

    tprint("Webalyzer", font="Small Slant", sep="\n")


def print_intro_welcome():
    """
        Prints welcome intro
    """

    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.02)
    print_brand_name()
    sleep(.5)


def print_about():
    """
        Prints Webalyzer's short story
    """

    for line in WEBALYZER:
        sleep(1)
        print(line)


def run_choices_screen():
    """
        Prints run_choices options
    """
    print(QUITORNEW)
    print()
    for line in CHOICES:
        print(line)
    print()


def print_outro():
    """
        Prints Webalyzer's Outro
    """

    run('clear', check=True)
    for line in BYE_TOP + BYE_BRAND + BYE_MIDDLE + BYE_BOTTOM:
        sleep(.02)
        print(line)


def del_last_line():
    """
        Function to delete last line
    """

    # delete last line
    sys.stdout.write('\r\x1b[2K')


def del_last_lines_up(times):
    """
        Function to delete lines up to (x times)
    """

    for _ in range(times):
        # ACSII codes based on
        # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

        # Move one line up \r to the start of the line
        sys.stdout.write('\r\x1b[1A')
        # Delete the last line
        sys.stdout.write('\x1b[2K')
    print()
    sleep(.2)
