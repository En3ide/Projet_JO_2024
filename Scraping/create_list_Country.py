from bs4 import BeautifulSoup
import requests, ast, sqlite3

def recup_code_pays():
    # Renvoie un tableau [Num, Alpha-3, Alpha-2, Nom Français]
    url = 'https://fr.wikipedia.org/wiki/ISO_3166-1'
    reponse = requests.get(url)
    if reponse.status_code == 200:
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
                
                attr_code_country = tmp[1]
                attr_name_contry = tmp[4].replace("\n", "")
                
                #result.append([tmp[0], tmp[1], tmp[2], tmp[4].replace("\n", "")])
                result.append({"code_country": attr_code_country, "name_country": attr_name_contry})

        return(result)
    else:
        print(reponse.status_code)
        return([])

#obsolète un peu
def send_country_code(result, bdd=""):
    send = "INSERT INTO Country_table (code_country, name_country) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("code_country") + "', '" +
            dic.get("name_country") + "'),\n")
    send += send[:-2] + ";"
    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    return(send)

print(send_country_code(recup_code_pays()))