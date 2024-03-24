from bs4 import BeautifulSoup
import requests, ast, sqlite3

def send_transp(bdd=""):
    send = "INSERT INTO Transport (id_trans) VALUES\n"
    send += ("('Train'),\n")
    +("('Tramway'),\n")
    +("('Métro'),\n")
    +("('Train'),\n")
    +";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    return(send)