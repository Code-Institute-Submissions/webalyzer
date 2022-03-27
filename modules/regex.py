""" Regex Module """

import re


# After many hours study about regex
# I finally found the the solutions to my problems :)
# For the URL I had initially bored a code from geekforgeeks
# But it turned out that domains with dashes was deemed not valid.

# VALIDATE_URL finds all valid domains to be valid after many tests,
# with all kinds of combinations. Well, atleast all domains I've tested.

# VALID_SUBSTRING finds all valid text in an occean of spaces and
# newlines, be it strings, letters or numbers. So happy!


VALIDATE_URL = re.compile(
    r"(((https|http):\/\/)[^\W]"
    r"(?:([a-zA-Z\d]+)(?:(\.|\-)|\w+)+).*)"
)

VALID_SUBTRING = re.compile(r"[^ ]*(?:(?:\w+.*))")
