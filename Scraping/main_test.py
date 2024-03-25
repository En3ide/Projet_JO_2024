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
        subprocess.check_call(["pip", "install", "-r", fichier_requirements])
        print('[',datetime.now().time(),'] ', "Installation des dépendances réussie.")
        return True
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'installation des dépendances :", e)
        return False

def main(file_sql):
    with Pool() as pool:
        if os.path.exists(json+"transport.json"):
            transport = json_to_data(json+"transport.json")
        else:
            transport = pool.apply(recup_transport)
        if os.path.exists(json+"site.json"):
            site = json_to_data(json+"site.json")
        else:
            site = pool.apply(recup_site)
        if os.path.exists(json+"transport.json"):
            to_serve = json_to_data(json+"to_serve.json")
        else:
            to_serve = pool.apply(recup_to_serve)
        if os.path.exists(json+"transport.json"):
            athlete = json_to_data(json+"athlete.json")
        else:
            athlete = pool.apply(recup_athlete)
        if os.path.exists(json+"country.json"):
            country = json_to_data(json+"country.json")
        else:
            country = pool.apply(recup_country)
        if os.path.exists(json+"discipline.json"):
            discipline = json_to_data(json+"discipline.json")
        else:
            discipline = pool.apply(recup_discipline)
        if os.path.exists(json+"record.json"):
            record = json_to_data(json+"record.json")
        else:
            record = pool.apply(recup_record)
        """if os.path.exists(json+"event.json"):
            event = json_to_data(json+"event.json")
        else:
            event = pool.apply(recup_event)"""
        if os.path.exists(json+"date_calendar.json"):
            date_calendar = json_to_data(json+"date_calendar.json")
        else:
            date_calendar = pool.apply(recup_date_calendar)
    data_to_json(transport, json + "transport.json")
    data_to_json(site, json + "tite.json")
    data_to_json(to_serve, json + "to_serve.json")
    data_to_json(athlete, json + "athlete.json")
    data_to_json(country, json + "country.json")
    data_to_json(discipline, json + "discipline.json")
    data_to_json(record, json + "record.json")
    data_to_json(date_calendar, json + "date_calendar.json")
    # On put les insert dans le fichier sql
    sql = (
        send_transport(transport) + "\n" +
        send_site(site) + "\n" +
        send_to_serve(to_serve, site) + "\n" +
        send_athlete(athlete) + "\n" +
        send_country(country) + "\n" +
        send_discipline(discipline) + "\n" +
        send_record(record) + "\n" +
        #send_event(event) + "\n" +
        send_date_calendar(date_calendar)
    )
    with open(file_sql, "w", encoding="utf-8") as f:
        f.write(sql)
    print('[',datetime.now().time(),'] ', "Création des données fini !!")
    return file_name


json = "./saved_json/"

if __name__ == "__main__":
    if installer_requirements("./Scraping/requirements.txt"):
        main("./BD/INSERTION_BDD.sql")