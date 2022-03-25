"""
    This module handles the
    validation of HTML and
    CSS code of the website's
    user.
"""

import re
from time import sleep
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import cfscrape
from getch import pause
from modules.validate.validate_input import Validate
from modules.prints import (print_brand_name,
                            run_choices_screen, del_last_lines_up)
from modules.regex import VALID_SUBTRING


def run_options():
    """
        Function to display
        options.

        ....
        Args:
            None
        ....
        Returns:
            No explicit return set.
        ....
    """

    del_last_lines_up(1000)
    print_brand_name()
    run_choices_screen()


def error_choose_another_option():
    """
        Function to display another
        option input to user if response
        from service isn't 200.

        ....
        Args:
            None
        ....
        Returns:
            No explicit return set.
        ....
    """

    # Creating a new Validate object
    another = Validate.another_cls()
    # Validating the input against valid items
    another[0].validate_input(another[0], another[1])

    run_options()


def choose_another_option():
    """
        Function to display another
        option input to user when code
        has been validated.

        ....
        Args:
            None
        ....
        Returns:
            No explicit return set.
        ....
    """
    del_last_lines_up(1)
    print("Well done, there were no errors!")

    # Creating a new Validate object
    another = Validate.another_cls()
    # Validating the input against valid items
    another[0].validate_input(another[0], another[1])

    run_options()


class ValidateCode:
    """
        Class to validate requested
        codes from either options of
        1. HTML or 2. CSS

        ....
        Args:
            int(option), str(url)
        ....
        Returns:
            Class pass on str(self.data)
            to it's inherited classes
            Html and Css.
        ....
    """

    def __init__(self, option, url):
        self.option = option
        self.url = url

        self.service = ''
        self.res_check = 0

        self.html = f"https://validator.nu/?doc={url}"
        self.css = f"https://jigsaw.w3.org/css-validator/validator?uri={url}"

        self.headers = {'Referrer': 'https://webalyzer.heokuapp.com',
                        'User-Agent': 'Mozilla/5.0 (platform; '
                        'rv:geckoversion) Gecko/geckotrail '
                        'Firefox/firefoxversion',
                        'Accept': 'text/html',
                        'Accept-Encoding': 'gzip, compress', }
        try:
            with requests.Session() as re_s:
                re_s = cfscrape.create_scraper()
                re_s.headers = self.headers

                while self.res_check == 0:
                    del_last_lines_up(14)
                    if self.option == '1':
                        print("Checking Validator.nu Service!")
                        self.service = "Validator.nu"
                        self.res_check = requests.get(
                            'https://validator.nu').status_code
                        sleep(1.2)
                        del_last_lines_up(1)

                    elif self.option == '2':
                        print("Checking Jigsaw.w3.org Service!")
                        self.service = "Jigsaw.w3.org"
                        self.res_check = requests.get(
                            'https://jigsaw.w3.org/'
                            'css-validator/').status_code
                        sleep(1.2)
                        del_last_lines_up(1)

                if self.res_check not in [200, 201, 202]:
                    raise HTTPError(
                        f"Response: {self.res_check}"
                    )

        except HTTPError as http_err:
            print("Validation Service Error: "
                  f"{http_err}, please try again, later.")

        except requests.exceptions.ConnectionError:
            print("This validation service can't be "
                  "reached, please try again, later.")

        else:
            if self.res_check:
                if self.option == '1':
                    print("Checking Successfull!")
                    sleep(1)
                    del_last_lines_up(1)
                    print("Retriving Results :)")
                    res = re_s.get(self.html)
                    sleep(1)
                    del_last_lines_up(1)
                else:
                    print("Checking Successfull!")
                    sleep(1)
                    del_last_lines_up(1)
                    print("Retriving Results :)")
                    res = re_s.get(self.css)
                    sleep(1)
                    del_last_lines_up(1)

            self.data = BeautifulSoup(res.content, 'html5lib')
            self.data.prettify()

    def __str__(self):
        # __str__ avoids sending the
        # object's name and id in memory,
        # instead of the actual usable data
        return str(self.data)


