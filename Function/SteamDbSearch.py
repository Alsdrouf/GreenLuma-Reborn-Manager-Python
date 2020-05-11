import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = 'https://steamdb.info/search/?a=app&q=M'
response = requests.get(url)
