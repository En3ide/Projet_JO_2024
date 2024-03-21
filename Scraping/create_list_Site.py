from bs4 import BeautifulSoup
import requests, ast, sqlite3

def recup_adress_creation_date(nom, url):
    attr_adress, attr_creation_date = nom, ""
    
    reponse = requests.get(url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        table_info = soup.find('table', class_='infobox_v2 noarchive')
        # g eu flemme vsy c bon
        
    return attr_adress, attr_creation_date
        

def recup_site():
    # Renvoie un tableau [Date, Adress, Capacité, URL du site]
    url = 'https://fr.wikipedia.org/wiki/Jeux_olympiques_d%27%C3%A9t%C3%A9_de_2024'
    reponse = requests.get(url)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Exemple : Extraire le tableau
        tab = soup.find_all('table', class_=['wikitable','sortable','jquery-tablesorter'])

        result = []
        tmp = []
        for tr in tab[3].find_all('tr'):
            cells = tr.find_all('td')
            if len(cells) > 3:
                tmp = [cell for cell in cells]
                
                attr_name = tmp[0].text.replace("\n", "")+' '+tmp[1].text.replace("\n", "")
                attr_url = "https://fr.wikipedia.org/"+tmp[0].a['href']
                attr_capacity = tmp[3].text.replace('\xa0', '').replace("\n", "")
                attr_adress, attr_creation_date = recup_adress_creation_date(attr_name, attr_url)
                
                result.append({"name_site": attr_name, "adress_site": attr_adress, "creation_date_site": attr_creation_date, "capacity": attr_capacity, "URL_site": attr_url})
        return(result)
    else:
        print("Echec de la request, code retour [ "+ reponse.status_code +" ]")
        return([])

# obsolète un peu
def send_site(result, bdd=""):
    send = ""
    for i in result:
        send += "INSERT INTO Site (Creation_date, Adress, Capacity, URL_site) VALUES ('"+i[0]+"', '"+ i[1] +"', "+ i[2] +", '"+i[3]+"');"
    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.close()
        curseur.execute(send)
        connexion.close()
        connexion.commit()
    return(send)

print(recup_site())