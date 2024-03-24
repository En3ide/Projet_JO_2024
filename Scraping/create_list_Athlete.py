###################
# Script de scraping Athlete
###################

##### Import #####
import doctest
import requests
from bs4 import BeautifulSoup
import ast

##### Code #####
list_record = [{'name_athlete' : 'Bolt' , 'firstname_athlete' : 'Usain', 'birthday_athlete' : '1986-08-21', "gender_athlete" : "Homme", "code_country" : "JAM"},
               {'name_athlete' : 'Thompson-Herah' , 'firstname_athlete' : 'Elaine', 'birthday_athlete' : '1992-06-28', "gender_athlete" : "Femme", "code_country" : "JAM"},
               {'name_athlete' : 'Beamon' , 'firstname_athlete' : 'Bob', 'birthday_athlete' : '1946-08-29', "gender_athlete" : "Homme", "code_country" : "USA"}]  # list de dict où chaque clé représente un attribut de la table record