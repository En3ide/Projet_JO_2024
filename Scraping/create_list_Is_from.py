###################
# Script de scraping table Date_calendar
###################

##### Import #####
from bs4 import BeautifulSoup
from create_list_Site import *
from get_id_table_selon_attr import *
from datetime import datetime
import requests, ast, sqlite3, re, locale

##### Code #####
main_url= "https://olympics.com/fr/paris-2024/sites"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
file_name = "transport.json"

def recup_url_transp(athlete, country):
    result = []
    for ath in athlete:
        result.append({"id_athlete": ath.index(), "code_country": ath.get("code_country")})
        for country in ath.get("code_country"):
            result.append({"id_athlete": ath.index(), "code_country": country})
    print('[',datetime.now().time(),'] ', "sql Record fini !!!")
    return result

def send_is_from(is_from):
        # Création de la requête SQL
    send = "INSERT INTO Is_from (id_athlete, ) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("stat_record") + "', '" +
            dic.get("date_record") + "', '" +
            dic.get("id_event") + "', " +
            dic.get("id_athlete") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql Record fini !!!")
    return(send)