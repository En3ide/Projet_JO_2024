###################
# Script de scraping table Team
###################

##### Import #####
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
from create_list_Event import *
from create_list_Athlete import *
from utilitary_function import *
from datetime import datetime

##### Code #####
main_url= ""
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def recup_team():
    pass

def send_team(result, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO Team (size_team, type_medal, code_country) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("size_team") + "', '" +
            dic.get("type_medal") + "', '" +
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

def create_sql():
    return send_team(recup_team())

if __name__ == "__main__":
    send_team(recup_team())