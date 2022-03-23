""" Regex Module """

import re

VALIDATE_URL = re.compile(
    r"((?:(?:https)|(?: http))+(?::\/\/)+(?:[^:\/?\n]+).*)")

# Regex to extract whole domain name from http to (e.g. .com, etc)
# Or just the domain name like in nike in
# https://nike.com or https://www.nike.com
# As it turns out it was way harder to validate JS files than anticipated
# I won't be using these but let them be here for future reference.
WHOLE_DOMAIN = re.compile(r"((?:(?:https)|(?:http))+(?::\/\/)+(?:[^:\/?\n]+))")
DOMAIN = re.compile(r"((?:https:)|(?:\w+)|(?:\.|//))+((\w+)?)(?:\.).*")
