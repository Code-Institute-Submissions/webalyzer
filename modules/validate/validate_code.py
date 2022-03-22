"""
    init validate code module
"""

from time import sleep
import requests
from bs4 import BeautifulSoup
import cfscrape
from getch import pause
from modules.utils import Validate
from modules.utils import del_last_lines_up
from modules.prints import print_brand_name, run_choices_screen


class ValidateCode:
    """
        Class to validate requested codes from options.
    """

    def __init__(self, option, url):
        self.option = option
        self.url = url

        self.html = f"https://validator.nu/?doc={url}"
        self.css = f"https://jigsaw.w3.org/css-validator/validator?uri={url}"
        self.javascript = "https://jshint.com"

        if self.option == '1':
            with requests.Session() as re_s:
                re_s = cfscrape.create_scraper()
                re_s.headers = {'Referrer': 'https://webalyzer.heokuapp.com',
                                'User-Agent': 'Mozilla/5.0 (platform; '
                                'rv:geckoversion) Gecko/geckotrail '
                                'Firefox/firefoxversion',
                                'Accept': 'text/html',
                                'Accept-Encoding': 'gzip, compress', }
                res = re_s.get(self.html)

        elif self.option == '2':
            with requests.Session() as re_s:
                re_s = cfscrape.create_scraper()
                re_s.headers = {'Referrer': 'https://webalyzer.heokuapp.com',
                                'User-Agent': 'Mozilla/5.0 (platform; '
                                'rv:geckoversion) Gecko/geckotrail '
                                'Firefox/firefoxversion',
                                'Accept': 'text/html',
                                'Accept-Encoding': 'gzip, compress', }
                res = re_s.get(self.css)

        else:
            with requests.Session() as re_s:
                re_s = cfscrape.create_scraper()
                re_s.headers = {'Referrer': 'https://webalyzer.heokuapp.com',
                                'User-Agent': 'Mozilla/5.0 (platform; '
                                'rv:geckoversion) Gecko/geckotrail '
                                'Firefox/firefoxversion',
                                'Accept': 'text/html',
                                'Accept-Encoding': 'gzip, compress', }
                res = re_s.get(self.javascript)

        self.data = BeautifulSoup(res.content, 'html5lib')

    def __str__(self):
        return str(self.data)


class Html(ValidateCode):
    """
        Class to send validation request of html code.
    """

    def __init__(self, option, data):
        super().__init__(option, data)
        self.all_li = self.data.find_all('li')

    def err(self):
        """
            Function to filter and beautify
            errors for the terminal.
        """

        all_lis = self.data.find_all('li', class_='error')

        errors = []
        location = []
        for error in all_lis:
            err = error.find('p').text
            loc = error.find('p', class_='location').text
            errors.append(err)
            location.append(loc)

        error_list = list(zip(errors, location))

        if not len(error_list) == 0:
            print("We received the following errors:\n")

            for error in error_list:
                for line in error:
                    print(line)
                sleep(.4)
                print()

            pause("Press any key to continue...")
            del_last_lines_up(1000)
            print_brand_name()
            run_choices_screen()

        else:
            del_last_lines_up(2)
            print("Well done, there were no errors!")
            # Creating a new Validate object
            another = Validate.another_cls()

            # Validating the input against valid items
            another[0].validate_input(another[0], another[1])


class Css(ValidateCode):
    """
        Class to send validation request of html code.
    """

    def __init__(self, option, data):
        super().__init__(option, data)
        self.trs = self.data.find_all('tr', attrs={'class': 'error'})

    def err(self):
        """
            Function to filter and beautify
            errors for the terminal.
        """

        tds_list = []
        for tr in self.trs:
            on_line = "On line "
            rem_text = (" : \n                                "
                        "\n                                    ")
            tds = tr.find_all('td')
            for td in tds:
                td_text = td.text.strip()
                if len(td_text) == 0:
                    continue
                elif rem_text in td_text:
                    ioc = td_text.index(" :")
                    valid_text = td_text[0:ioc]
                    bad_part = td_text[ioc:]
                    last = bad_part[73:]
                    tds_list.append(valid_text + ": " + last)
                    continue
                elif int(td_text):
                    tds_list.append(on_line + td_text + ": ")

        if len(tds_list) != 0:
            print("We received the following errors:\n")

            seq = iter(tds_list)
            for _ in seq:
                two_and_two = _ + next(seq)
                print(two_and_two)
                sleep(.2)

            pause("Press any key to continue...")
            del_last_lines_up(1000)
            print_brand_name()
            run_choices_screen()

        else:
            del_last_lines_up(2)
            print("Well done, there were no errors!")
            # Creating a new Validate object
            another = Validate.another_cls()

            # Validating the input against valid items
            another[0].validate_input(another[0], another[1])
