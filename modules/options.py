"""
init run options
"""
from subprocess import run
from time import sleep
from modules.slow_print import sprint  # , wprint
# from modules.utils import delete_last_line


def run_choices():
    """
    Function to present choices of the app
    """
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
    print("\n" * 1)
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
