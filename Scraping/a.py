from bs4 import BeautifulSoup
import requests
import html2text

main_url = "https://www.paris2024.org/fr/calendrier-sports-olympiques/"
response = requests.get(main_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver le contenu HTML de la page
    content = soup.find('div', class_='content')

    # Convertir le contenu HTML en texte brut avec html2text
    text_content = html2text.html2text(str(content))

    # Enregistrez le texte brut dans un fichier
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text_content)

    print("Le contenu a été enregistré dans le fichier 'output.txt'.")
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}.")
