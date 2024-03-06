from bs4 import BeautifulSoup
import requests, ast, sqlite3

def recup_site():
    # Renvoie un tableau [Num, Alpha-3, Alpha-2, Nom Français]
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
            #tmp = ast.literal_eval(str(content))# Site commune status capacité Sport_olympic
            # print(str(tmp)+"   1")
                #print(tmp)
                result.append(["00-00-00",tmp[0].text.replace("\n", "")+' '+tmp[1].text.replace("\n", ""),tmp[3].text.replace('\xa0', '').replace("\n", ""), "https://fr.wikipedia.org/"+tmp[0].a['href']])# Creation_date Address capacity URL
        return(result)
    else:
        print("Echec de la request, code retour [ "+ reponse.status_code +" ]")
        return([])

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

print(send_site(recup_site()))