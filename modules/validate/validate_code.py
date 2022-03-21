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
        self.all_li = self.data.find_all('li')

    def extract(self):
        """
            Extract relevant text
        """
        extracted = []
        for li in self.all_li:
            span = li.find('span')
            extracted.append(span)

        return extracted

    def err(self):
        """
            Function to filter and beautify
            errors for the terminal.
        """
        result = self.extract()

        return result
