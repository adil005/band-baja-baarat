import sqlite3
from weather_condition import *
city=raw_input('Enter the city name: ')
locality=raw_input('enter the locality: ')
date=raw_input('Enter the no of days after which u want result <=15 ')
flag=0
conn=sqlite3.connect('adi.db')
cur=conn.cursor()
for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality)):
        flag=1
        break
if flag==0:
        not_in_db(city,locality,date)       
else:
        for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality )):
                print row
        print ('catering one\n\n')
        for row in cur.execute('SELECT * FROM Mycaters WHERE city=? AND locality=?',(city,locality )):
                print row
        print ('tent one\n')
        for row in cur.execute('SELECT * FROM Mytents WHERE city=? AND locality=?',(city,locality )):
                print row
conn.close()        
