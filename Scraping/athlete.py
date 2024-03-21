###################
# Script de scraping Athlete
###################

##### Import #####
import doctest
import requests
from bs4 import BeautifulSoup
import ast

##### Code #####
list_record = []  # Dict où chaque clé représente un attribut de la table record

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

def scraping_athlete(soup):
    '''
    Retourne la liste de liste des athletes 
    param : Objet BeautifulSoup soup
    return : list(list) liste
    '''