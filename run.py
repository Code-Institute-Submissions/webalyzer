import requests
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/assets/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

# Making a GET request
r = requests.get('https://api.github.com/users/mtraveller')
  
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.content)
