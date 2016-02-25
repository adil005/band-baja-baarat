import json
import requests
from halls_with_lawns import *
from halls_without_lawns import *

def not_in_db(city,locality,date):
    url2='http://api.openweathermap.org/data/2.5/forecast/daily?q='+city+'&mode=json&units=metric&cnt='+date+'&appid=44db6a862fba0b067b1930da0d769e98'
    response=requests.get(url2)
    load_text=json.loads(response.content)
    i=0
    flag=0
    for link in load_text["list"]: #using weather api to know if it will rain or not
        for link2 in link["weather"]:
            i=i+1
            if i == int (date):
                flag=1
                break
        if flag:
            break

    if 'rain' in link2["description"]: #once rain is detected halls without lawn should be booked 
        print ('It seems like RAINING on that day so halls without lawns recommended: ')
        without_lawns(city,locality)

    else:
        print ('there is no sign of rain so u can have halls with lawn: ')
        with_lawns(city,locality)

    
