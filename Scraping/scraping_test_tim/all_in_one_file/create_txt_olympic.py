import importlib
import subprocess

# Vérifier si le module requests est installé
try:
    importlib.import_module('requests')
    print(f"Le module requests est déjà installé.")
except ImportError:
    print("Le module 'requests' n'est pas installé. Installation en cours...")
    subprocess.run(['pip', 'install', 'requests'])

# Vérifier si le module html2text est installé
try:
    importlib.import_module('html2text')
    print(f"Le module html2text est déjà installé.")
except ImportError:
    print("Le module 'html2text' n'est pas installé. Installation en cours...")
    subprocess.run(['pip', 'install', 'html2text'])
    
# Vérifier si le module bs4 est installé
try:
    importlib.import_module('bs4')
    print(f"Le module bs4 est déjà installé.")
except ImportError:
    print("Le module 'bs4' n'est pas installé. Installation en cours...")
    subprocess.run(['pip', 'install', 'bs4'])

import requests
import html2text
from bs4 import BeautifulSoup

main_url = "https://www.paris2024.org/fr/calendrier-sports-olympiques/"

def get_calendar_url():
    main_url = "https://www.paris2024.org/fr/calendrier-sports-olympiques/"
    search_url = "calendrier-sports-olympique"

    # Récupérer le contenu de la page web
    response = requests.get(main_url)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tag = [a for a in soup.find_all('a', href=True) if search_url in a.get('href')][0]

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
    url = url
    text_content = get_text_from_html(url)

    if text_content:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text_content)
        print("Le contenu a été enregistré dans le fichier 'output.txt'.")

if __name__ == "__main__":
    create_txt(get_calendar_url())