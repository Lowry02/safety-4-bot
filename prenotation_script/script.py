import constantly
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import os
import requests

BASE_URL = "http://localhost:1337/api"
API_TOKEN = "50346ea7f233fd6912ca47ac76019c6f2ee6c8d9f8b7a716c5d86beefc5d8f6d4861a7c1f303a9241bc04d5d7a5f5d19d81d5753b50ced39a44965347c71b8362c54dcdd30c4a797b0048783aab5068c2080d41169c38108f46a369abe141fba99c6f7f487d97fd47d5ae810417c753591871aa7b67aaa480c9e7a5401ae7587"

# ---------- URL to book a room per day ----------

prova = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=lezioniprenota&token=s285853&v1=ED1&v2=Edificio%20H3&v3=971TRIESTE&v4=20220302&v5=1100&v6=ANALISI%20MATEMATICA%20II%0D&v7=Aula%203A%20Edificio%20H3"

lessons_per_day = {
    "0" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=1100&v6=ANALISI%20MATEMATICA%20I&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-'
    ],
    "1" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=1100&v6=GEOMETRIA%201&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-'
    ],
    "2" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=0900&v6=ANALISI%20MATEMATICA%20I&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-',
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=1100&v6=GEOMETRIA%201&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-'
    ],
    "3" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=1100&v6=ANALISI%20MATEMATICA%20I&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-'
    ],
    "4" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=22&v1=ED1&v2=Edificio%20C1&v3=5765TRIESTE&v4={}&v5=1100&v6=GEOMETRIA%201&v7=Aula%20H%20%20-%20Edificio%20C1%20-%20%20%20-'
    ],
    "5" : [],
    "6" : []
}

studyroom_per_day = {
    "0" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=14.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=17.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
    ],
    "1" : [],
    "2" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=14.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=17.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
    ],
    "3" : [
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=14.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
        'https://us-central1-eiloborg.cloudfunctions.net/s4aweb?token=s285853&c={}&f=20&v1=17.00&v2=ED1&v3=Edificio%20H3%20SPAZIO%20STUDIO%203%20e%20piano%205&v4=SER49&v5={}',
    ],
    "4" : [],
    "5" : [],
    "6" : []
}

# ----------- FUNCTIONS -------------

def get_tomorrow_week_day():
    return str(datetime.datetime.today().weekday() + 1 % 7)

def get_tomorrow_date():
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_date_format = str(tomorrow.year) + str(tomorrow.month).zfill(2) + str(tomorrow.day).zfill(2)
    return tomorrow_date_format

def book_room(username, nome, edificio, aula, tipo, codice, ora):
    tipo = "lezioniprenota" if tipo == "Lezione" else ""
    edificio = edificio.replace(" ", "%20")
    nome = nome.replace(" ", "%20")
    aula = aula.replace(" ", "%20")
    tomorrow = get_tomorrow_date()
    url = f"https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f={tipo}&token={username}&v1=ED1&v2={edificio}&v3={codice}&v4={tomorrow}&v5={ora}&v6={nome}%0D&v7={aula}%20{edificio}"    
    command = "curl '" + url + "'"
    os.system(command)
    print(url)

def get_token():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("file:///Users/lorenzocusin/Documents/Safety4All/index.html")
    token = driver.find_element_by_id("token").text
    driver.close()
    return token

def login(username, password):
    url = f"https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=0&v1={username}&v2={password}"
    command = "curl '" + url + "'"
    os.system(command)

# ----------- MAIN -----------------

# login APP with API_TOKEN
room_list = requests.get(f"{BASE_URL}/aule", headers={'Authorization' : f"Bearer {API_TOKEN}"}).json()

# organize room per user
room_per_user = {}
for item in room_list:
    username = item['esse3username']
    if not username in room_per_user.keys():
        room_per_user[username] = [item]
    else:
        room_per_user[username].push(item)

# book rooms per user
for username in room_per_user.keys():
    for room in room_per_user[username]:
        password = room['esse3psw']
        login(username, password)
        book_room(
            username=username,
            nome=room['Nome'],
            edificio=room['Edificio'],
            aula=room['Aula'],
            tipo=room['Tipo'],
            codice=room['Codice'],
            ora=room['Ora']
        )