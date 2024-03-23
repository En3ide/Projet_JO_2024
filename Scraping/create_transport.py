from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime

url_tmp = "https://olympics.com/fr/paris-2024/sites"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
def recup_url_transp(url):
    print("test1")
    reponse = requests.get(url, headers=HEADERS)
    print("test2")
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        result = []
        # Extraction du tableau
        ul = soup.find('ul', class_ = "content-list-grid")
        tab_site = ul.find_all('li')
        if tab_site != None:
            for site in tab_site:
                href = site.find('a').get('href')
                #print(href.split("/")[-1].replace("-", " "))
                if href != None:
                    #print(href)
                    print(href.split("/")[-1])
                    print(recup_transp_v2(href))
                    result.append({"name_site": href.split("/")[-1].replace("-", " "), "transport": recup_transp_v2(href)})
    else:
        print(reponse.status_code)
        print('Fini !!!')
        return([])

def recup_transp(url):
    reponse = requests.get(url, headers=HEADERS)
    result = []
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        section = soup.find_all('section', class_='text-block')
        for sec in section:
            #print('test3\n'+sec.text)
            if 'INFORMATIONS SUR LES TRANSPORTS' in sec.text:
                p = sec.find('p')
                p = p.replace(") et", "),")
                for part in p.text.split('),'):
                    print(part)
                    if 'gare' in part:
                        if ", " in part:
                            tmp = part[part.find('(')+1:].split(", ")
                        else:
                            tmp = [part[part.find('(')+1:].replace(")", "").replace(".", "")]
                        result.append({"type": "gare",
                                       "name" : part[part.find('«')+2:part.find('»')-1],
                                       "number":  tmp})
                    if 'station' in part:
                        if ", " in part:
                            tmp = part[part.find('(')+1:].replace(")", "").replace(".", "").split(", ")
                        else:
                            tmp = [part[part.find('(')+1:].replace(")", "").replace(".", "")]
                        result.append({"type": "station",
                                       "name": part[part.find('«')+2:part.find('»')-1],
                                        "number": tmp })
    #print(result)
    return result

def recup_transp_v2(url):
    #print('test 1')
    reponse = requests.get(url, headers=HEADERS)
    #print('test 2')
    result = []
    if reponse.status_code == 200:
        #print('test request reçu')
        soup = BeautifulSoup(reponse.text, 'html.parser')
        section = soup.find_all('section', class_='text-block')
        for sec in section:
            #print('test3\n'+sec.text)
            if 'INFORMATIONS SUR LES TRANSPORTS' in sec.text:
                #print('test information trans')
                p = sec.find('p')
                p = p.text
                contient_donne = True
                while contient_donne == True:
                    #print('test contient <<')
                    if p.find('«') != -1 and p.find(')') != -1:
                        ligne = p[p.find('«'):p.find(')')+1]
                        p = p.replace(ligne, "")
                        if ", " in ligne[ligne.find('(')+1:ligne.find(')')]:
                            tmp = ligne[ligne.find('(')+1:ligne.find(')')].split(', ')
                        else:
                            tmp = [ligne[ligne.find('(')+1:ligne.find(')')]]
                        temp = {"name": ligne[ligne.find("«")+2:ligne.find("»")-1], "number": tmp}
                        print(temp)
                        result.append(temp)
                    else:
                        contient_donne = False      
    #print(result)
    return result

recup_url_transp(url_tmp)
test = "https://olympics.com/fr/paris-2024/sites/la-concorde"
#recup_transp(test)
#recup_transp_v2(test)