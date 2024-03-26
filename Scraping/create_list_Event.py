###################
# Script de scraping table Event
###################

##### Import #####
import requests, sqlite3
from bs4 import BeautifulSoup
from create_list_Discipline import *
from create_list_Record import *
from get_id_table_selon_attr import *

MOT_EQUIPE = ["équipes", "équipe", "Equipe", "relais", "Relais", "Double", "double", "football", "ensembles", "handball", "hockey", "Duo", "duos", "synchronisé", "water-polo", "volleyball", "rugby", "Deux", "Quatre"]

def obtenir_pages_sports_olympiques_fr():
    pages_sports_olympiques = []
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
            liens_sports = div.find_all('a')
            # Récupération de l'attribut href de la balise.
            for liens in liens_sports:
                if 'href' in liens.attrs:
                    pages_sports_olympiques.append(liens['href'])
    return pages_sports_olympiques

def obtenir_pages_sports_paralympiques_fr():
    pages_sports_paralympiques = []
    # Récupération des sports des Jeux Paralympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/fr/sports-paralympiques/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Supposant que les sports se trouvent dans le troisieme div
        for div in divs[2]:
            # Trouver tous les tags 'a' à l'intérieur du div
            liens_sports = div.find_all('a')
            for liens in liens_sports:
                if 'href' in liens.attrs:
                    pages_sports_paralympiques.append(liens['href'])
                if liens.text.strip() == "powerlifting":
                    pages_sports_paralympiques.pop()
    
    return pages_sports_paralympiques

