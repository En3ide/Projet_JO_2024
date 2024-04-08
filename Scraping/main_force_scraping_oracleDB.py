from multiprocessing import Pool
from create_list_Transport import *
from create_list_Site import *
from create_list_Athlete import *
from create_list_Country import *
from create_list_Discipline import *
from create_list_Record import *
from create_list_To_Serve import *
from create_list_Event import *
from create_list_Date_calendar import *
from create_list_Is_from import *
from datetime import datetime
from utilitary_function import *
from connect_to_bdd import *
import os, subprocess, mysql.connector

def installer_requirements(fichier_requirements):
    """
    Installe les dépendances spécifiées dans un fichier requirements.txt
    Args:
    - fichier_requirements (str): Le chemin vers le fichier requirements.txt
    Returns:
    - bool: True si l'installation s'est déroulée avec succès, False sinon
    """
    try:
        subprocess.check_call(["python.exe", "-m", "pip", "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError as e:
        print("Python.exe introuvable !!!")
    try:
        subprocess.check_call(["pip", "install", "-r", fichier_requirements])
        print('[',datetime.now().time(),'] ', "Installation des dépendances réussie.")
        return True
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'installation des dépendances :", e)
        return False


def main(file_sql):
    with Pool() as pool:
            transport = pool.apply(recup_transport)
            site = pool.apply(recup_site)
            to_serve = pool.apply(recup_to_serve)
            athlete = pool.apply(recup_athlete)
            country = pool.apply(recup_country)
            discipline = pool.apply(recup_discipline)
            record = pool.apply(recup_record)
            event = pool.apply(recup_event)
            date_calendar = pool.apply(recup_date_calendar)
            is_from = pool.apply(recup_is_from, (athlete, country, ))
    data_to_json(transport, json + "transport.json")
    data_to_json(site, json + "site.json")
    data_to_json(to_serve, json + "to_serve.json")
    data_to_json(athlete, json + "athlete.json")
    data_to_json(country, json + "country.json")
    data_to_json(discipline, json + "discipline.json")
    data_to_json(record, json + "record.json")
    data_to_json(event, json + "event.json")
    data_to_json(date_calendar, json + "date_calendar.json")
    data_to_json(is_from, json + "is_from.json")
    liste_table = {
        "Transport": transport,
        "Site": site,
        "To_Serve": to_serve,
        "Athlete": athlete,
        "Country": country,
        "Discipline": record,
        "Event": event,
        "Date_calendar": date_calendar,
        "Is_from": is_from
    }
    data_to_json(liste_table, json + "liste_table.json")
    # On put les insert dans le fichier sql
    # On les envoie à la base de donnée si lien donnée
    oracleDB = (
        sql_transport_oracleDB(transport) + "\n\n" +
        sql_site_oracleDB(site) + "\n\n" +
        sql_country_oracleDB(country) + "\n\n" +
        sql_athlete_oracleDB(athlete) + "\n\n" +
        sql_discipline_oracleDB(discipline) + "\n\n" +
        sql_record_oracleDB(record, event, athlete) + "\n\n" +
        sql_date_calendar_oracleDB(date_calendar) + "\n\n" +
        sql_to_serve_oracleDB(to_serve, site) + "\n\n" +
        sql_event_oracleDB(event, discipline, record) + "\n\n" +
        sql_is_from_oracleDB(is_from)
    )
    with open(file_sql, "w", encoding="utf-8") as f:
        f.write(str(oracleDB))
    with open(PATH + "Script_SQL/INTERNETEURS_SCRIPT_CREATION_ORACLE_DATABASE.sql", "r", encoding="utf-8") as f:
        sql_creation = f.read()
    with open(PATH + "Script_SQL/INTERNETEURS_ORACLE_DATABASE.sql", 'w', encoding="utf-8") as fichier:
        fichier.write(sql_creation + "\n" + str(oracleDB))
    print('[',datetime.now().time(),'] ', "Création des données fini !!")
    # envoie à la base de donnée si compatible
    if len(ip_address) > 0:
        # Envoie à la base de donnée le script de création de bdd
        # Et insert les données trouvé
        connection = se_connecter_mysql(ip_address, user, password, bdd_name)
        execute_sql(connection, sql_creation)
        execute_sql(connection, str(oracleDB))
    return file_name

PATH = os.path.dirname(os.path.abspath(__file__)) + "/../" #repart du dossier racine du projet
json = PATH + "saved_json/" 
path_script_insert = PATH + "Script_SQL/INSERTION_TABLE_ORACLE_DATABASE.sql"
ip_address = ""
user = ""
password = ""
bdd_name = ""

if __name__ == "__main__":
    if installer_requirements(PATH + "Scraping/requirements.txt"):
        main(path_script_insert)