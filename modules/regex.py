""" Regex Module """

import re

# FULL_URL regex code Source:
# geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/
# Regex code to check URL
FULL_URL = re.compile("((http|https)://)(\\w+)?" +
                      "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                      "{2,256}\\.[a-z]" +
                      "{2,6}\\b([-a-zA-Z0-9@:%" +
                      "._\\+~#?&//=]*)")

# Regex to extract whole domain name from http to (e.g. .com, etc)
# Or just the domain name like in nike in
# https://nike.com or https://www.nike.com
# As it turns out it was way harder to validate JS files than anticipated
# I won't be using these but let them be here for future reference.
WHOLE_DOMAIN = re.compile(r"((?:(?:https)|(?:http))+(?::\/\/)+(?:[^:\/?\n]+))")
DOMAIN = re.compile(r"((?:https:)|(?:\w+)|(?:\.|//))+((\w+)?)(?:\.).*")
