from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime
from date_convert import date_convert, convert_date

main_url = 'https://fr.wikipedia.org/wiki/Jeux_olympiques_d%27%C3%A9t%C3%A9_de_2024'

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
                if donnee[0] != None:
                    attr_adress = donnee[0]
                else:
                    attr_adress = attr_name
                attr_creation_date = convert_date(donnee[1])
             
                result.append({"name_site": attr_name, "adress_site": attr_adress, "creation_date_site": attr_creation_date, "capacity_site": attr_capacity, "URL_site": attr_url})
        return(result)
    else:
        print(reponse.status_code)
        return([])
    
def send_site(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Site_table (name_site, adress_site, creation_date_site, capacity_site, URL_site) VALUES\n"
    for dic in result:
        send += (" ('" + dic.get("name_site") + "', '" +
            dic.get("adress_site") + "', '" +
            dic.get("creation_date_site") + "', " +
            dic.get("capacity_site") + ", '" +
            dic.get("URL_site") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    return(send)

if __name__ == "__main__":
    print(send_site(recup_site()))