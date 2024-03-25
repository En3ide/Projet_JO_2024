from multiprocessing import Process, Queue, Pool, subprocess
from create_list_Transport import *
from create_list_Site import *
from create_list_Athlete import *
from create_list_Country import *
from create_list_Discipline import *
from create_list_Record import *
from create_list_To_Serve import *
from create_list_Event import *
from create_list_Date_calendar import * 

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
        print("Installation des dépendances réussie.")
        return True
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'installation des dépendances :", e)
        return False

if __name__ == "__main__":
    installer_requirements("requirements.txt")
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
        
    sql_transport = send_transport(transport)
    sql_site = send_site(site)
    sql_to_serve = send_to_serve(to_serve, site)
    sql_athlete = send_athlete(athlete)
    sql_country = send_country(country)
    sql_discipline = send_discipline(discipline)
    sql_record = send_record(record)
    sql_event = send_event(event)
    sql_date_calendar = send_date_calendar(date_calendar)