import os, base64, requests, json
from time import sleep
from random import choice
from requests_futures.sessions import FuturesSession
from threading import Thread
from random import randint
from itertools import cycle
with open('config.json') as lol:
  config = json.load(lol) 

token = config.get('token')
minwork = config.get('Min-Workers')
maxwork = config.get('Max-Workers')
img = config.get('gcimage')
session = FuturesSession(max_workers=randint(minwork,maxwork),)
ps = []
prox = cycle(ps)

with open('img.png', 'wb') as f:
    r = requests.get(img, stream=True)
    for block in r.iter_content(1024):
        if not block:
            break
        f.write(block)

for line in open('proxies.txt'):
    ps.append(line.replace('\n', ''))

os.system("cls & mode 70,25 & title GC Bomber")
clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

cum = 0
bum = 0
num = 0
pum = 0
gum = 0

def ui():
    print(f'''
                ╔═╗  ╔═╗  ╔╗   ╔═╗  ╔╦╗  ╔╗   ╔═╗  ╦═╗
                ║ ╦  ║    ╠╩╗  ║ ║  ║║║  ╠╩╗  ║╣   ╠╦╝
                ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╩ ╩  ╚═╝  ╚═╝  ╩╚═
        [1] Mass Create GC     |    [2] Leave Gcs on Token
        [3] Rename Gcs         |    [4] Invite Victim to GCS
        [5] Remove from GCS    |    [6] Spam Invite & Leave
        [7] Change Icon in GCS |    [8] Scrape All Gcs
    ''')

def ui2():
    print('''
                ╔═╗  ╔═╗  ╔╗   ╔═╗  ╔╦╗  ╔╗   ╔═╗  ╦═╗
                ║ ╦  ║    ╠╩╗  ║ ║  ║║║  ╠╩╗  ║╣   ╠╦╝
                ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╩ ╩  ╚═╝  ╚═╝  ╩╚═
    ''')

def invnkick( uid,cIDS):
    while True:
        try:
            headers = {"Authorization": token}
            r = requests.put(f'https://canary.discordapp.com/api/v{randint(6,9)}/channels/{cIDS}/recipients/{uid}', headers=headers,proxies={"http": 'http://' + next(prox)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[ + ] Invited [ {uid} ] | In [ {cIDS} ] | ")
            elif r.status_code == 429:
                print(f"[ - ] Failed to invite [ {uid} ] | In [ {cIDS} ]")
            b = requests.delete(f'https://canary.discordapp.com/api/v{randint(6,9)}/channels/{cIDS}/recipients/{uid}', headers=headers, proxies={"http": 'http://' + next(prox)}).result()
            if b.status_code == 200 or b.status_code == 201 or b.status_code == 204:
                print(f"[ + ] Removed [ {uid} ] | In [ {cIDS} ] ")
            elif b.status_code == 429:
                print(f"[ - ] Failed to Remove [ {uid} ] | In [ {cIDS} ]")
        except:
            return
        sleep(2)

def invtogc(uid, cIDS):
    try:
        headers = {"Authorization": token}
        r = session.put(f'https://canary.discordapp.com/api/v{randint(6,9)}/channels/{cIDS}/recipients/{uid}', headers=headers).result()
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"[ + ] Invited [ {uid} ] | In [ {cIDS} ] ")
        elif r.status_code == 429:
            print(f"[ - ] Failed to invite [ {uid} ] | In [ {cIDS} ]")
    except:
        return
    sleep(2)

def remfromgc(uid, cIDS):
    try:
        headers = {"Authorization": token}
        r = requests.delete(f'https://canary.discordapp.com/api/v{randint(6,9)}/channels/{cIDS}/recipients/{uid}', headers=headers, proxies={"http": 'http://' + next(prox)})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"[ + ] Removed [ {uid} ] | In [ {cIDS} ] ")
        elif r.status_code == 429:
            print(f"[ - ] Failed to Remove [ {uid} ] | In [ {cIDS} ]")
    except:
        return
    sleep(2)


def creategc(tokenn, uid, name):
    global pum
    t = base64.b64encode(open("img.png", "rb").read()).decode('ascii')
    try:
        headers2 = {"Authorization": tokenn}
        b = session.get("https://canary.discordapp.com/api/v6/users/@me", headers=headers2, proxies={"http": 'http://' + next(prox)}).result()
        tokenid = b.json()
        idd = tokenid['id']
    except:
        return
    try:
        headers = {"Authorization": tokenn,"Content-Type" : "application/json"}
        headers2 = {'Authorization': token,"Content-Type": "application/json"}
        json = {"recipients":[ f"{idd}",f"{uid}"]}
        r = session.post(f'https://discordapp.com/api/v{randint(6,9)}/users/@me/channels', headers=headers, json=json, proxies={"http": 'http://' + next(prox)}).result()
        gcID2 = r.json()
        session.patch(f"https://discordapp.com/api/v{randint(6,9)}/channels/{gcID2['id']}", headers=headers2, json={"name": f"{name}","icon": f"data:image/png;base64,{t}"}, proxies={"http": 'http://' + next(prox)})
        pum += 1
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            gcID = r.json()
            print(f"[ + ] created GC | GC ID [ {gcID['id']} ] | {pum}")
            with open('groupids.txt', 'a') as pp:
                pp.write(gcID['id'] + "\n")
            session.delete(f"https://discordapp.com/api/v{randint(6,9)}/channels/{gcID['id']}", headers=headers, proxies={"http": 'http://' + next(prox)})
        elif r.status_code == 429:
            print(f"[ - ] ratelimited | {pum}")
    except:
        return
    sleep(2)

