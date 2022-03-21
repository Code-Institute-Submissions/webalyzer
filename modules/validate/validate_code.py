"""
    init validate code module
"""

from subprocess import run
import requests
from bs4 import BeautifulSoup
import cfscrape
from getch import pause
from modules.utils import Validate
# from modules.utils import del_last_lines_up
from modules.prints import run_choices_screen


class ValidateCode:
    """
        Class to validate requested codes from options.
    """

    def __init__(self, url):
        self.url = url

        self.html = f"https://validator.nu/?doc={url}"
        self.css = f"https://jigsaw.w3.org/css-validator/validator?uri={url}"
        self.javascript = "https://jshint.com"

        with requests.Session() as re_s:
            re_s = cfscrape.create_scraper()
            re_s.headers = {'Referrer': 'https://webalyzer.heokuapp.com',
                            'User-Agent': 'Mozilla/5.0 (platform; '
                            'rv:geckoversion) Gecko/geckotrail '
                            'Firefox/firefoxversion',
                            'Accept': 'text/html',
                            'Accept-Encoding': 'gzip, compress', }
            res = re_s.get(self.html)

        self.data = BeautifulSoup(res.content, 'html5lib')
        self.data.prettify()

    def __str__(self):
        return str(self.data)


class Html(ValidateCode):
    """
        Class to send validation request of html code.
    """

    def __init__(self, data):
        super().__init__(data)
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
                print("\n")

            pause("Press any key to continue...")
            run('clear', check=True)
            run_choices_screen()

        else:
            print("Well done, there were no errors!")
            # Creating a new Validate object
            another = Validate.another_cls()

            # Validating the input against valid items
            another[0].validate_input(another[0], another[1])

        return
