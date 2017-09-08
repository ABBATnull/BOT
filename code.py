import requests
from bs4 import BeautifulSoup

def getHtml (url):
    r = requests.get(url)
    return r.text

def getSoup_appearedOrNot (html, pageNumber):
    soup = BeautifulSoup (html, 'html.parser')
    soupForCheking = soup.find_all ('img')
    howManyTimes = 0
    for i in soupForCheking:
        print (i, '\n')
        if ('upload/shield/superbrands-50-l.jpg' in i):
            howManyTimes += 1

    print (str(howManyTimes), 'СОВПАДЕНИЙ НА ', str(pageNumber), 'СТРАНИЦЕ!\n')            

urls = ['https://www.eldorado.ru/special/550985894/?filter_category[1624320]=On',
        'https://www.eldorado.ru/special/550985894/page/2/?filter_category[1624320]=On',
        'https://www.eldorado.ru/special/550985894/page/3/?filter_category[1624320]=On']

getSoup_appearedOrNot(getHtml(urls[0]), 1)
getSoup_appearedOrNot(getHtml(urls[1]), 2)
getSoup_appearedOrNot(getHtml(urls[2]), 3)
