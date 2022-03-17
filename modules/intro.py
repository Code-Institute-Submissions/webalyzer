"""
init run intro
"""
from time import sleep
from subprocess import run
from getch import pause
from modules.slow_print import sprint, wprint
from modules.utils import (del_last_line, del_last_lines_up,
                           print_brand_name, print_yes_no, Validate)
# from modules.options import run_choices


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
        "\n")

    for i in range(101):
        # Loop to print from 0 - 100% without newline
        # on previous line
        print(f"\r\x1b[1;34mInitializing\x1b[0;0m: {i}% \x1b[?25l", end="")
        print("\x1b[?25h", end="")
        sleep(.05)

    del_last_line()
    sleep(1)

    while True:
        print_yes_no()
        sleep(.3)
        input_answer = 'y', 'n'
        background = Validate(input_answer, input(
            "\x1b[3m\x1b[33mWould you like to know what "
            "\x1b[0;0m\x1b[48;2;38;57;106m \x1b[1;97mWebalyzer "
            "\x1b[0;0;0;0;0m\x1b[3m\x1b[33m does?"
            "   \x1b[0;0m\x1b[23m"))

        background_answer = background.validate_input()

        if background_answer:
            # print(background.validate_input())
            # print(type(background.validate_input()[1]))
            # pause("!!!")
            if background_answer[1] == 'y':
                run('clear', check=True)
                print_brand_name()
                sleep(1)
                sprint("Webalyzer is an app that asks for a URL "
                       "and returns the requested data.\n")
                sleep(1.5)
                sprint("The features of Webalyzer is:\n")
                sleep(1)
                wprint("1. Validate The standard META TAGS of:")
                print("\nhttps://html.spec.whatwg.org/"
                      "multipage/semantics.html#standard-metadata-names\n")
                sleep(1)
                wprint("2. Validate HTML, CSS and Javascript")
                sleep(1)
                sprint("\nValidation of HTML, CSS is through 'W3C' "
                       "=> World Wide Web Consortium")
                sleep(2)
                sprint("Validation of Javascript is through CodeBeautify\n")
                # del_last_lines_up(15)

                read_more = Validate(input_answer,
                                     input("Want to read about "
                                           "each option in more detail?"
                                           "   "))

                if read_more.validate_input()[1] == 'y':
                    del_last_lines_up(15)
                    print("run help")
                    pause("!!!")

            elif background.validate_input()[1] == 'n':
                pass

        break

    # run_choices()
