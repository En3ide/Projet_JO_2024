###################
# Script de scraping Athlete
###################

##### Import #####
import doctest
import requests
from bs4 import BeautifulSoup
import ast

##### Code #####
list_record = []  # list de dict où chaque clé représente un attribut de la table record

def contenue(url):
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

def scraping_usain_bolt(soup):
    '''
    Retourne la liste de liste des athletes 
    param : Objet BeautifulSoup soup
    return : list(list) liste
    '''
    liste = []
    tables = soup.find_all("table")
    for tr in tables[0].find_all("tr"):
        cells = tr.find_all('td')
        content = [cell.text for cell in cells]
        print(content)

def main():
    '''
    Fonction principale
    '''
    # Usain bolt
    soup = contenue("https://fr.wikipedia.org/wiki/Usain_Bolt")
    print(scraping_usain_bolt(soup))

main()