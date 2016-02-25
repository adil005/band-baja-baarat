import sqlite3

conn=sqlite3.connect('adi.db')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Myhalls ')
cur.execute('CREATE TABLE Myhalls (city varchar(255),locality varchar(255),hall_name varchar(255),contact_hall int,address_hall TEXT,distance_hall FLOAT )')
cur.execute('DROP TABLE IF EXISTS Mycaters')
cur.execute('DROP TABLE IF EXISTS Mytents')
cur.execute('CREATE TABLE Mycaters(city varchar(255),cater_name varchar(255),locality varchar(255),contact_cater int,address_cater TEXT )')
cur.execute('CREATE TABLE Mytents (city varchar(255),tent_name varchar(255),locality varchar(255),contact_tent int,address_tent TEXT )')
conn.close()
