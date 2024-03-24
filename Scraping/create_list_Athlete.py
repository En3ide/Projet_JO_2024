###################
# Script de scraping table Athlete
###################

##### Import #####
import doctest
import requests
from bs4 import BeautifulSoup
import ast

##### Code #####
list_record = [{'firstname_athlete' : 'Usain', 'name_athlete' : 'Bolt' , 'birthday_athlete' : '1986-08-21', "gender_athlete" : "Homme", "code_country" : "JAM"},
               {'firstname_athlete' : 'Elaine', 'name_athlete' : 'Thompson-Herah', 'birthday_athlete' : '1992-06-28', "gender_athlete" : "Femme", "code_country" : "JAM"},
               {'firstname_athlete' : 'Bob', 'name_athlete' : 'Beamon', 'birthday_athlete' : '1946-08-29', "gender_athlete" : "Homme", "code_country" : "USA"}]  # list de dict où chaque clé représente un attribut de la table record

def recup_athlete():
    return list_record