class Html(ValidateCode):
    """
        Class to send validated
        HTML code to err().

        ....
        Args:
            str(self.data=(scraped HTML of validated service))
        ....
        Returns:
            Class is not set to explicitly other
            than passed on to err() after a try for error
            has been made.
        ....
    """

    def __init__(self, option, data):
        super().__init__(option, data)

        try:
            self.all_lis = self.data.find('ol')
            if self.all_lis == "'Html' object has no attribute 'data'":
                raise AttributeError(
                    f"No Response: {self.all_lis}"
                )
        except AttributeError as data_err:
            del_last_lines_up(3)
            print("Ohh.. noo.. There's an error!\n"
                  "Error: Did not receive data from validator, "
                  "instead got:\n"
                  f"{data_err}"
                  "\n\nWhich basically means; that the "
                  "validator has an issue.\n")
            sleep(3)

    def err(self):
        """
            Function to filter
            errors for the terminal.

            ....
            Args:
                str(data=(scraped HTML of validated service))
            ....
            Returns:
                Class medthod is not set to
                return True after printed in the terminal
                of either errors or a no error message.
            ....
        """

        try:
            all_errors = self.all_lis.find_all('li')
            if all_errors == "'Html' object has no attribute 'data'":
                raise AttributeError()

        except AttributeError:
            error_choose_another_option()
            return True

        else:
            print("Processing Results..")
            sleep(1)
            errors_list = []
            for list_item in all_errors:
                count = 0
                try:
                    for li in list_item.find('li', {'class': 'error'}):
                        if count == 2:
                            continue
                        errors_list.append(li.text)
                        count += 1
                except TypeError:
                    choose_another_option()
                    return True

            del_last_lines_up(5)

            print("We received the following errors:\n")

            for error in errors_list:
                for line in error:
                    print(line)
                sleep(.4)
                print()

            pause(message="\x1b[3mPress any key to continue...\x1b[23m")
            del_last_lines_up(1000)
            print_brand_name()
            run_choices_screen()

            return True


class Css(ValidateCode):
    """
        Class to send validated
        CSS code to err().

        ....
        Args:
            str(self.data=(scraped HTML of validated service))
        ....
        Returns:
            Class medthod is not set to
            return True after printed in the terminal
            of either errors or a no error message.
        ....
    """

    def __init__(self, option, data):
        super().__init__(option, data)

        try:
            self.trs = set(self.data.find_all('tr', {'class': 'error'}))
            if self.trs == "'Css' object has no attribute 'data'":
                raise AttributeError(
                    f"No Response: {self.trs}"
                )

        except AttributeError as data_err:
            del_last_lines_up(3)
            print("Ohh.. noo.. There's an error!\n"
                  "Error: Did not receive data from validator, "
                  "instead got:\n"
                  f"{data_err}"
                  "\n\nWhich basically means "
                  "that the validator has an issue.\n")
            sleep(3)

        print("Processing Results..")
        sleep(1)

    def err(self):
        """
            Function to filter
            errors for the terminal.

            ....
            Args:
                str(data=(scraped CSS of validated service))
            ....
            Returns:
                Class is not set to explicitly
                return anything other than printing
                in the terminal of either errors
                or a no error message.
            ....
        """

        error_list = []
        try:
            if self.trs in self.trs == "'Css' object has no attribute 'trs'":
                raise AttributeError()

        except AttributeError:
            error_choose_another_option()
            return True

        else:
            for tr in self.trs:
                tr_text = tr.text

                valid_text = re.findall(VALID_SUBTRING, tr_text)
                for idx in valid_text:
                    index = valid_text.index(idx)
                    if not len(idx) > 6:
                        continue
                    replace_text = re.sub(' : ', ': ', idx)
                    valid_text[index] = replace_text
                error_list.append(valid_text)

            if len(error_list) != 0:
                error_list = set(tuple(err_sub) for err_sub in error_list)
                del_last_lines_up(5)
                print("We received the following errors:\n")

                for err_l in error_list:
                    error_message = re.sub(
                        r"(\s\s+)", ' ', ' '.join(err_l))

                    print(error_message)
                    print()
                    sleep(.4)

                pause(message="\x1b[3mPress any key to continue...\x1b[23m")
                del_last_lines_up(1000)
                print_brand_name()
                run_choices_screen()

            else:
                choose_another_option()

        return True
