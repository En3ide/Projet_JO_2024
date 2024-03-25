import requests, sqlite3
from bs4 import BeautifulSoup

ASSO_SPORTS_O = [(0,36), (1,0), (2,2), (3,3), (4,4), (5,5), (6,7), (7,6), (8,9), (9,8), (10,12), (11,10), (12,11), (13,31), (14,13), (15,14), (16,15)\
               , (17,16), (18,17), (19,18), (20,20), (21,21), (22,22), (23,24), (24,1), (25,25), (26,38), (27,35), (28,34), (29,32), (30,32), (31,37),\
                 (32,39), (33,40), (34,29), (35,28), (36,27), (37,26), (38,30), (39,19), (40,23), (41,41), (42,42), (43,43), (44,44)]

ASSO_SPORTS_P = [(0,2), (1,1), (2,4), (3,17), (4,5), (5,7), (6,8), (7,9), (8,10), (9,11), (10,13), (11,12), (12,6), (13,14), (14,16), (15,15), (16,19), (17,18)\
                 , (18,22), (19,0), (20,3), (21,20), (22,21)]

def obtenir_sports_olympiques_fr():
    sports_olympiques = []
    # Récupération des sports des Jeux Olympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/fr/sports-olympiques/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Les sports se trouvent dans le 4 et 6 div de cette classe
        targeted_div = [divs[3], divs[5]]
        for div in targeted_div:
            # Trouver tous les tags 'a' à l'intérieur du div de cette classe
            noms_sports = div.find_all('a')
            for sport in noms_sports:
                sports_olympiques.append(sport.text.strip())
    return sports_olympiques

def obtenir_sports_paralympiques_fr():
    sports_paralympiques = []
    # Récupération des sports des Jeux Paralympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/fr/sports-paralympiques/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Supposant que les sports se trouvent dans le troisieme div
        for div in divs[2]:
            # Trouver tous les tags 'a' à l'intérieur du div
            noms_sports = div.find_all('a')
            for sport in noms_sports:
                #Le site  à une légère erreur que je corrige ici
                if sport.text.strip() != "powerlifting":
                    sports_paralympiques.append(sport.text.strip())
                else :
                    sports_paralympiques.pop()
                    sports_paralympiques.append("para powerlifting")
                
    return sports_paralympiques

def obtenir_sports_olympiques_en():
    sports_olympiques = []
    # Récupération des sports des Jeux Olympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/en/olympic-sports/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Les sports se trouvent dans le 4 et 6 div de cette classe
        targeted_div = [divs[1], divs[3]]
        for div in targeted_div:
            # Trouver tous les tags 'a' à l'intérieur du div de cette classe
            noms_sports = div.find_all('a')
            for sport in noms_sports:
                #Le site  à une légère erreur que je corrige ici
                if sport.text.strip() != "ountain bike":
                    sports_olympiques.append(sport.text.strip())
                else :
                    sports_olympiques.pop()
                    sports_olympiques.append("mountain bike")
                
    return sports_olympiques

def obtenir_sports_paralympiques_en():
    sports_paralympiques = []
    # Récupération des sports des Jeux Paralympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/en/paralympic-sports/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Les sports se trouvent dans le troisieme div
        for div in divs[2]:
            # Trouver tous les tags 'a' à l'intérieur du div
            noms_sports = div.find_all('a')
            for sport in noms_sports:
                sports_paralympiques.append(sport.text.strip())
                
    return sports_paralympiques

def associate_sports(l_en, l_fr, association):
    res = []
    for sport in association:
        res.append((l_en[sport[0]],l_fr[sport[1]]))
    return res

def get_table_disciplines(l_en, l_fr, association, cat = "P"):
    res = []
    if cat == "O":
        cate = "Olympic"
    else:
        cate = "Paralympic"
    l_sports = associate_sports(l_en, l_fr, association)
    for sport in l_sports:
        res.append({'name_fr_disc':sport[1].lower(), 'name_an_disc':sport[0].lower(), 'category_disc':cate})
    return res

def recup_discipline():
    sports_olympiques_en = obtenir_sports_olympiques_en()
    sports_olympiques_fr = obtenir_sports_olympiques_fr()
    sports_paralympiques_en = obtenir_sports_paralympiques_en()
    sports_paralympiques_fr = obtenir_sports_paralympiques_fr()
    table_O = get_table_disciplines(sports_olympiques_en,sports_olympiques_fr, ASSO_SPORTS_O,"O")
    table_P = get_table_disciplines(sports_paralympiques_en, sports_paralympiques_fr, ASSO_SPORTS_P)
    
    table = table_O + table_P
    
    return table

def send_discipline(result, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO Discipline (name_fr_disc, name_an_disc, category_disc) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("name_fr_disc") + "', '" +
            dic.get("name_an_disc") + "', '" +
            dic.get("category_disc") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    return(send)

def create_sql():
    return send_discipline(recup_discipline())

if __name__ == "__main__":
    send_discipline(recup_discipline())
    