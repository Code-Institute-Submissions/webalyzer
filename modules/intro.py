"""
init run intro
"""
from subprocess import run
from time import sleep
from modules.slow_print import sprint  # , wprint
# from subprocess import run


def print_intro():
    """
    Testing mapping
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
        "00100000 01110100 01101000 01100101 "
        "01101101 00100000 00111010 00101001\n")

    choice = run_choices()
    print(choice)


def run_choices():
    """
    Function to present choices of the app
    """
    skip = input("Skip info of the choices?: ").lower()
    if skip == 'y':
        pass
    else:
        sleep(1)
        print("Validate HTML")
        sleep(1)
        print("Validate CSS")
        sleep(1)
        print("Validate Javascript")
        sleep(1)
        print("Validate Meta Tags")
        sleep(1)

    run('clear', check=True)
    sleep(2)
    sprint("Please choose one of the following:\n")
    print("\n" * 2)
    print("Validate Meta Tags?")
    validation_choice = input("     y = yes / n = no:  \n").lower()

    if not validation_choice == 'n':
        return validation_choice

    run('clear', check=True)
    sprint("Validate HTML?")
    validation_choice = input("y = yes / n = no:  \n").lower()

    if not validation_choice == 'n':
        return validation_choice

    run('clear', check=True)
    sprint("Validate CSS?")
    validation_choice = input("y = yes / n = no:  \n").lower()

    if not validation_choice == 'n':
        return validation_choice

    run('clear', check=True)
    sprint("Validate Javascript?")
    validation_choice = input("y = yes / n = no:  \n").lower()

    if not validation_choice == 'n':
        return validation_choice

    run('clear', check=True)
    ask_again = input("Start Over?  y / n").lower()
    if ask_again == 'y':
        repeat_choices()

    return


def repeat_choices():
    """
    Function to repeat choices
    """
    return True
