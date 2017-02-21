
import  subprocess
import os
import sqlite3
from datetime import datetime, date, time
today = datetime.now()
DB = '/Users/steven/OneDrive/WWW/code/Django170212/djangoproject/db.sqlite3'
cmd = 'speedtest-cli --csv' #cmd = 'ls -l /tmp'

# Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload
#a = '4068,Bytemark Hosting,York,2017-02-11T21:30:00.326709,32.1327997839918,27.114,34071279.72141616,8588335.028817672'

a = subprocess.getoutput(["speedtest-cli --csv"])
print(a)
b = a.split(',') # 
print(b)

conn = sqlite3.connect(DB) 
cur = conn.cursor()
cur.execute('INSERT INTO speed_speed (ServerID,Sponsor,ServerName,Timestamp,Distance,Ping,Download,Upload) VALUES ( ?, ?, ?, ? ,?,?,?,?)', (b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]) ) 
conn.commit()
