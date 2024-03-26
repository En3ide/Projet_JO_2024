###################
# Script de scraping table Athlete
###################

##### Import #####
import doctest
import requests, sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
import ast

##### Code #####
# list de dict où chaque clé représente un attribut de la table record
list_record = [{'name_athlete' : 'Bolt' , 'firstname_athlete' : 'Usain', 'birthday_athlete' : '1986-08-21', "gender_athlete" : "Homme", "code_country" : "JAM"},
                {'firstname_athlete': 'Elaine', 'name_athlete': 'Thompson-Herah', 'birthday_athlete': '1992-06-28', 'gender_athlete': 'Femme', 'code_country': 'JAM'},
                {'firstname_athlete': 'Bob', 'name_athlete': 'Beamon', 'birthday_athlete': '1946-08-29', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete': 'Wayde', 'name_athlete': 'van Niekerk', 'birthday_athlete': '1992-07-15', 'gender_athlete': 'Homme', 'code_country': 'ZAF'},
                {'firstname_athlete': 'David', 'name_athlete': 'Rudisha', 'birthday_athlete': '1988-12-17', 'gender_athlete': 'Homme', 'code_country': 'KEN'},
                {'firstname_athlete': 'Jakob', 'name_athlete': 'Ingebrigtsen', 'birthday_athlete': '2000-09-19', 'gender_athlete': 'Homme', 'code_country': 'NOR'},
                {'firstname_athlete': 'Kenenisa', 'name_athlete': 'Bekele', 'birthday_athlete': '1982-06-13', 'gender_athlete': 'Homme', 'code_country': 'ETH'},
                {'firstname_athlete': 'Samuel', 'name_athlete': 'Wanjiru', 'birthday_athlete': '1986-11-10', 'gender_athlete': 'Homme', 'code_country': 'KEN'},
                {'firstname_athlete': 'Liu', 'name_athlete': 'Xiang', 'birthday_athlete': '1983-07-13', 'gender_athlete': 'Homme', 'code_country': 'CHN'},
                {'firstname_athlete': 'Karsten', 'name_athlete': 'Warholm', 'birthday_athlete': '1996-02-28', 'gender_athlete': 'Homme', 'code_country': 'NOR'},
                {'firstname_athlete': 'Conseslus', 'name_athlete': 'Kipruto', 'birthday_athlete': '1994-12-08', 'gender_athlete': 'Homme', 'code_country': 'KEN'},
                {'firstname_athlete': 'Chen', 'name_athlete': 'Ding', 'birthday_athlete': '1992-08-05', 'gender_athlete': 'Homme', 'code_country': 'CHN'},
                {'firstname_athlete': 'Jared', 'name_athlete': 'Tallent', 'birthday_athlete': '1984-10-17', 'gender_athlete': 'Homme', 'code_country': 'AUS'},
                {'firstname_athlete': 'Kenny', 'name_athlete': 'Harrison', 'birthday_athlete': '1965-02-13', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete': 'Thiago', 'name_athlete': 'Braz da Silva', 'birthday_athlete': '1993-12-16', 'gender_athlete': 'Homme', 'code_country': 'BRA'},
                {'firstname_athlete': 'Ryan', 'name_athlete': 'Crouser', 'birthday_athlete': '1992-12-18', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete': 'Virgilijus', 'name_athlete': 'Alekna', 'birthday_athlete': '1972-02-13', 'gender_athlete': 'Homme', 'code_country': 'LTU'},
                {'firstname_athlete': 'Sergey', 'name_athlete': 'Litvinov', 'birthday_athlete': '1992-12-18', 'gender_athlete': 'Homme', 'code_country': 'BLR'},
                {'firstname_athlete': 'Andreas', 'name_athlete': 'Thorkildsen', 'birthday_athlete': '1982-04-01', 'gender_athlete': 'Homme', 'code_country': 'NOR'},
                {'firstname_athlete': 'Damian', 'name_athlete': 'Warner', 'birthday_athlete': '1989-10-04', 'gender_athlete': 'Homme', 'code_country': 'CAN'},
                {'firstname_athlete': 'Florence', 'name_athlete': 'Griffith-Joyner', 'birthday_athlete': '1959-12-21', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Marie-José', 'name_athlete': 'Pérec', 'birthday_athlete': '1968-05-09', 'gender_athlete': 'Femme', 'code_country': 'FRA'},
                {'firstname_athlete': 'Nadiya', 'name_athlete': 'Olizarenko', 'birthday_athlete': '1953-11-28', 'gender_athlete': 'Femme', 'code_country': 'UKR'},
                {'firstname_athlete': 'Faith', 'name_athlete': 'Kipyegon', 'birthday_athlete': '1994-01-10', 'gender_athlete': 'Femme', 'code_country': 'KEN'},
                {'firstname_athlete': 'Vivian', 'name_athlete': 'Cheruiyot', 'birthday_athlete': '1983-09-11', 'gender_athlete': 'Femme', 'code_country': 'KEN'},
                {'firstname_athlete': 'Almaz', 'name_athlete': 'Ayana', 'birthday_athlete': '1991-11-21', 'gender_athlete': 'Femme', 'code_country': 'ETH'},
                {'firstname_athlete': 'Tiki', 'name_athlete': 'Gelana', 'birthday_athlete': '1987-10-22', 'gender_athlete': 'Femme', 'code_country': 'ETH'},
                {'firstname_athlete': 'Jasmine', 'name_athlete': 'Camacho-Quinn', 'birthday_athlete': '1996-08-21', 'gender_athlete': 'Femme', 'code_country': 'PRI'},
                {'firstname_athlete': 'Sydney', 'name_athlete': 'McLaughlin', 'birthday_athlete': '1999-09-07', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Gulnara', 'name_athlete': 'Samitova-Galkina', 'birthday_athlete': '1978-07-09', 'gender_athlete': 'Femme', 'code_country': 'RUS'},
                {'firstname_athlete': 'Qieyang', 'name_athlete': 'Shenjie', 'birthday_athlete': '1990-11-11', 'gender_athlete': 'Femme', 'code_country': 'CHN'},
                {'firstname_athlete': 'Jackie', 'name_athlete': 'Joyner-Kersee', 'birthday_athlete': '1962-03-03', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Yulimar', 'name_athlete': 'Rojas', 'birthday_athlete': '1995-10-21', 'gender_athlete': 'Femme', 'code_country': 'VEN'},
                {'firstname_athlete': 'Yelena', 'name_athlete': 'Slesarenko', 'birthday_athlete': '1982-02-28', 'gender_athlete': 'Femme', 'code_country': 'RUS'},
                {'firstname_athlete': 'Yelena', 'name_athlete': 'Isinbayeva', 'birthday_athlete': '1982-06-03', 'gender_athlete': 'Femme', 'code_country': 'RUS'},
                {'firstname_athlete': 'Ilona', 'name_athlete': 'Slupianek', 'birthday_athlete': '1956-09-24', 'gender_athlete': 'Femme', 'code_country': 'DEU'},
                {'firstname_athlete': 'Martina', 'name_athlete': 'Hellmann', 'birthday_athlete': '1960-12-12', 'gender_athlete': 'Femme', 'code_country': 'DEU'},
                {'firstname_athlete': 'Anita', 'name_athlete': 'Włodarczyk', 'birthday_athlete': '1985-08-08', 'gender_athlete': 'Femme', 'code_country': 'POL'},
                {'firstname_athlete': 'Olisdeilys', 'name_athlete': 'Menéndez', 'birthday_athlete': '1979-11-14', 'gender_athlete': 'Femme', 'code_country': 'CUB'},
                {'firstname_athlete': 'Caeleb', 'name_athlete': 'Dressel', 'birthday_athlete': '1996-08-16', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete' : 'Michael', 'name_athlete' : 'Phelps', 'birthday_athlete' : '1985-06-30', "gender_athlete" : "Homme", "code_country" : "USA"},
                {'firstname_athlete': 'Michael', 'name_athlete': 'Phelps', 'birthday_athlete': '1985-06-30', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete': 'Sun', 'name_athlete': 'Yang', 'birthday_athlete': '1991-12-01', 'gender_athlete': 'Homme', 'code_country': 'CHN'},
                {'firstname_athlete': 'Mykhailo', 'name_athlete': 'Romanchuk', 'birthday_athlete': '1996-08-07', 'gender_athlete': 'Homme', 'code_country': 'UKR'},
                {'firstname_athlete': 'Ryan', 'name_athlete': 'Murphy', 'birthday_athlete': '1965-11-09', 'gender_athlete': 'Homme', 'code_country': 'USA'},
                {'firstname_athlete': 'Evgeny', 'name_athlete': 'Rylov', 'birthday_athlete': '1996-09-23', 'gender_athlete': 'Homme', 'code_country': 'RUS'},
                {'firstname_athlete': 'Adam', 'name_athlete': 'Peaty', 'birthday_athlete': '1994-12-28', 'gender_athlete': 'Homme', 'code_country': 'GBR'},
                {'firstname_athlete': 'Zac', 'name_athlete': 'Stubblety-Cook', 'birthday_athlete': '1999-01-04', 'gender_athlete': 'Homme', 'code_country': 'AUS'},
                {'firstname_athlete': 'Joseph', 'name_athlete': 'Schooling', 'birthday_athlete': '1995-06-16', 'gender_athlete': 'Homme', 'code_country': 'SGP'},
                {'firstname_athlete': 'Kristóf', 'name_athlete': 'Milák', 'birthday_athlete': '2000-02-20', 'gender_athlete': 'Homme', 'code_country': 'HUN'},
                {'firstname_athlete': 'Emma', 'name_athlete': 'McKeon', 'birthday_athlete': '1994-05-24', 'gender_athlete': 'Femme', 'code_country': 'AUS'},
                {'firstname_athlete': 'Ariarne', 'name_athlete': 'Titmus', 'birthday_athlete': '2000-09-07', 'gender_athlete': 'Femme', 'code_country': 'AUS'},
                {'firstname_athlete': 'Katie', 'name_athlete': 'Ledecky', 'birthday_athlete': '1997-03-17', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Kaylee', 'name_athlete': 'McKeown', 'birthday_athlete': '2001-07-11', 'gender_athlete': 'Femme', 'code_country': 'AUS'},
                {'firstname_athlete': 'Missy', 'name_athlete': 'Franklin', 'birthday_athlete': '1995-05-10', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Lilly', 'name_athlete': 'King', 'birthday_athlete': '1997-02-10', 'gender_athlete': 'Femme', 'code_country': 'USA'},
                {'firstname_athlete': 'Tatjana', 'name_athlete': 'Schoenmaker', 'birthday_athlete': '1997-07-09', 'gender_athlete': 'Femme', 'code_country': 'ZAF'},
                {'firstname_athlete': 'Sarah', 'name_athlete': 'Sjöström', 'birthday_athlete': '1993-08-17', 'gender_athlete': 'Femme', 'code_country': 'SWE'},
                {'firstname_athlete': 'Zhang', 'name_athlete': 'Yufei', 'birthday_athlete': '1998-04-19', 'gender_athlete': 'Femme', 'code_country': 'CHN'},
                {'firstname_athlete': 'Katinka', 'name_athlete': 'Hosszú', 'birthday_athlete': '1985-05-03', 'gender_athlete': 'Femme', 'code_country': 'HUN'}]

def recup_athlete():
    print('[',datetime.now().time(),'] ', "Recup Athlete fini !!!")
    return list_record

def send_athlete(result, bdd=""):
    # Création de la requête SQL
    send = "INSERT INTO Athlete (firstname_athlete, name_athlete, birthday_athlete, gender_athlete, code_country) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("firstname_athlete") + "', '" +
            dic.get("name_athlete") + "', '" +
            dic.get("birthday_athlete") + "', '" +
            dic.get("gender_athlete") + "', '" +
            dic.get("code_country") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print('[',datetime.now().time(),'] ', "sql Athlete fini !!!")
    return(send)

def create_sql():
    return send_athlete(recup_athlete())

if __name__ == "__main__":
    send_athlete(recup_athlete())