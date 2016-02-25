import requests
from bs4 import BeautifulSoup
import sqlite3

def tent(city,locality):
   conn=sqlite3.connect('adi.db')
   cur=conn.cursor()
   url='http://yellowpages.sulekha.com/tents-tarpaulin-suppliers-rentals_'+city
   r=requests.get(url) #web scraping is done for tents data using beautiful soup
   s=BeautifulSoup(r.content)
   k=s.find_all("li",{"class":"list-item"})
   for item in k:
      try:
         a=item.find_all("a",{"class":"YPTRACK GAQ_C_BUSL"})[0].text
      except:
         pass
      try:
         b=item.find_all("b",{"class":"contact-number"})[0].text
      except:
         pass
      try:
         c=item.find_all("address",{"class":"pull-left"})[0].text
      except:
         pass
      cur.execute('INSERT INTO Mytents(city,tent_name,locality,contact_tent,address_tent) VALUES(?,?,?,?,?)',(city,a,locality,b,c))
      conn.commit()
   conn.close()
