###################
# Script de scraping table Country
###################

##### Import #####
from bs4 import BeautifulSoup
from utilitary_function import *
import requests, ast, sqlite3

##### Code #####
main_url = 'https://fr.wikipedia.org/wiki/ISO_3166-1'

def recup_country():
    # Info du tableau (tmp) [Num, Alpha-3, Alpha-2, Code subdivisions, Nom Français, NOM ISO, Nom langue originale, Indépendant]

    reponse = requests.get(main_url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Exemple : Extraire le tableau
        tab = soup.find('table', class_=['wikitable', 'sortable', 'jquery-tablesorter'])

        result = []
        tmp = []
        for tr in tab.find_all('tr'):
            cells = tr.find_all('td')
            content = [cell.text for cell in cells]
            tmp = ast.literal_eval(str(content))
            if len(tmp) > 0:
                
                attr_code_country = tmp[1]
                attr_name_contry = tmp[4].replace("\n", "")[1:]
                
                result.append({"code_country": attr_code_country, "name_country": attr_name_contry})
        print('[',datetime.now().time(),'] ', "Recup_country Fini !!!")
        return(result)
    else:
        print(reponse.status_code)
        return([])


def send_country(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT IGNORE INTO Country (code_country, name_country) VALUES\n"
    for dic in result:
        code_country = dic.get("code_country").replace("'", "''")
        name_country = dic.get("name_country").replace("'", "''")
        send += ("('" + code_country + "', '" +
            name_country + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql country Fini !!!")
    return(send)

def sql_country_oracleDB(result):
    # Création de la requête SQL
    send = "INSERT ALL\n"
    for dic in result:
        send += ("INTO Country (code_country, name_country) VALUES ('" +
            dic.get("code_country").replace("'", "''") + "', '" +
            dic.get("name_country") + "')\n")
    send = send[:-1] + ";"
    return(send)

if __name__ == "__main__":
    #print(send_country(recup_country()))
    pass