###################
# Script de scraping table Date_calendar
###################

##### Import #####
from get_id_table_selon_attr import *
from bs4 import BeautifulSoup
import requests, sqlite3
from date_convert import date_convert, convert_date
from datetime import datetime

##### Code #####
main_url = 'https://fr.wikipedia.org/wiki/Jeux_olympiques_d%27%C3%A9t%C3%A9_de_2024'
file_name = "site.json"

def recup_date_adress(url):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        return collect_adress(soup), collect_date(soup)
        
def collect_adress(n):
    table_info = n.find('tbody')
    if "Adresse" in str(table_info):
        for tr in table_info.find_all("tr"):
            if "Adresse" in str(tr):
                td = tr.find_all("td")
                return [t for t in td ][0].text.replace("\n", "")
    return

def collect_date(n):
    tbody = n.find_all('tbody')
    for i in tbody:
        if "Création" in str(i):
            for tr in i.find_all("tr"):
                if "Création" in str(tr):
                    td = tr.find_all("td")
                    return [t for t in td][0].text.replace("\n", "")
    for i in tbody:
        if "Début de construction" in str(i):
            for tr in i.find_all("tr"):
                if "Début de construction" in str(tr):
                    td = tr.find_all("td")
                    return [t for t in td][0].text.replace("\n", "")
    for i in tbody:
        if "Ouverture" in str(i):
            for tr in i.find_all("tr"):
                if "Ouverture" in str(tr):
                    td = tr.find_all("td")
                    return [t for t in td][0].text.replace("\n", "")
    return

def recup_site():
    reponse = requests.get(main_url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Extraction du tableau
        tab = soup.find_all('table', class_=['wikitable','sortable','jquery-tablesorter'])

        result = []
        tmp = []
        for tr in tab[3].find_all('tr'):
            cells = tr.find_all('td')
            if len(cells) > 3:
                tmp = [cell for cell in cells]
                
                attr_name = tmp[0].text.replace("\n", "") # + ' '+ tmp[1].text.replace("\n", "")
                attr_url = "https://fr.wikipedia.org/" + tmp[0].a['href']
                attr_capacity = tmp[3].text.replace('\xa0', '').replace("\n", "")
                if attr_capacity in " -":
                    attr_capacity = "NULL"
                donnee = recup_date_adress(attr_url)
                if donnee[0] is not None:
                    attr_adress = donnee[0]
                else:
                    attr_adress = attr_name
                attr_creation_date = convert_date(donnee[1])
             
                result.append({"name_site": attr_name.replace("\u00a0", " "), "adress_site": attr_adress.replace("\u00a0", " "), "creation_date_site": attr_creation_date, "capacity_site": attr_capacity, "URL_site": attr_url})
        print('[',datetime.now().time(),'] ', "Recup_site Fini !!!")
        return(result)
    else:
        print(reponse.status_code)
        return([])
    
def send_site(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Site (name_site, adress_site, creation_date_site, capacity_site, URL_site) VALUES\n"
    for dic in result:
        date_is_null = dic.get("creation_date_site") == "NULL"
        send += (" ('" + dic.get("name_site").replace("'", "''") + "', '" +
            dic.get("adress_site").replace("'", "''"))
        if date_is_null:
            send += "', "
        else:
            send += "', '"
        send += dic.get("creation_date_site").replace("'", "''")
        if date_is_null:
            send += ", "
        else:
            send += "', "

        send += (dic.get("capacity_site").replace("'", "''") + ", '" +
            dic.get("URL_site").replace("'", "''") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql Site Fini !!!")
    return(send)

def create_sql():
    return send_site(recup_site())

if __name__ == "__main__":
    send_site(recup_site())