import requests
from bs4 import BeautifulSoup

def caters(city): #web scraping is done to fetch data for caters using beautiful soup
    url='http://yellowpages.sulekha.com/catering-services_'+city
    r=requests.get(url)
    s=BeautifulSoup(r.content)
    g=s.find_all("li",{"itemtype":"http://schema.org/LocalBusiness"})
    for item in g:
        try:
            print item.find_all("a",{"class":"YPTRACK GAQ_C_BUSL"})[0].text
            print item.find_all("b",{"class":"contact-number"})[0].text
        except:
            pass
        try:
            print item.find_all("address",{"class":"pull-left"})[0].text
        except:
            pass
        print "\n"
