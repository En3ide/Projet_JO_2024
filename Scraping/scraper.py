import importlib
import subprocess
import requests
import html2text
from bs4 import BeautifulSoup

def get_calendar_url():
    main_url = "https://www.paris2024.org/fr/calendrier-sports-olympiques/"

    # Récupérer le contenu de la page web
    response = requests.get(main_url)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver la balise <a> qui contient le lien
        a_tag = soup.find('a', class_='b-button')

        # Vérifier si la balise <a> a été trouvée
        if a_tag:
            # Récupérer l'URL (href)
            href = a_tag.get('href')
            
            if href:
                print(f"L'URL récupérée est : {href}")
                return href
            else:
                print("La balise <a> n'a pas d'attribut href.")
        else:
            print("Balise <a> non trouvée.")
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")

def get_text_from_html(url):
    # Récupérer le contenu de la page web
    response = requests.get(url)
    
    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Configurez html2text pour ne pas ajouter de nouvelles lignes après chaque balise
        h = html2text.HTML2Text()
        h.body_width = 0  # Désactiver la coupe de texte
        h.single_line_break = True  # Utiliser une seule ligne pour les sauts de ligne

        # Convertir le HTML en texte brut avec la mise en forme
        text_content = h.handle(response.text)
        
        text_content = text_content.replace("l", "")
        
        return text_content
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}")
        return None

def create_txt(url):
    # Exemple d'utilisation avec l'URL de la page
    text_content = get_text_from_html(url)

    if text_content:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text_content)
        print("Le contenu a été enregistré dans le fichier 'output.txt'.")