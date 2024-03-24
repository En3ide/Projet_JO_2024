import requests
from bs4 import BeautifulSoup

MOT_EQUIPE = ["équipes","équipe","Equipe","relais","Relais","Double","double","football","ensembles","handball","hockey","Duo","duos","synchronisé","water-polo","volleyball","rugby"]

def obtenir_pages_sports_olympiques_fr():
    pages_sports_olympiques = []
    # Récupération des sports des Jeux Olympiques de Paris 2024
    réponse = requests.get("https://www.paris2024.org/fr/sports-olympiques/")
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        # Trouver tous les divs avec la classe 'block-classic-editor'
        divs = soup.find_all('div', class_='block-classic-editor')
        # Les sports se trouvent dans le 4 et 6 div de cette classe
        targeted_div = [divs[3],divs[5]]
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
    # Récupération des sports des Jeux Paralympiques de Paris 2024
    réponse = requests.get(url)
    if réponse.status_code == 200:
        soup = BeautifulSoup(réponse.text, 'html.parser')
        title_sport = soup.find_all('h1')[0].text.strip()
        epreuves.append(title_sport)
        
        divs = soup.find_all('div','block-classic-editor')
        l_li = []
    for i in range (len(divs)):
        h2 = divs[i].find_all('h2')
        
        if h2 != [] and h2[0].text.strip() == "Epreuves en 2024":
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
                epreuves.append("Epreuves en ligne (femmes/hommes")
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
                
            # Cas général.
            else:                
                l_li = divs[i+2].find_all('li')
                for li in l_li:
                    epreuves.append(li.text.strip())
                return  epreuves
                
            #En boxe les catégories de poids ont pas encore été défini

def get_table_event(l_event, cat = "O"):
    """[nom_sport, eprv1, eprv2...]"""
    table = []
    for sport in l_event:
        dico = {}
        for event in sport:
            pass
            

def main():
    pages_sports_olympiques_fr = obtenir_pages_sports_olympiques_fr()
    pages_sports_paralympiques_fr = obtenir_pages_sports_paralympiques_fr()
    
    l_epreuves = []
    for url in pages_sports_olympiques_fr:
        l_epreuves.append(obtenir_epreuves(url))
        print(f"--- {l_epreuves[-1][0]} ---")
        for i in range(1,len(l_epreuves[-1])):
            print(l_epreuves[-1][i])
    if __name__ == "__main__":
    main()

