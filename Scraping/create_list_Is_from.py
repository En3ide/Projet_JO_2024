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

def recup_is_from(athlete, country):
    result = []
    for ath in athlete:
        result.append({"id_athlete": athlete.index(ath), "code_country": ath.get("code_country")})
        for country in ath.get("code_country"):
            result.append({"id_athlete": athlete.index(ath), "code_country": country})
    print('[',datetime.now().time(),'] ', "sql Is_from fini !!!")
    return result

def send_is_from(result, bdd=""):
        # Création de la requête SQL
    send = "INSERT INTO Is_from (id_athlete, code_country) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("id_athlete") + "', '" +
            dic.get("code_country") + "'),\n")
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

def create_sql(athlete, country):
    return send_is_from(recup_is_from(athlete, country))