from django.db import models
from django.utils import timezone

class Speed(models.Model):
# Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload
# 4068,Bytemark Hosting,York,2017-02-11T21:30:00.326709,32.1327997839918,27.114,34071279.72141616,8588335.028817672
    ServerID = models.IntegerField()
    Sponsor = models.CharField(max_length=64)
    ServerName = models.CharField(max_length=64)
    Timestamp = models.DateTimeField()
    Distance = models.DecimalField(max_digits=20, decimal_places=10)
    Ping = models.DecimalField(max_digits=20, decimal_places=10)
    Download = models.DecimalField(max_digits=20, decimal_places=10)
    Upload = models.DecimalField(max_digits=20, decimal_places=10)

    def publish(self):
        cmd = 'speedtest-cli --csv' #cmd = 'ls -l /tmp'
#        a = commands.getstatusoutput(cmd)

        a = '4068,Bytemark Hosting,York,2017-02-11T21:30:00.326709,32.1327997839918,27.114,34071279.72141616,8588335.028817672'
        b = a[1].split()
        self.ServerID = b[0]
        self.Sponsor = b[1]
        self.ServerName = b[2]
        self.Timestamp = timezone.now() # b[3]
        self.Distance = b[4]
        self.Ping = b[5]
        self.Download = b[6] 
        self.Upload = b[7]
        self.save()

    def __str__(self):
        return self.ServerName


'''
import commands
import os
import sqlite3
from datetime import datetime, date, time
today = datetime.now()
DB = '/var/www/lab_app/speedtest.db'
cmd = 'speedtest-cli --simple' #cmd = 'ls -l /tmp'

#a = (0, 'Ping: 89.409 ms\nDownload: 3.43 Mbit/s\nUpload: 0.13 Mbit/s')
a = commands.getstatusoutput(cmd)
 
b = a[1].split()
#print b

Ping		= b[1] #89.409 ms\n
Download 	= b[4] #: 3.43 Mbit/s\n
Upload 		= b[7] #: 0.13 Mbit/s'

print  Ping, Download, Upload

#conn = sqlite3.connect(DB) 
#cur = conn.cursor()
#cur.execute('DROP TABLE IF EXISTS speedtest ') 
#cur.execute('CREATE TABLE speedtest (dates datetime, Ping numeric, Download numeric, Upload numeric)')
#conn.close()

conn = sqlite3.connect(DB) 
cur = conn.cursor()
cur.execute('INSERT INTO speedtest (dates, Ping, Download, Upload) VALUES ( ?, ?, ?, ? )', (today,  Ping, Download, Upload ) ) 
conn.commit()


cmd = 'ls -l' #speedtest-cli --simple> $log
import os
os.system('sample_cmd > tmp')
print open('tmp', 'r').read()
print 'speedtest:' 
cur.execute('SELECT dates, Ping, Download, Upload from speedtest') 
for row in cur : 
	print row
#cur.execute('DELETE FROM temperatures WHERE temp < 100') 


conn.commit()

'''        