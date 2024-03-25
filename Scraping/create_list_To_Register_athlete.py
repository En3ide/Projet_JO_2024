###################
# Script de scraping table Date_calendar
###################

##### Import #####
from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime
from create_list_Site import *
from get_id_table_selon_attr import *
from datetime import datetime

##### Code #####
main_url= "https://olympics.com/fr/paris-2024/sites"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
file_name = "transport.json"

def recup_to_register_athlete(event, athlete):
    pass

def send_to_register_athlete(result, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO To_register_athlete (firstname_athlete, name_athlete, birthday_athlete, gender_athlete, code_country) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("firstname_athlete") + "', '" +
            dic.get("name_athlete") + "', '" +
            dic.get("birthday_athlete") + "', " +
            dic.get("gender_athlete") + "', " +
            dic.get("code_country") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql To_register_athlete fini !!!")
    return(send)