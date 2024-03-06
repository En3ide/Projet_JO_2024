from bs4 import BeautifulSoup
import requests, ast, sqlite3

def recup_code_pays():
    # Renvoie un tableau [Num, Alpha-3, Alpha-2, Nom Français]
    url = 'https://fr.wikipedia.org/wiki/ISO_3166-1'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')

    # Exemple : Extraire le tableau
    tab = soup.find('table', class_=['wikitable','sortable','jquery-tablesorter'])

    result = []
    tmp = []
    for tr in tab.find_all('tr'):
        cells = tr.find_all('td')
        content = [cell.text for cell in cells]
        tmp = ast.literal_eval(str(content))
        if len(tmp) > 0:
            result.append([tmp[0], tmp[1], tmp[2], tmp[4].replace("\n", "")])

    print(result[0])
    return(result)

def send_country_code(result, bdd=""):
    send = ""
    for i in result:
        send += "INSERT INTO Country ( Country_code, Country_name) VALUES ('" + i[1] + "', '" + i[3] + "');"
    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.close()
        curseur.execute(send)
        connexion.close()
        connexion.commit()
    return(send)

print(send_country_code(recup_code_pays()))