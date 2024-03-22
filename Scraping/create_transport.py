from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime

url_tmp = "https://olympics.com/fr/paris-2024/sites"

def recup_url_transp(url):
    print("test1")
    reponse = requests.get(url)
    print("test2")
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Extraction du tableau
        #tab = soup.find_all('table', class_=['content-list-grid'])
        print("test3")
    else:
        print(reponse.status_code)
        return([])

recup_url_transp(url_tmp)