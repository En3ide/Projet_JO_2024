from multiprocessing import process, Queue, Pool
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
import os, subprocess

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
    data_to_json(site, json + "tite.json")
    data_to_json(to_serve, json + "to_serve.json")
    data_to_json(athlete, json + "athlete.json")
    data_to_json(country, json + "country.json")
    data_to_json(discipline, json + "discipline.json")
    data_to_json(record, json + "record.json")
    data_to_json(date_calendar, json + "date_calendar.json")
    data_to_json(is_from, json + "is_from.json")
    liste_table = {
        "Transport": transport,
        "Site": site,
        "To_Serve": to_serve,
        "Athlete": athlete,
        "Country": country,
        "Discipline": record,
        "Date_calendar": date_calendar,
        "Is_from": is_from
    }
    with open(json+ "liste_table.json", "w", encoding="utf-8") as f:
        f.write(liste_table)
    # On put les insert dans le fichier sql
    sql = (
        send_transport(transport) + "\n\n" +
        send_site(site) + "\n\n" +
        send_athlete(athlete) + "\n\n" +
        send_country(country) + "\n\n" +
        send_discipline(discipline) + "\n\n" +
        send_record(record, event, athlete) + "\n\n" +
        send_date_calendar(date_calendar)+ "\n\n" +
        send_to_serve(to_serve, site) + "\n\n" +
        send_event(event, discipline, record) + "\n" +
        send_is_from(is_from)
    )
    with open(file_sql, "w", encoding="utf-8") as f:
        f.write(sql)
    print('[',datetime.now().time(),'] ', "Création des données fini !!")
    return file_name


json = "./saved_json/"

if __name__ == "__main__":
    if installer_requirements("./Scraping/requirements.txt"):
        main("./BD/INSERTION_BDD.sql")