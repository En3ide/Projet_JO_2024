import ast

def get_id_site(table_dict, cle, valeur):
    if table_dict is not None:
        valeur = valeur.lower()
        if " de " in valeur:
            valeur = valeur.replace(" de ", " ")
        if " des " in valeur:
            valeur = valeur.replace(" des ", " ")
        valeur = valeur.split(" ")
        print("Valeur = " + str(valeur))
        for dic in table_dict:
            if dic != None:
                tmp1 = dic.get(cle).lower()
                if " de " in tmp1:
                    tmp1 = tmp1.replace(" de ", " ")
                if " des " in tmp1:
                    tmp1 = tmp1.replace(" des ", " ")
                temp = 0
                for val in valeur:
                    if val in str(tmp1):
                        print("oui")
                        temp +=1
                if temp >= 2:
                    return table_dict.index(dic)+1
    return None

import json
with open("test_site_tttt", "r") as f:
    data = json.load(f)
print(get_id_table(data,"name_site", "Château de Versaille"))

#print(data[0].get("name_site"))
# print(get_id_table("Site", name_site="Stade de Marseille"))