def leavegcs(gcs):
    global bum
    try:
        headers = {"Authorization": token,"Content-Type" : "application/json"}
        r = requests.delete(f"https://canary.discordapp.com/api/v{randint(6,9)}/channels/{gcs}", headers=headers, proxies={"http": 'http://' + next(prox)})
        bum += 1
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"[ + ] Left [ {gcs} ] | {bum}")
        elif r.status_code == 429:
            print(f"[ - ] Couldn't Leave [ {gcs} ] | {bum}")
    except:
        return
    sleep(2)

def rename(cIDS, name):
    global num
    try:
        headers = {"Authorization": token, "Content-Type": "application/json"}
        json = {"name": f"{name}"}
        num += 1
        r = requests.patch(f"https://discordapp.com/api/v{randint(6,9)}/channels/{cIDS}", headers=headers, json=json, proxies={"http": 'http://' + next(prox)})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"[ + ] Renamed [ {cIDS} ] | {name} | {num}")
        elif r.status_code == 429:
            print(f"[ - ] Couldn't Rename [ {cIDS} ] | {num}")
    except:
        return
    sleep(2)
def changemg(cIDS):
    global cum
    try: 
        ttoken = config.get('token')
        headers = {'Authorization': ttoken,"Content-Type": "application/json"}
        t = base64.b64encode(open("img.png", "rb").read()).decode('ascii')
        r = session.patch(f"https://canary.discordapp.com/api/v{randint(6,9)}/channels/{cIDS}", headers=headers, json={"icon": f"data:image/png;base64,{t}"}).result()
        cum += 1
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"[ + ] Changed Icon in [ {cIDS} ] | {cum}")
        elif r.status_code == 429:
            print(f"[ - ] Couldn't Change in [ {cIDS} ] | {cum}")
    except:
        return
    sleep(2)

def scrgc():
    global gum
    try:
        s = open("groupids.txt", "w+")
        headers = {"Authorization": token}
        r = session.get(f"https://canary.discordapp.com/api/v9/users/@me/channels", headers=headers).result()
        gc = r.json()
        for idd in gc:
            gum += 1
            if(idd['type'] == 3): 
                print(f"[ + ] Scraped [ {idd['id']} ] | {gum}")
                s.write(idd['id'] + "\n")
    except:
        return
    sleep(2)
        

def gcc():
    clear()
    ui2()
    ts = []
    for t in token:
        t = Thread(target=scrgc)
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

def imgch(): 
    url = input("image url: ")
    with open('img.png', 'wb') as f:
        r = requests.get(url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"loaded {len(gc)} group ids")
    clear()
    ui2()
    ts = []
    for cIDS in gc:
        t = Thread(target=changemg, args=(cIDS,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()


def bomb(uid):
    name = config.get("names")
    tokens = []
    for line in open("tokens.txt"):
        tokens.append(line.strip('\n'))
    print(f"Loaded {len(tokens)} tokens")
    clear()
    ui2()
    ts = []
    for tokenn in tokens:
        t = Thread(target=creategc, args=(tokenn,uid,name))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

def gcleave():
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"Loaded {len(gc)} group ids")
    clear()
    ui2()
    ts = []
    for gcs in gc:
        t = Thread(target=leavegcs, args=(gcs,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

def gcrename():
    name = input("Channel Names: ")
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"Loaded [ {len(gc)} ] group ids")
    clear()
    ui2()
    ts = []
    for cIDS in gc:
        t = Thread(target=rename, args=(cIDS, name,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
        
def gcinv():
    uid = input("User id: ")
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"Loaded [ {len(gc)} ] group ids")
    clear()
    ui2()
    ts = []
    for cIDS in gc:
        t = Thread(target=invtogc, args=(uid, cIDS,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

def gcrem():
    uid = input("User id: ")
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"Loaded [ {len(gc)} ] group ids")
    clear()
    ui2()
    ts = []
    for cIDS in gc:
        t = Thread(target=remfromgc, args=(uid, cIDS,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

def gcspamanr():
    print("in order to stop this, restart it because its looped.")
    uid = input("User id: ")
    gc = []
    for line in open("groupids.txt"):
        gc.append(line.strip('\n'))
    print(f"Loaded [ {len(gc)} ] group ids")
    clear()
    ui2()
    ts = []
    for cIDS in gc:
        t = Thread(target=invnkick, args=(uid, cIDS,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
 

def Menu():
    while True:
        clear()
        ui()
        an = input("Choice: ")
        if an == "1":
            uid = input("User id: ")
            for i in range(500):
                bomb(uid)
        elif an == "2":
            gcleave()
        elif an == "3":
            gcrename()
        elif an == "4":
            gcinv()
        elif an == "5":
            gcrem()
        elif an == "6":
            gcspamanr()
        elif an == "7":
            imgch()
        elif an == "8":
            scrgc()

Menu()
