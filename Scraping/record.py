###################
# Script de scraping Record
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

def scraping_athletisme(soup):
    '''
    Retourne la liste de liste de althletisme 
    param : Objet BeautifulSoup soup
    return : list(list) liste
    '''
    liste = []
    tables = soup.find_all("table")
    for i in range (0,3):
        for tr in tables[i].find_all('tr') :
            cells = tr.find_all('td')
            content = [cell.text for cell in cells]
            if len(content) > 0 and not contient_n_fois(content[1]," ",3):
                content[0] = selection(content[0])
                content.pop(-1)
                liste.append(content)
    return liste

def contient_n_fois(ch,c,nbr):
    '''
    Renvoie True si la chaine de caractere ch possede nbr caractere c
    param : (str) ch -> chaine de caractere , (str) c -> caractere, (int) nbr -> nombre d'iteration
    return : Boolean 
    '''
    n = 0
    for char in ch :
        if c == char :
            n += 1
    return n >= nbr
    
def selection(ch):
    '''
    Renvoie ch sans le mot "Progression"
    param : (str) ch -> chaine de caractere
    return : (str) ch
    '''
    index = ch.index('Progression')
    return ch[0:index]

def remplir_dict(liste , sport):
    '''
    Permet de remplir le liste de dict
    param : (list(list)) liste -> liste de scraping, (str) sport 
    return : (list(dict)) liste_dict
    '''
    liste_dict = []
    for l in liste :
        dict = {"stat_record" : l[3],"date_record" : l[4],"id_event" : None,"id_athele" : None, "discipline" : sport , "event" : l[0], "athlete" : l[1]}
        liste_dict.append(dict)
    return liste_dict

def scraping_natation(soup):
    '''
    Retourne la liste de dictionnaire de natation
    param : Objet BeautifulSoup soup
    return : list(dict) liste 
    '''
    liste = []
    tables = soup.find_all("table")
    for i in range(7,10) :
        for tr in tables[i].find_all('tr') :
            cells = tr.find_all('td')
            content = [cell.text.replace("\n","") for cell in cells]
            if len(content) > 0 and not contient_n_fois(content[2]," ",3):
                content.pop(-1)
                liste.append([content[0], content[2], content[5],content[1],content[4],content[3]])
    return liste


##### Main #####
def main():
    '''
    Fonction principal
    '''
    # ATHLETISME 
    soup = contenue("https://fr.wikipedia.org/wiki/Records_olympiques_d%27athl%C3%A9tisme")
    liste = scraping_athletisme(soup)
    dict = remplir_dict(liste, "athletisme")
    # NATATION
    soup = contenue("https://fr.wikipedia.org/wiki/Natation_aux_Jeux_olympiques")
    liste =  scraping_natation(soup)
    dict += remplir_dict(liste, "natation ")
    return dict



print(main())
