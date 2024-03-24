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
                    print(recup_transp(href))
                    if len(recup_transp(href)) >= 1:
                        result.append({"name_site": href.split("/")[-1].replace("-", " "), "transport": recup_transp(href)})
        print("Fini !!!")
    else:
        #print(reponse.status_code)
        print('Fini !!!')
        return([])


def recup_transp(url):
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
                if "li" in str(sec):
                    lis = sec.find_all('li')
                    if lis != []:
                        for li in lis:
                            result.extend(recup_info(li))
                secs = sec.find_all('p')
                for sec in secs:
                    result.extend(recup_info(sec))
    #print(result)
    return result

def recup_info(sec):
    result = []
    temp = dict
    if "» (" in str(sec):
        #print("sec = "+sec.text)
        sec = sec.text
        #sec = sec.replace(sec[sec.find(") (")+2:sec.find(") (")+sec.find(")")], "")
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
                result.append(temp)
                sec = sec.replace(sec[sec.find("«")+2:sec.find(")")-1], "")
            else:
                contient_donne = False
    return result

def send_country(result, bdd=""):
    
    # Création de la requête SQL
    send = "INSERT INTO To_Serve (id_site, id_trans, num_ligne) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("code_country") + "', '" +
            dic.get("name_country") + "'),\n")
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    print(send)
    return(send)

recup_url_transp(url_tmp)