import requests

def get_olympic_sports():
    olympic_sports = {}
    # Récupération des sports des Jeux Olympiques
    response = requests.get("https://olympics.com/tokyo-2020/fr/sports/")
    if response.status_code == 200:
        content = response.text
        # Traitement du contenu HTML pour extraire les sports et épreuves
        # Vous pouvez utiliser BeautifulSoup ou d'autres librairies pour cela
        # Voici un exemple minimaliste pour la démonstration
        # Supposons que les données soient stockées dans des balises <div class="sport">
        sports_html = content.split('<div class="sport">')[1:]
        for sport_html in sports_html:
            sport_name = sport_html.split('<h3 class="sport-name">')[1].split('</h3>')[0]
            event_list = []
            events = sport_html.split('<li class="sport-event">')[1:]
            for event in events:
                event_name = event.split('<span class="event-name">')[1].split('</span>')[0]
                event_list.append(event_name)
            olympic_sports[sport_name] = event_list
    return olympic_sports

def get_paralympic_sports():
    paralympic_sports = {}
    # Récupération des sports des Jeux Paralympiques
    response = requests.get("https://www.paralympic.org/fr/sports")
    if response.status_code == 200:
        content = response.text
        # Traitement du contenu HTML pour extraire les sports et épreuves
        # Vous pouvez utiliser BeautifulSoup ou d'autres librairies pour cela
        # Voici un exemple minimaliste pour la démonstration
        # Supposons que les données soient stockées dans des balises <div class="sport">
        sports_html = content.split('<div class="sport">')[1:]
        for sport_html in sports_html:
            sport_name = sport_html.split('<h3 class="sport-name">')[1].split('</h3>')[0]
            event_list = []
            events = sport_html.split('<li class="sport-event">')[1:]
            for event in events:
                event_name = event.split('<span class="event-name">')[1].split('</span>')[0]
                event_list.append(event_name)
            paralympic_sports[sport_name] = event_list
    return paralympic_sports

def main():
    olympic_sports = get_olympic_sports()
    paralympic_sports = get_paralympic_sports()
    print("Sports des Jeux Olympiques:")
    print(olympic_sports)
    print("\nSports des Jeux Paralympiques:")
    print(paralympic_sports)

if __name__ == "__main__":
    main()