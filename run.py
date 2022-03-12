"""
Provides access to python requests module
"""
import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://api.github.com/users/mtraveller')

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
