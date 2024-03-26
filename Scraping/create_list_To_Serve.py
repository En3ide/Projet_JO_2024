###################
# Script de scraping table Date_calendar
###################

##### Import #####
from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime
from create_list_Site import *
from get_id_table_selon_attr import *
from datetime import datetime

##### Code #####
main_url= "https://olympics.com/fr/paris-2024/sites"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def recup_url_transp():
    #print("test1")
    reponse = requests.get(main_url, headers=HEADERS)
    #print("test2")
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        result = []
        # Extraction du tableau
        ul = soup.find('ul', class_ = "content-list-grid")
        tab_site = ul.find_all('li')
        if tab_site != None:
            for site in tab_site:
                href = site.find('a').get('href')
                #print(href.split("/")[-1].replace("-", " "))
                if href != None:
                    #print(href)
                    #print(href.split("/")[-1])
                    #print(recup_transp(href))
                    if len(recup_transp(href)) >= 1:
                        result.append({"name_site": href.split("/")[-1].replace("-", " "), "transport": recup_transp(href)})
        print('[',datetime.now().time(),'] ', "Recup_To_serve Fini !!")
        return result
    else:
        #print(reponse.status_code)
        print('Fini !!!')
        return([])


def recup_transp(url):
    '''
    Récupère les ligne contenant les information d'un site
    Renvoie un tableau avec dict des valeur Nom station et Num ligne des site
    '''
    reponse = requests.get(url, headers=HEADERS)
    #print('test 2')
    result = []
    if reponse.status_code == 200:
        #print('test request reçu')
        soup = BeautifulSoup(reponse.text, 'html.parser')
        section = soup.find_all('section', class_='text-block')
        for sec in section:
            #print('test3\n'+sec.text)
            if 'INFORMATIONS SUR LES TRANSPORTS' in sec.text:
                if "li" in str(sec):
                    lis = sec.find_all('li')
                    if lis != []:
                        for li in lis:
                            result.extend(recup_info(li))
                secs = sec.find_all('p')
                for sec in secs:
                    result.extend(recup_info(sec))
    #print(result)
    return result


# Découpe les ligne "" << nom station >> (Num ligne 1, Num ligne 2, Num ligne 3, Num ligne 4) ""
# [{"name": "nom station", "number": ["Num ligne 1", "Num ligne 2", "Num ligne 3"]}]
def recup_info(sec):
    '''
    Découpe les ligne ""<< nom station >> (Num ligne 1, Num ligne 2, Num ligne 3, Num ligne 4) ""
    [{"name": "nom station", "number": ["Num ligne 1", "Num ligne 2", "Num ligne 3"]}]
    '''
    result = []
    temp = dict
    if "» (" in str(sec):
        #print("sec = "+sec.text)
        sec = sec.text
        #sec = sec.replace(sec[sec.find(") (")+2:sec.find(") (")+sec.find(")")], "")
        tmp = ""
        contient_donne = True
        while contient_donne == True:
            #print('test contient <<')
            if sec.find("» (") != -1:
                sec = sec.replace(sec[:-sec[::-1].find("«")-1], "")
                tmp = sec[sec.find("«")+2:sec.find("»")-1]
                tmp2 = sec[sec.find("» (")+3:sec.find(")")]
                if ", " in tmp2 or " et " in tmp2:
                    tmp2 = re.split(r',| et ', tmp2)
                    tmp2 = [element.strip() for element in tmp2 if element.strip()]
                else:
                    tmp2 = [tmp2]
                temp = {"name": tmp, "number": tmp2}
                result.append(temp)
                sec = sec.replace(sec[sec.find("«")+2:sec.find(")")-1], "")
            else:
                contient_donne = False
    return result


def dic_to_table(result):
    '''
    modifie le resulta de recup_url_transp pour créer en avance les entité de la table
    exemple "Stade Delcroix | station mérise | [RER C, RER D, RER M]"
    devient "Nom site       | id_transport   | num_ligne | nom_station"
            "Stade Delcroix | 1 | RER C | station mérise"
            "Stade Delcroix | 1 | RER D | station mérise"
            "Stade Delcroix | 1 | RER M | station mérise"
    '''
    tab = []
    for site in result:
        for station in site.get("transport"):
            for number in station.get("number"):
                if "RER" in number or "Train" in number:
                    trsp_type = 1
                elif "Tramway" in number:
                    trsp_type = 2
                elif "Bus" in number:
                    trsp_type = 3
                elif "Métro" in number or "Ligne" in number:
                    trsp_type = 4
                tab.append({"name_site": site.get("name_site"), "id_trans": trsp_type, "num_ligne": number, "station_name": station.get("name").replace("\u2019", "'").replace("\u2013", "-")})
    return tab

def get_id_site(table_dict, cle, valeur):
    '''
    Va tester la valeur de la clé avec toute les entré de table_dict
    lorsqu'il trouve une correspondance il revoie l'id du site concerné
    '''
    if table_dict is not None:
        valeur = valeur.lower()
        valeur = valeur.replace(" de ", " ")
        valeur = valeur.replace(" des ", " ")
        valeur = valeur.split(" ")
        #print("Valeur = " + str(valeur))
        for dic in table_dict:
            if dic != None:
                tmp1 = dic.get(cle).lower()
                tmp1 = tmp1.replace(" de ", " ")
                tmp1 = tmp1.replace(" des ", " ")
                temp = 0
                for val in valeur:
                    if val in str(tmp1):
                        #print("oui")
                        temp +=1
                if temp >= 2:
                    return table_dict.index(dic)+1
    return "NULL"

def recup_to_serve():
    return dic_to_table(recup_url_transp())

def send_to_serve(transport, site, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO To_Serve (id_site, id_trans, num_ligne, station_name) VALUES\n"
    for dic in transport:
        id = get_id_site(site, "name_site" ,dic.get("name_site"))
        send += (" (" + str(id) + ", " +
            str(dic.get("id_trans")) + ", '" +
            dic.get("num_ligne") + "', '" +
            dic.get("station_name").replace("'", "''") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql to_serve Fini !!!")
    return(send)

if __name__ == '__main__':
    pass