def obtenir_epreuves(url):
    epreuves = []
    # Récupération de la page de sport
    réponse = requests.get(url)
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        title_sport = soup.find_all('h1')[0].text.strip()
        epreuves.append(title_sport)
        
        divs = soup.find_all('div','block-classic-editor')
        l_li = []
    for i in range (len(divs)):
        h2 = divs[i].find_all('h2')
        
        if h2 != [] and (h2[0].text.strip() == "Epreuves en 2024" or h2[0].text.strip() == "Epreuve en 2024"):
            #J'ai remarqué une configuration générale pour la plupart des pages de sports, mais voici les corrections pour certaines pages.
            #En boxe les catégories de poids ont pas encore été défini
            if title_sport == "Canoë sprint" or title_sport == "Canoë-kayak slalom":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                return epreuves
            
            #Obligée de le faire manuellement celui ci
            elif title_sport == "Cyclisme sur route":
                epreuves.append("Epreuves contre la montre (femmes/hommes)")
                epreuves.append("Epreuves en ligne (femmes/hommes)")
                return epreuves
            
            elif title_sport == "Gymnastique artistique":
                l_li = divs[i+3].find_all('li')
                for li in range(0,4):
                    epreuves.append(f"{l_li[li].text.strip()} (femmes/hommes)")
                for li in range(4,len(l_li)):
                    epreuves.append(f"{l_li[li].text.strip()} (femmes)")
                    
                l_li = divs[i+5].find_all('li')
                for li in range(4,len(l_li)):
                    epreuves.append(f"{l_li[li].text.strip()} (hommes)")
                return epreuves
            
            elif title_sport == "Haltérophilie":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    epreuves.append(f"{li.text.strip()} (femmes)")
                l_li = divs[i+5].find_all('li')
                for li in l_li:
                    epreuves.append(f"{li.text.strip()} (hommes)")
                return  epreuves
            
            elif title_sport == "Judo":
                l_li = divs[i+2].find_all('li')
                
                for li in range(len(l_li)-1):
                    l_li[li] = l_li[li].text.split()
                    deca = 0
                    for elt in range(len(l_li[li])):
                        if l_li[li][0][0] != '-' and l_li[li][0][0] != '+':
                            del l_li[li][elt-deca]
                            deca += 1
                for epr in l_li[0]:
                    epreuves.append(f"Tournois {epr[0:-1]} individuel (femmes)")
                for epr in l_li[1]:
                    epreuves.append(f"Tournois {epr[0:-1]} individuel (hommes)")
                epreuves.append("Tournois par équipes (mixtes)")
                return epreuves
            
            elif title_sport == "Lutte":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    epreuves.append(f"Lutte libre {li.text.strip()} (femmes)")
                l_li = divs[i+5].find_all('li')
                for li in l_li:
                    epreuves.append(f"Lutte libre {li.text.strip()} (hommes)")
                l_li = divs[i+7].find_all('li')
                for li in l_li:
                    epreuves.append(f"Lutte gréco-romaine {li.text.strip()} (femmes)")
                return  epreuves
            
            elif title_sport == "Taekwondo":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    if li.text.strip()[0] == "H":
                        epreuves.append(f"{li.text.strip()[2:]} (hommes)")
                    else :
                        epreuves.append(f"{li.text.strip()[2:]} (femmes)")
                return  epreuves
            
            elif title_sport == "Voile":
                l_li = divs[i+2].find_all('li')
                genre = ["femmes","hommes","mixte"]
                i = 0
                for li in l_li:
                    epr = li.text.strip()
                    epreuves.append(f"{epr[epr.index(':')+2:]} ({genre[i]})")
                    i+=1
                
                return  epreuves
            
            elif title_sport == "Natation artistique":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(f"{li.text.strip()} (mixte)")
                return  epreuves
            
            elif title_sport == "Athlétisme":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    if li.text.strip() == "Marche sur un marathon en relais mixte":
                        epreuves.append("Marche sur un marathon en relais (mixte)")
                    else :
                        epreuves.append(li.text.strip())
                    epreuves[-1] = epreuves[-1][0:epreuves[-1].index(')')+1]
                return  epreuves
            
            elif title_sport == "Natation":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    if li.text.strip() == "Relais mixte 4x100m quatre nages":
                        epreuves.append("Relais 4x100m quatre nages (mixte)")
                    else :
                        epreuves.append(li.text.strip())
                    epreuves[-1] = epreuves[-1][0:epreuves[-1].index(')')+1]
                return  epreuves
            
            elif title_sport == "Boccia":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace("femmes-hommes","femmes/hommes"))
                for i in range(4,len(epreuves)):
                    epreuves[i] = epreuves[i].replace(' mixte','') +' (mixte)'
                    
                return  epreuves
            
            elif title_sport == "Cécifoot":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace(" masculin","") + " (hommes)")
                return  epreuves
            
            elif title_sport == "Escrime fauteuil":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace("femmes, hommes","femmes/hommes"))
                return  epreuves
            
            elif title_sport == "Para athlétisme":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    txt = li.text.strip()
                    if txt == "Relais mixte 4x100m":
                        epreuves.append(txt.replace(' mixte','') + ' (mixte)')
                    else:
                        if 'T' in txt:
                            name_event = txt[0:txt.index('T')]
                            reste = txt[txt.index('T'):]
                        else:
                            name_event = txt[0:txt.index('F')]
                            reste = txt[txt.index('F'):]
                        epr = reste.split('.')
                        for ep in epr:
                            if ep != "":
                                epreuves.append(f"{name_event}{ep}".replace("femmes-hommes","femmes/hommes"))
                return  epreuves
                
            elif title_sport == "Para aviron":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                epreuves[1] = epreuves[1].replace(" (men’s)","").replace(" (women’s)",'') + ' (mixte)'
                return  epreuves
            
            elif title_sport == "Para badminton":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace('dames-hommes','femmes/hommes'))
                for epr in range(len(epreuves)-2,len(epreuves)):
                    epreuves[epr] = epreuves[epr].replace('mixte ','') + ' (mixte)'
                return  epreuves
            
            elif title_sport == "Para canoë":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace('-','/'))
                return  epreuves
            
            elif title_sport == "Para cyclisme sur route":                
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace('femmes-hommes','femmes/hommes'))
                epreuves[-1] = epreuves[-1].replace('mixte ','') + ' (mixte)'
                return  epreuves
            
            elif title_sport == "Para cyclisme sur piste":
                l = divs[i+2:i+15]
                for div in l:
                    epreuves.append(div.find('p').text.strip().replace('femmes-hommes','femmes/hommes'))
                return epreuves
            
            elif title_sport == "Para équitation (para dressage)":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(f"{li.text.strip()} (mixte)")
                return  epreuves
            
            elif title_sport == "Para powerlifting":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    c = li.text.strip().replace("Jusqu’à ","-")
                    epreuves.append(f"{c} (femmes)")
                l_li = divs[i+5].find_all('li')
                for li in l_li:
                    c = li.text.strip().replace("Jusqu’à ","-")
                    epreuves.append(f"{c} (hommes)")
                return  epreuves
            
            elif title_sport == "Para judo":
                l_li = divs[i+2].find_all('li')
                for li in range(0,4):
                    epreuves.append(l_li[li].text.strip().replace(" (femmes)","") + " (femmes)")
                for li in range(4,len(l_li)):
                    epreuves.append(l_li[li].text.strip().replace(" (hommes)","") + " (hommes)")
                return  epreuves
            
            elif title_sport == "Para natation":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    txt = li.text.strip()
                    genre = txt[txt.index('('):txt.index(')')+1].replace('-','/')
                    nom_event = txt[0:txt.index('(')]
                    epreuves.append(f"{nom_event}{genre}")
                return  epreuves
            
            elif title_sport == "Para taekwondo":
                l_li = divs[i+2].find_all('li')
                
                for li in range(len(l_li)):
                    l_li[li] = l_li[li].text.split()
                    deca = 0
                    for elt in range(len(l_li[li])):
                        if l_li[li][0][0] != '-' and l_li[li][0][0] != '+' and l_li[li][0] != "K44":
                            del l_li[li][elt-deca]
                            deca += 1
                for epr in range (1,len(l_li[0])):
                    epreuves.append(f"{l_li[0][0]} {l_li[0][epr][0:-1]} (femmes)")
                for epr in range (1,len(l_li[1])):
                    epreuves.append(f"{l_li[1][0]} {l_li[1][epr][0:-1]} (hommes)")
                return epreuves
            
            elif title_sport == "Para tennis de table":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace("femmes-hommes","femmes/hommes"))
                return  epreuves
            
            elif title_sport == "Para tir sportif":
                l_li = divs[i+3].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                l_li = divs[i+5].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                return  epreuves
            
            elif title_sport == "Para triathlon":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace("femmes, hommes","femmes/hommes"))
                return  epreuves
            
            elif title_sport == "Rugby fauteuil":
                epreuves.append("Tournoi 8 équipes (mixte)")
                return  epreuves
            
            elif title_sport == "Tennis fauteuil":
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip().replace("femmes, hommes","femmes/hommes"))
                return  epreuves
            elif title_sport == "Volleyball assis" or title_sport == "Goalball":
                epreuves.append("Tournoi 8 équipes (femmes)")
                epreuves.append("Tournoi 8 équipes (hommes)")
                return  epreuves
            # Cas général.
            else:                
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                return  epreuves
            
