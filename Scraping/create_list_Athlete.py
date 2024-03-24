###################
# Script de scraping table Athlete
###################

##### Import #####
import doctest
import requests
from bs4 import BeautifulSoup
import ast

##### Code #####
list_record = [{'name_athlete' : 'Bolt' , 'firstname_athlete' : 'Usain', 'birthday_athlete' : '1986-08-21', "gender_athlete" : "Homme", "code_country" : "JAM"},
               {'name_athlete' : 'Thompson-Herah' , 'firstname_athlete' : 'Elaine', 'birthday_athlete' : '1992-06-28', "gender_athlete" : "Femme", "code_country" : "JAM"},
               {'name_athlete' : 'Beamon' , 'firstname_athlete' : 'Bob', 'birthday_athlete' : '1946-08-29', "gender_athlete" : "Homme", "code_country" : "USA"},
               {'name_athlete' : 'van Niekerk' , 'firstname_athlete' : 'Wayde', 'birthday_athlete' : '1992-07-15', "gender_athlete" : "Homme", "code_country" : "ZAF"},
               {'name_athlete' : 'Rudisha' , 'firstname_athlete' : 'David', 'birthday_athlete' : '1988-12-17', "gender_athlete" : "Homme", "code_country" : "KEN"},
               {'name_athlete' : 'Ingebrigtsen' , 'firstname_athlete' : 'Jakob', 'birthday_athlete' : '2000-09-19', "gender_athlete" : "Homme", "code_country" : "NOR"},
               {'name_athlete' : 'Bekele' , 'firstname_athlete' : 'Kenenisa', 'birthday_athlete' : '1982-06-13', "gender_athlete" : "Homme", "code_country" : "ETH"},
               {'name_athlete' : 'Wanjiru' , 'firstname_athlete' : 'Samuel', 'birthday_athlete' : '1986-11-10', "gender_athlete" : "Homme", "code_country" : "KEN"},
               {'name_athlete' : 'Xiang' , 'firstname_athlete' : 'Liu', 'birthday_athlete' : '1983-07-13', "gender_athlete" : "Homme", "code_country" : "CHN"},
               {'name_athlete' : 'Warholm' , 'firstname_athlete' : 'Karsten', 'birthday_athlete' : '1996-02-28', "gender_athlete" : "Homme", "code_country" : "NOR"},
               {'name_athlete' : 'Kipruto' , 'firstname_athlete' : 'Conseslus', 'birthday_athlete' : '1994-12-08', "gender_athlete" : "Homme", "code_country" : "KEN"},
               {'name_athlete' : 'Ding' , 'firstname_athlete' : 'Chen', 'birthday_athlete' : '1992-08-05', "gender_athlete" : "Homme", "code_country" : "CHN"},
               {'name_athlete' : 'Tallent' , 'firstname_athlete' : 'Jared', 'birthday_athlete' : '1984-10-17', "gender_athlete" : "Homme", "code_country" : "AUS"},
               {'name_athlete' : 'Harrison' , 'firstname_athlete' : 'Kenny', 'birthday_athlete' : '1965-02-13', "gender_athlete" : "Homme", "code_country" : "USA"},
               {'name_athlete' : 'Braz da Silva' , 'firstname_athlete' : 'Thiago', 'birthday_athlete' : '1993-12-16', "gender_athlete" : "Homme", "code_country" : "BRA"},
               {'name_athlete' : 'Crouser' , 'firstname_athlete' : 'Ryan', 'birthday_athlete' : '1992-12-18', "gender_athlete" : "Homme", "code_country" : "USA"},
               {'name_athlete' : 'Alekna' , 'firstname_athlete' : 'Virgilijus', 'birthday_athlete' : '1972-02-13', "gender_athlete" : "Homme", "code_country" : "LTU"},
               {'name_athlete' : 'Litvinov' , 'firstname_athlete' : 'Sergey', 'birthday_athlete' : '1992-12-18', "gender_athlete" : "Homme", "code_country" : "BLR"},
               {'name_athlete' : 'Thorkildsen' , 'firstname_athlete' : 'Andreas', 'birthday_athlete' : '1982-04-01', "gender_athlete" : "Homme", "code_country" : "NOR"},
               {'name_athlete' : 'Warner' , 'firstname_athlete' : 'Damian', 'birthday_athlete' : '1989-10-04', "gender_athlete" : "Homme", "code_country" : "CAN"},
               {'name_athlete' : 'Griffith-Joyner' , 'firstname_athlete' : 'Florence', 'birthday_athlete' : '1959-12-21', "gender_athlete" : "Femme", "code_country" : "USA"},
               {'name_athlete' : 'Pérec' , 'firstname_athlete' : 'Marie-José', 'birthday_athlete' : '1968-05-09', "gender_athlete" : "Femme", "code_country" : "FRA"},
               {'name_athlete' : 'Olizarenko' , 'firstname_athlete' : 'Nadiya', 'birthday_athlete' : '1953-11-28', "gender_athlete" : "Femme", "code_country" : "UKR"},
               {'name_athlete' : 'Kipyegon' , 'firstname_athlete' : 'Faith', 'birthday_athlete' : '1994-01-10', "gender_athlete" : "Femme", "code_country" : "KEN"},
               {'name_athlete' : 'Cheruiyot' , 'firstname_athlete' : 'Vivian', 'birthday_athlete' : '1983-09-11', "gender_athlete" : "Femme", "code_country" : "KEN"},
               {'name_athlete' : 'Ayana' , 'firstname_athlete' : 'Almaz', 'birthday_athlete' : '1991-11-21', "gender_athlete" : "Femme", "code_country" : "ETH"},
               {'name_athlete' : 'Gelana' , 'firstname_athlete' : 'Tiki', 'birthday_athlete' : '1987-10-22', "gender_athlete" : "Femme", "code_country" : "ETH"},
               {'name_athlete' : 'Camacho-Quinn' , 'firstname_athlete' : 'Jasmine', 'birthday_athlete' : '1996-08-21', "gender_athlete" : "Femme", "code_country" : "PRI"},
               {'name_athlete' : 'McLaughlin' , 'firstname_athlete' : 'Sydney', 'birthday_athlete' : '1999-09-07', "gender_athlete" : "Femme", "code_country" : "USA"},
               {'name_athlete' : 'Samitova-Galkina' , 'firstname_athlete' : 'Gulnara', 'birthday_athlete' : '1978-07-09', "gender_athlete" : "Femme", "code_country" : "RUS"},
               {'name_athlete' : 'Shenjie' , 'firstname_athlete' : 'Qieyang', 'birthday_athlete' : '1990-11-11', "gender_athlete" : "Femme", "code_country" : "CHN"},
               {'name_athlete' : 'Joyner-Kersee' , 'firstname_athlete' : 'Jackie', 'birthday_athlete' : '1962-03-03', "gender_athlete" : "Femme", "code_country" : "USA"},
               {'name_athlete' : 'Rojas' , 'firstname_athlete' : 'Yulimar', 'birthday_athlete' : '1995-10-21', "gender_athlete" : "Femme", "code_country" : "VEN"},
               {'name_athlete' : 'Slesarenko' , 'firstname_athlete' : 'Yelena', 'birthday_athlete' : '1982-02-28', "gender_athlete" : "Femme", "code_country" : "RUS"},
               {'name_athlete' : 'Isinbayeva' , 'firstname_athlete' : 'Yelena', 'birthday_athlete' : '1982-06-03', "gender_athlete" : "Femme", "code_country" : "RUS"},
               {'name_athlete' : 'Slupianek' , 'firstname_athlete' : 'Ilona', 'birthday_athlete' : '1956-09-24', "gender_athlete" : "Femme", "code_country" : "DEU"},
               {'name_athlete' : 'Hellmann' , 'firstname_athlete' : 'Martina', 'birthday_athlete' : '1960-12-12', "gender_athlete" : "Femme", "code_country" : "DEU"},
               {'name_athlete' : 'Włodarczyk' , 'firstname_athlete' : 'Anita', 'birthday_athlete' : '1985-08-08', "gender_athlete" : "Femme", "code_country" : "POL"},
               {'name_athlete' : 'Menéndez' , 'firstname_athlete' : 'Olisdeilys', 'birthday_athlete' : '1979-11-14', "gender_athlete" : "Femme", "code_country" : "CUB"},]  # list de dict où chaque clé représente un attribut de la table record
def recup_athlete():
    return list_record