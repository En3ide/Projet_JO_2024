###################
# Script de avoir l'id d'une table selon ses attributs
###################

##### Import #####
from create_list_Site import *
from create_list_Date_calendar import *
from create_list_Athlete import *
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

        for dict in table_dict:
            find = True
            for cle, valeur in kwargs.items():
                if not valeur in dict.get(cle):
                    find = False
                    break
            if find:
                return table_dict.index(dict)+1
    return None

def get_id_athlete(*args):
    '''
    Renvoie un dictionnaire nom_athlete:id d'athlètes
    str -> id / [str, str] -> id
    ex :
    get_id_athlete("Usain Bolt", "Elaine Thompson-Herah", "Bob Beamon")
    get_id_athlete(["Usain Bolt", "1986-08-21"], ["Elaine Thompson-Herah", "1992-06-28"], ["Bob Beamon", "1946-08-29"])
    '''
    rep = {}
    if isinstance(args[0], str):
        for nom_athlete in args:
            split_name = nom_athlete.split(' ')
            rep[nom_athlete] = get_id_table("Athlete", firstname_athlete=split_name[0], name_athlete=split_name[1])
    else:
        for list in args:
            split_name = list[0].split(' ')
            birth = list[1]
            rep[list[0]] = get_id_table("Athlete", firstname_athlete=split_name[0], name_athlete=split_name[1], birthday_athlete=birth)
    return rep


def data_to_json(data, file_name):
    with open(file_name, "w") as f:
        json.dump(data, f)
    return file_name

def json_to_data(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    print(get_id_table("Site", name_site="Arena Paris Nord"))