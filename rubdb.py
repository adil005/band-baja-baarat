import sqlite3
from weather_condition import *
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
import uuid
app = Flask(__name__)
auth=HTTPBasicAuth()
users = {
    "joh": "hell",
    "susan": "bye"
}
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/get_key/') #url to fetch api_key
@auth.login_required
def get_newtasks():
    uid=uuid.uuid4()  
    api_key=uid.hex #generating random alphanumeric string
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO takekey(key,key2) Values (?,?)',(api_key,1)) #inserting key in database and also the other coloum has no significance 
    conn.commit()
    conn.close()
    return ("your  api key is  "+api_key) #returning to server
    


    
@app.route('/bandbaaja-baarat/<string:city>/<string:locality>/<string:key>/<string:date>', methods=['GET']) #url for bandbaaja-baarat api
def get_tasks(city,locality,key,date):
    #city=raw_input('Enter the city name: ')
    #locality=raw_input('enter the locality: ')
    #date=raw_input('Enter the no of days after which u want result <=15 ')
    flag=0
    flag2=0
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    for row in cur.execute("SELECT  * FROM takekey WHERE key=? AND key2=?",(key,1)): #checking whether key which user is trying to access api matches with the one present in database
        flag2=1
        break
    if flag2==1:
        tasks=[]
        tasks.append({"city":{"name":city,"area":locality}})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality)):
            flag=1
            break
        if flag==0:
            not_in_db(city,locality,date) #if data is not present in database      
        for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0: #accessing data from database
                tasks.append({"marriage_lawn/halls":[{"ma_name":row[2],
                            "ma_address":row[4],
                            "ma_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[1]["marriage_lawn/halls"].append({"ma_name":row[2],
                        "ma_address":row[4],
                        "ma_contact":row[3]})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Mycaters WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0:
                tasks.append({"marriage_catering":[{"cat_name":row[1],
                        "cat_address":row[4],
                        "cat_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[2]["marriage_catering"].append({"cat_name":row[1],
                        "cat_address":row[4],
                        "cat_contact":row[3]})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Mytents WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0:
                tasks.append({"marriage_tents":[{"tents_name":row[1],
                        "tents_address":row[4],
                        "tents_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[3]["marriage_tents"].append({"tents_name":row[1],
                        "tents_address":row[4],
                        "tents_contact":row[3]})
        return jsonify({'tasks': tasks}) #returnning json format tasks list to a server

if __name__ == '__main__':
    app.run(debug=True,port=9630) #running server
conn.close()        
