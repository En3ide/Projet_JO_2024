###################
# Script de scraping table Date_calendar
###################

##### Import #####
from datetime import datetime, timedelta
import requests, sqlite3
from bs4 import BeautifulSoup
import html2text, re

##### Code #####
def get_calendar_url():
    main_url = "https://www.paris2024.org/fr/calendrier-sports-olympiques/"
    search_url = "calendrier-sports-olympique"

    # Récupérer le contenu de la page web
    response = requests.get(main_url)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tag = [a for a in soup.find_all('a', href=True) if search_url in a.get('href')]

        # Vérifier si la balise <a> a été trouvée
        if a_tag is not []:
            # Récupérer l'URL (href)
            return a_tag[0].get('href')
        else:
            print("Balise <a> non trouvée.")
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")

def create_list_day_medal():
    # Récupérer le contenu de la page web
    response = requests.get(get_calendar_url())

    rep = []
    
    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Configurez html2text pour ne pas ajouter de nouvelles lignes après chaque balise
        h = html2text.HTML2Text()
        h.body_width = 0  # Désactiver la coupe de texte
        h.single_line_break = True  # Utiliser une seule ligne pour les sauts de ligne

        # Convertir le HTML en texte brut avec la mise en forme
        text_content = h.handle(response.text)
        text_content = text_content.replace("l", "")

        list_text_content = text_content.split("\n")[1:-1]

        for ligne in list_text_content:
            #cas "cette sessions"
            if "cette session" in ligne:
                liste_chiffres = re.findall(r'\d+', ligne)
            #case "toutes les sessions"
            elif "toutes les sessions" in ligne:
                tmp_list = re.findall(r'\d+', ligne)
                liste_chiffres = []
                if len(tmp_list[1]) == 1:
                    tmp_list[1] = "0" + tmp_list[1]
                day_start, day_end = int(tmp_list[0]), int(tmp_list[1])

                if day_start >= 26 and day_start <= 31:
                    day_start = "2024-07-" + str(day_start)
                else:
                    day_start = "2024-08-" + str(day_start)
                if day_end >= 26 and day_end <= 31:
                    day_end = "2024-07-" + str(day_end)
                else:
                    day_end = "2024-08-" + str(day_end)

                day_start = datetime.strptime(day_start, "%Y-%m-%d")
                day_end = datetime.strptime(day_end, "%Y-%m-%d")

                while day_start <= day_end:
                    liste_chiffres.append(day_start.strftime("%d"))
                    day_start += timedelta(days=1)

            # cas "chiffres listé"
            else:
                liste_chiffres = re.findall(r'\d+', ligne[ligne.index("session"):])

            for chiffre in liste_chiffres:
                tmp_chiffre = chiffre
                if len(chiffre) == 1:
                    tmp_chiffre = "0" + chiffre
                if tmp_chiffre not in rep:
                    rep.append(tmp_chiffre)
    return rep

def recup_date_calendar():
    # Date de début et de fin
    start_date = datetime(2024, 7, 26)
    end_date = datetime(2024, 8, 11)

    # Initialiser la liste de dictionnaires
    date_list = []

    # Remplir la liste de dictionnaires avec des dates
    current_date = start_date
    list_day_medal = create_list_day_medal()

    while current_date <= end_date:
        attr_date_cal = current_date.strftime("%Y-%m-%d")
        attr_medal_cer = str(current_date.strftime("%d") in list_day_medal)
        date_list.append({"date_cal": attr_date_cal, "medal_ceremony_date_cal": attr_medal_cer})
        current_date += timedelta(days=1)
    print('[',datetime.now().time(),'] ', "Recup date_calendar fini !!!")
    return date_list


def send_date_calendar(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT IGNORE INTO Date_calendar (date_cal, medal_ceremony_date_cal) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("date_cal") + "', " +
            dic.get("medal_ceremony_date_cal") + "),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql Date_calendar fini !!!")
    return(send)

def sql_date_calendar_oracleDB(result):
    # Création de la requête SQL
    send = "INSERT ALL\n"
    for dic in result:
        send += ("INTO date_calendar (date_cal, medal_ceremony_date_cal) VALUES ('" +
            dic.get("date_cal").replace("'", "''") + "', '" +
            dic.get("medal_ceremony_date_cal") + "')\n")
    send = send[:-1] + ";"
    return(send)

if __name__ == "__main__":
    pass