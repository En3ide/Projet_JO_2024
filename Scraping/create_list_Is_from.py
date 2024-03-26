###################
# Script de scraping table Date_calendar
###################

##### Import #####
from create_list_Site import *
from utilitary_function import *
from datetime import datetime
from create_list_Athlete import recup_athlete
from create_list_Country import recup_country
import sqlite3

##### Code #####
def recup_is_from(athlete, country):
    result = []
    for ath in athlete:
        result.append({"id_athlete": athlete.index(ath), "code_country": ath.get("code_country")})
        #result.append({"id_athlete": athlete.index(ath), "code_country": ath.get("code_country")})
    print('[',datetime.now().time(),'] ', "sql Is_from fini !!!")
    return result

def send_is_from(result, bdd=""):
        # Création de la requête SQL
    send = "INSERT INTO Is_from (id_athlete, code_country) VALUES\n"
    for dic in result:
        send += ("(" + str(dic.get("id_athlete")) + ", '" +
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

# print(create_sql(recup_athlete(), recup_country()))