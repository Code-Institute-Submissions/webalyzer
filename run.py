"""
Init the app
"""
from subprocess import run
from modules.prints import print_intro_welcome
from modules.intro import print_intro


run('clear', check=True)
print_intro_welcome()
print_intro()
