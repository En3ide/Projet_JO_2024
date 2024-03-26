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
        if os.path.exists(json+"event.json"):
            event = json_to_data(json+"event.json")
        else:
            event = pool.apply(recup_event)
        if os.path.exists(json+"date_calendar.json"):
            date_calendar = json_to_data(json+"date_calendar.json")
        else:
            date_calendar = pool.apply(recup_date_calendar)
        if os.path.exists(json + "is_from.json"):
            is_from = json_to_data(json + "is_from.json")
        else:
            is_from = pool.apply(recup_is_from, (athlete, country, ))
    data_to_json(transport, json + "transport.json")
    data_to_json(site, json + "site.json")
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
    data_to_json(liste_table, json + "liste_table.json")
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
        f.write(str(sql))
    with open("./BD/INTERNETEURS_SCRIPT_CREATION.sql", "r", encoding="utf-8") as f:
        sql_creation = f.read()
    with open("./BD/INTERNETEURS.sql", 'w', encoding="utf-8") as fichier:
        fichier.write(sql_creation + "\n" +str(sql))
    print('[',datetime.now().time(),'] ', "Création des données fini !!")
    return file_name


PATH = os.path.abspath(__file__)
json = PATH + "../saved_json/"
path_script_insert = PATH + "../BD/INSERTION_BDD.sql"

if __name__ == "__main__":
    if installer_requirements(PATH + "../Scraping/requirements.txt"):
        main(path_script_insert)