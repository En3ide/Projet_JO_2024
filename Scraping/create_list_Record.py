###################
# Script de scraping table Record
###################

##### Import #####
from bs4 import BeautifulSoup
import requests, sqlite3
import re
from date_convert import date_convert, convert_date

##### Code #####
main_url_athletisme = "https://fr.wikipedia.org/wiki/Records_olympiques_d%27athl%C3%A9tisme"
main_url_natation = "https://fr.wikipedia.org/wiki/Natation_aux_Jeux_olympiques"

def get_content_url(url):
    '''
    Permet de récupérer le contenue d'un URL
    param : (str) url
    return : Soup
    '''
    requete = requests.get(url) # Envoie une requete get a l'url
    # verifie si la requete a reussi
    if requete.status_code != 200 :
        return("La requete n'as pas aboutis")
    cont = requete.text # contenue brut de l'url, cad balise, script, commentaire
    soup = BeautifulSoup(cont,"html.parser") #contenue de l'url, cad uniquement html (balise)
    return soup

def contient_n_fois_c(chaine, sous_chaine, nbr):
    '''
    Renvoie True si la chaine de caractere chaine possede au moins nbr sous_chaine
    param : (str) chaine -> chaine de caractere , (str) sous_chaine -> sous chaine de caractere, (int) nbr -> nombre d'iteration
    return : Boolean 
    '''
    n = 0
    for char in chaine :
        if sous_chaine == char :
            n += 1
    return n >= nbr
    
def remove_progression_from_chaine(ch):
    '''
    Renvoie ch sans le mot "Progression"
    param : (str) ch -> chaine de caractere
    return : (str) ch
    '''
    index = ch.index('Progression')
    return ch[0:index]

def formatage_name_event_record(chaine):
    '''
    Renvoie la chaine formaté pour retirer les espaces avant "km" "m" et entre les chiffres
    param : (str) chaine -> chaine de caractere
    return : (str) chaine formaté
    '''
    return re.sub(r'(\d+)\s+(\S)', r'\1\2', chaine)

def formatage_stat_record(chaine):
    '''
    Renvoie la chaine formaté pour retirer les espaces entre les chiffres
    param : (str) chaine -> chaine de caractere
    return : (str) chaine formaté
    '''
    return re.sub(r'(?<=\d)\s(?=\d)', '', chaine).replace("\n", "")

def scraping_athletisme(soup):
    '''
    Retourne la liste de liste de althletisme 
    param : Objet BeautifulSoup soup
    return : list(list) liste
    '''
    liste = []
    name_sport = "Athlétisme"

    tables = soup.find_all("table")
    for i in range (0,3):
        for tr in tables[i].find_all('tr'):
            cells = tr.find_all('td')
            content = [cell.text for cell in cells]
            if len(content) > 0 and not contient_n_fois_c(content[1], " ", 3):
                content[0] = remove_progression_from_chaine(content[0]) 
                content.pop(-1)

                # Info dispo : [Discipline, Athlète, Pays, Perfomance, Date, Lieu]
                attr_stat_record = formatage_stat_record(content[3])
                attr_date_record = convert_date(content[4])
                attr_id_event = "NULL"
                attr_id_athlete = "NULL"
                nom_event = formatage_name_event_record(content[0])
                nom_athlete = content[1]

                liste.append({"stat_record" : attr_stat_record, "date_record" : attr_date_record, "id_event" : attr_id_event, 
                "id_athlete" : attr_id_athlete, "discipline" : name_sport , "event" : nom_event, "athlete" : nom_athlete})
    return liste

def scraping_natation(soup):
    '''
    Retourne la liste de dictionnaire de natation
    param : Objet BeautifulSoup soup
    return : list(dict) liste 
    '''
    liste = []
    name_sport = "Natation"

    tables = soup.find_all("table")
    for i in range(7, 10) :
        for tr in tables[i].find_all('tr'):
            cells = tr.find_all('td')
            content = [cell.text.replace("\n","") for cell in cells]
            if len(content) > 0 and not contient_n_fois_c(content[2], " ", 3):
                content.pop(-1)

                # Info dispo : [Discipline, Temps, Athlète, Nationalité, Date, Lieu, Information]
                attr_stat_record = formatage_stat_record(content[1])
                attr_date_record = convert_date(content[4])
                attr_id_event = "NULL"
                attr_id_athlete = "NULL"
                nom_event = formatage_name_event_record(content[0])
                nom_athlete = content[2]

                liste.append({"stat_record" : attr_stat_record, "date_record" : attr_date_record, "id_event" : attr_id_event, 
                "id_athlete" : attr_id_athlete, "discipline" : name_sport , "event" : nom_event, "athlete" : nom_athlete})
    return liste

def recup_record():
    # Scraping pour athlétisme
    soup = get_content_url(main_url_athletisme)
    liste = scraping_athletisme(soup)

    # Scraping pour natation
    soup = get_content_url(main_url_natation)
    liste += scraping_natation(soup)

    return liste

def send_record(result, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO Record_table (stat_record, date_record, id_event, id_athlete) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("stat_record") + "', '" +
            dic.get("date_record") + "', '" +
            dic.get("id_event") + "', " +
            dic.get("id_athlete") + "'),\n")
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
    return send_record(recup_record())

if __name__ == "__main__":
    send_record(recup_record())