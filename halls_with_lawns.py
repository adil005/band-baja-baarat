import requests
from bs4 import BeautifulSoup
from distance import *
from catering import *
from tents import *
import sqlite3

def with_lawns(city,current_add):
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    url='http://www.matrimonydirectory.com/wedding-venues-in-' +city
    r=requests.get(url)
    s=BeautifulSoup(r.content) #web scraping is done to fetch data of wedding halls
    ob1=s.find_all("div",{"class":"listing-top clearfix"})
    i=0
    j=0
    x=()
    arr=[]
    for link in ob1:
        i=0
        string=link.find_all("p",{"class":"list-address list-map-address"})[0].text.replace("| Map"," ")
        try:
            di=finddistance(current_add,city,string) #distancematrix api is used to know the distance bt ur locality & hall
            di=di.replace(' km','') #di is string
            x=(float(di),link) #tuple is made with first data as distance
            arr.append(x)
        except:
            pass
    arr.sort() #array is sorted w.r.t distance

    for ob1 in arr:
        try:
            d=ob1[0]
        except:
            pass
        try:
            a=ob1[1].find_all("p",{"class":"list-heading"})[0].text
        except:
            pass
        try:
            c=ob1[1].find_all("p",{"class":"list-address list-map-address"})[0].text.replace("| Map"," ")
        except:
            pass
        try:
            b=ob1[1].find_all("div",{"class":"right-list right-call right-text"})[0].text
        except:
            pass
        cur.execute('INSERT INTO Myhalls(city,locality, hall_name, contact_hall, address_hall, distance_hall) Values (?,?,?,?,?,?)',(city,current_add,a,b,c,d))
        conn.commit()
    conn.close()        
    print ('CATERING WALAS on work \n ')
    caters(city,current_add)
    print ('TENTS WALAS on work \n ')
    tent(city,current_add)
    
