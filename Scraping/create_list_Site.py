from bs4 import BeautifulSoup
import requests, ast, sqlite3

url = 'https://fr.wikipedia.org/wiki/Jeux_olympiques_d%27%C3%A9t%C3%A9_de_2024'

def recup_site():
    reponse = requests.get(url)
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
                
                attr_name = tmp[0].text.replace("\n", "") + ' '+ tmp[1].text.replace("\n", "")
                attr_url = "https://fr.wikipedia.org/" + tmp[0].a['href']
                attr_capacity = tmp[3].text.replace('\xa0', '').replace("\n", "")
                attr_adress, attr_creation_date = attr_name, "" #recup_adress_creation_date(attr_name, attr_url)
                
                result.append({"name_site": attr_name, "adress_site": attr_adress, "creation_date_site": attr_creation_date, "capacity_site": attr_capacity, "URL_site": attr_url})
        return(result)
    else:
        print(reponse.status_code)
        return([])
    
def recup_adress_creation_date(nom, url):
    attr_adress, attr_creation_date = nom, ""
    
    reponse = requests.get(url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        table_info = soup.find('table', class_='infobox_v2 noarchive')
        # g eu flemme vsy c bon
        
    return attr_adress, attr_creation_date
        

def send_site(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Site_table (name_site, adress_site, creation_date_site, capacity_site, URL_site) VALUES\n"
    for dic in result:
        send += (" ('" + dic.get("name_site") + "', '" +
            dic.get("adress_site") + "', '" +
            dic.get("creation_date_site") + "', '" +
            dic.get("capacity_site") + "', '" +
            dic.get("URL_site") + "'),\n")
    send += send[:-2] + ";"

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