def get_table_event(l_event):
    """[nom_sport, eprv1, eprv2...]"""
    table = []
    for sport in l_event:
        for i in range(1,len(sport)):
            temp_nom_event = sport[i][0:sport[i].index('(')-1]
            temp_nom_event = re.sub(r'(\d+m)(?![^\s])', r'\1 ', nom_event.replace("\u202f", "").replace("\u2019", "'").replace("\u00a0", " ").replace("\u2013", "-"))
            nom_event = re.sub(r'\s+', ' ', temp_nom_event)
            if nom_event[-1] == " ":
                nom_event = nom_event[:-1]
            genre = sport[i][sport[i].index('(')+1:sport[i].index(')')].split('/')
            for g in genre:
                dico = {}
                dico['name_event'] = nom_event
                #Trouver si c'est une épreuve collective ou non
                for mot in MOT_EQUIPE:
                    if mot in nom_event:
                        dico['format_event'] = "Collective"
                if 'format_event' not in dico.keys():
                    if 'équipe' in g:
                        dico['format_event'] = "Collective"
                    else:
                        dico['format_event'] = "Individual"
                
                #Connaitre si c'est une épreuve hommes, femmes, ou mixte
                if "femmes" in g:
                    dico['gender_event'] = "Femme"
                elif "hommes" in g:
                    dico['gender_event'] = "Homme"
                else:
                    dico['gender_event'] = "Mixte"
                dico['discipline'] = sport[0].lower()
                table.append(dico)
                
    return table
            
def recup_event():
    pages_sport = obtenir_pages_sports_olympiques_fr() + obtenir_pages_sports_paralympiques_fr()
    l_epreuves = []
    for url in pages_sport:
        epreuves = obtenir_epreuves(url)
        if epreuves != None:
            l_epreuves.append(epreuves)
            # print(f"--- {l_epreuves[-1][0]} ---")
            # for i in range(1,len(l_epreuves[-1])):
            #     print(l_epreuves[-1][i])
    print("EVENT SCRAP FAIT")
    return get_table_event(l_epreuves)

def send_event(result, disc_table, record_table, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Event (name_event, format_event, gender_event, id_disc, id_record) VALUES\n"
    for dic in result:
        id_discipline = get_dic_id_table(disc_table, name_fr_disc=dic.get("discipline"))
        id_record = get_dic_id_table_in(record_table, discipline=dic.get("discipline"), event=dic.get("name_event"))
        send += ("('" + dic.get("name_event").replace("'", "''") + "', '" +
            dic.get("format_event") + "', '" +
            dic.get("gender_event") + "', " +
            id_discipline + ", " +
            id_record + "),\n")
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
    return send_event(recup_event)

if __name__ == "__main__":
    # print(send_event(recup_event(), recup_discipline(), recup_record()))
    #print(send_event(recup_event(), json_to_data("./saved_json/discipline.json"), json_to_data("./saved_json/record.json")))
    print(recup_event())