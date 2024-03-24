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
                for sec in p.text.split('),'):
                    print(sec)
                    if 'gare' in sec:
                        if ", " in sec:
                            tmp = sec[sec.find('(')+1:].split(", ")
                        else:
                            tmp = [sec[sec.find('(')+1:].replace(")", "").replace(".", "")]
                        result.append({"type": "gare",
                                       "name" : sec[sec.find('«')+2:sec.find('»')-1],
                                       "number":  tmp})
                    if 'station' in sec:
                        if ", " in sec:
                            tmp = sec[sec.find('(')+1:].replace(")", "").replace(".", "").split(", ")
                        else:
                            tmp = [sec[sec.find('(')+1:].replace(")", "").replace(".", "")]
                        result.append({"type": "station",
                                       "name": sec[sec.find('«')+2:sec.find('»')-1],
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
                print('test information trans')
                secs = sec.find_all('p')
                for sec in secs:
                    print("sec = "+ sec.text)
                    if "» (" in str(sec):
                        print("sec = "+sec.text)
                        sec = sec.text
                        tmp = ""
                        contient_donne = True
                        while contient_donne == True:
                            #print('test contient <<')
                            if sec.find("» (") != -1:
                                sec = sec.replace(sec[:-sec[::-1].find("«")-1], "")
                                tmp = sec[sec.find("«")+2:sec.find("»")-1]
                                tmp2 = sec[sec.find("» (")+3:sec.find(")")]
                                if ", " in tmp2:
                                    tmp2 = tmp2.split(", ")
                                else:
                                    tmp2 = [tmp2]
                                temp = {"name": tmp, "number": tmp2}
                                print(temp)
                                result.append(temp)
                                sec = sec.replace(sec[sec.find("«")+2:sec.find(")")-1], "")
                            else:
                                contient_donne = False    
    print(result)
    return result

def recup_transp_v3(url):
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
            ensemble = ""
            if 'INFORMATIONS SUR LES TRANSPORTS' in sec.text:
                if "li" in str(sec):
                    lis = sec.find_all('li')
                    if lis != []:
                        for li in lis:
                            ensemble += li.text
                        print(ensemble)
                print('test information trans')
                ensemble += sec.text
                ensemble = ensemble.replace("\n", "")
                print("Debut : \n"+ensemble+"\nFin")
                if "» (" in ensemble:
                    #print("sec = "+sec.text)
                    tmp, tmp2 = "",""
                    contient_donne = True
                    while contient_donne == True:
                        #print('test contient <<')
                        if ensemble.find("» (") != -1:
                            print(ensemble)
                            ensemble = ensemble.replace(ensemble[:-ensemble[::-1].find("«")-1], "")
                            tmp = ensemble[ensemble.find("«")+2:ensemble.find("»")-1]
                            tmp2 = ensemble[ensemble.find("» (")+3:ensemble.find(")")]
                            if ", " in tmp2:
                                tmp2 = tmp2.split(", ")
                            else:
                                tmp2 = [tmp2]
                            temp = {"name": tmp, "number": tmp2}
                            print(temp)
                            result.append(temp)
                            ensemble = ensemble.replace(ensemble[ensemble.find("«")+2:ensemble.find(")")-1], "")
                        else:
                            contient_donne = False
    print("\n\n"+str(result))
    return result

#recup_url_transp(url_tmp)
test = "https://olympics.com/fr/paris-2024/sites/parc-des-princes"
#recup_transp(test)
#recup_transp_v2(test)
recup_transp_v3(test)
"""chaine = "Les 27, 28 et 30 juillet 2024, une ligne de bus « Paris 2024 » directe et dédié aux spectateurs sera mise en place depuis la station « Charles-de-Gaulle – Etoile » (RER A, Métro 1, Métro 2, Métro 6)"
chaine = chaine.replace(chaine[:-chaine[::-1].find("«")-1], "")
print(chaine)
print(chaine[chaine.find("«")+2:chaine.find("»")-1])
print(chaine[chaine.find("» (")+2:chaine.find(")")+1])"""
