#<img src="/upload/shield/superbrands-50-l.jpg">

import requests
from bs4 import BeautifulSoup

def getHtml (url):
    r = requests.get(url)
    return r.text

def getSoup_appearedOrNot (html):
    soup = BeautifulSoup (html, 'html.parser')
    soupForCheking = soup.find_all ('img')
    return soupForCheking

urls = ['https://www.eldorado.ru/special/550985894/?filter_category[1624320]=On',
        'https://www.eldorado.ru/special/550985894/page/2/?filter_category[1624320]=On',
        'https://www.eldorado.ru/special/550985894/page/3/?filter_category[1624320]=On']

print (getSoup_appearedOrNot(getHtml(urls[0])))
