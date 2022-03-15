"""
init run intro
"""
from time import sleep
from modules.slow_print import sprint, wprint
from modules.utils import del_last_line, del_last_lines_up
from modules.options import run_choices


def print_intro():
    """
    Function to print intro and
    begin choices
    """
    print(
        "01001001 00100000 01101000 01101111 "
        "01110000 01100101 00100000 01111001 "
        "01101111 01110101 00100000 01100101 "
        "01101110 01101010 01101111 01111001 "
        "00100000 01010111 01100101 01100010 "
        "01110011 01101001 01100011 01101000 "
        "01100001 01101110 01101001 01100011 "
        "00100000 01100001 01110011 00100000 "
        "01101101 01110101 01100011 01101000 "
        "00100000 01100001 01110011 00100000 "
        "01001001 00100000 01100101 01101110 "
        "01101010 01101111 01111001 01100101 "
        "01100100 00100000 01101101 01100001 "
        "01101011 01101001 01101110 01100111 "
        "00100000 01101001 01110100 00111010 00101001\n")

    for i in range(101):
        # Loop to print from 0 - 100% without newline
        # on previous line
        print(f"\rInitiating: {i}%", end="")
        sleep(0.05)

    del_last_line()
    sleep(1)

    sprint("Please use 'y' for yes and 'n' for no\n")
    sleep(1)
    skip_background = input("Skip background? \n").lower()
    if skip_background == 'y':
        del_last_lines_up(5)
    else:
        del_last_lines_up(5)
        sprint("A little background:")
        sleep(1)
        sprint("Websichanic is an app that asks you for a URL "
               "and returns the requests data.\n")
        sleep(1.5)
        sprint("The features of Websichanic is:\n")
        sleep(1)
        wprint("1. Validate The standard META TAGS of:")
        sleep(1)
        print("https://html.spec.whatwg.org/"
              "multipage/semantics.html#standard-metadata-names\n")
        sleep(1)
        wprint("2. Validate HTML, CSS AND Javascript")
        sleep(1)
        sprint("Validation HTML, CSS is through 'W3C' "
               "=> World Wide Web Consortium")
        sleep(2)
        sprint("Validation of Javascript is through CodeBeautify\n")
        sleep(1)

    sprint("Please use 'y' for yes and 'n' for no\n")
    sleep(1.2)
    read_more = input("Want to read about "
                      "each option in more detail? \n").lower()

    if skip_background == 'y':
        if read_more == 'y':
            print("run help")
        else:
            choice = run_choices()
    else:
        del_last_lines_up(19)
    print(choice)
