"""
    init validate code module
"""
import requests
from bs4 import BeautifulSoup
import cfscrape


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

    def __str__(self):
        return str(self.data)


class Html(ValidateCode):
    """
        Subclass to send validation request of html code.
    """

    def __init__(self, data):
        super().__init__(data)

        # print(data)

        self.err = self.data.find_all('li')
        # self.err = self.data.find_all('li', _class='error')
        # self.war = self.data.find_all('li', _class='warning')

    def errors(self):
        """
            Function to find all errors.
        """

        return self.err
        # print(self.war)
