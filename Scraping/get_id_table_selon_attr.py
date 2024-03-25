###################
# Script de avoir l'id d'une table selon ses attributs
###################

##### Import #####
from create_list_Site import *
from create_list_Date_calendar import *
from create_list_Athlete import *
from create_list_Discipline import *
import json

##### Code #####

def get_id_table(nom_table, **kwargs):
    '''
    Retourne l'id de l'élément de la table nom_table avec kwargs (cle:valeur) comme attribut
    str, cle:valeur -> int
    ex: print(get_id_table("Site", name_site="Arena Paris Nord"))
    '''
    table_dict = None

    if nom_table == "Site":
        table_dict = recup_site()
    if nom_table == "Date_calendar":
        table_dict = recup_date_calendar()
    if nom_table == "Athlete":
        table_dict = recup_athlete()
    
    if table_dict is not None:

        for i, dict in enumerate(table_dict):
            find = True
            for cle, valeur in kwargs.items():
                if not valeur in dict.get(cle):
                    find = False
                    break
            if find:
                return i
    return None

def get_dic_id_table(liste_dic, **kwargs):
    '''
    '''
    for index, element in enumerate(liste_dic):
        match = True
        for cle, valeur in kwargs.items():
            if cle not in element or element[cle] != valeur:
                match = False
                break
        if match:
            return str(index)
    return "NULL"

def data_to_json(data, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_name

def json_to_data(data, file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    print(get_id_table("Site", name_site="Arena Paris Nord"))