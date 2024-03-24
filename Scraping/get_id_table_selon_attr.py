###################
# Script de avoir l'id d'une table selon ses attributs
###################

##### Import #####
from create_list_Site import *
from create_list_Date_calendar import *

##### Code #####

def get_id_table(nom_table, **kwargs):
    table_dict = None

    if nom_table == "Site":
        table_dict = recup_site()
    if nom_table == "Date_calendar":
        table_dict = recup_date_calendar()
    
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


if __name__ == "__main__":
    #print(get_id("Site", name_site="Arena Paris Nord"))
    pass