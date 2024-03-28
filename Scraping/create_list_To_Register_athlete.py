###################
# Script de scraping table To_register_athlete
###################

##### Import #####
import sqlite3
from datetime import datetime
from create_list_Event import *
from create_list_Athlete import *
from utilitary_function import *
from datetime import datetime

##### Code #####
main_url= ""
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def recup_to_register_athlete():
    pass

def send_to_register_athlete(result, event_table, athlete_table, bdd=""):
    # Création de la requête SQL
    send = "INSERT IGNORE INTO To_register_athlete (id_event, id_athlete) VALUES\n"
    event_id = "NULL" # en utilisant event_table, pas fait
    athlete_id = "NULL" # en utilisant athlete_table, pas fait
    for dic in result:
        send += ("(" + str(event_id) + ", " + str(athlete_id) + "),\n")
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

if __name__ == "__main__":
    #send_to_register_athlete(recup_to_register_athlete())
    pass