import xml.etree.ElementTree as ET
from ftplib import FTP
import inspect
import sys
import os, time
import collections
from datetime import datetime,timezone, timedelta
i=1
stop=0
while (stop == 0):
    
    host = 'youFTPadress'
    ftp = FTP(host) 
    ftp.login('login','pass')
    ftp.cwd('/directoryCopy')
    file=ftp.nlst()

    for bk in file:
        bak=bk 
        ftp.cwd('/directoryCopy/'+bk+"/")
        file=ftp.nlst()
        dtime = datetime.now()- timedelta(minutes = 44640)
        bk_dtime = dtime.strftime('%Y%m%d')
        count=0
        print('loading...')
        for fil in file:
            for create, modify in ftp.mlsd(file[count],facts=['modify']):
                    mod=str(modify['modify'])
                    mod2=mod[:-6]
                    if mod2 <bk_dtime:
                        ftp.delete(create) 
                        print(create,mod2)
            count += 1
            
    ftp.cwd('/directoryCopy2/')
    file=ftp.nlst()

    for bk in file:
        bak=bk 
        ftp.cwd('/directoryCopy2/'+bk+"/")
        file=ftp.nlst()
        dtime = datetime.now()- timedelta(minutes = 44640)
        bk_dtime = dtime.strftime('%Y%m%d')
        count=0
        print('loading...')
        for fil in file:
            for create, modify in ftp.mlsd(file[count],facts=['modify']):
                    mod=str(modify['modify'])
                    mod2=mod[:-6]
                    if mod2 <bk_dtime:
                        ftp.delete(create) 
                        print(create,mod2)
            
            count += 1

i +=1