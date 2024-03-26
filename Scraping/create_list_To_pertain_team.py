###################
# Script de scraping table To_pertain_team
###################

##### Import #####
from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime
from create_list_Event import *
from create_list_Athlete import *
from get_id_table_selon_attr import *
from datetime import datetime

##### Code #####
main_url= ""
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def recup_to_pertain_team():
    pass

def send_to_register_team(result, athlete_table, team_table, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO To_register_athlete (id_event, id_athlete) VALUES\n"
    to_pertain_team__table = recup_to_pertain_team() # pas fait
    team_i = "NULL" # en utilisant athlete_table, pas fait
    athlete_i = "NULL" # en utilisant team_table, pas fait
    for dic in result:
        send += ("('" + str(athlete_i) + "', '" + str(team_i) + "'),\n")
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
    return send_to_register_team(recup_to_pertain_team())

if __name__ == "__main__":
    send_to_register_team(recup_to_pertain_team())