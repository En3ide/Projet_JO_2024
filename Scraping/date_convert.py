import re
from datetime import datetime
from dateutil import parser

mois_fr = [
    'janvier',
    'février',
    'mars',
    'avril',
    'mai',
    'juin',
    'juillet',
    'août',
    'septembre',
    'octobre',
    'novembre',
    'décembre'
]
mois_en = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def date_convert(chaine):
    print(chaine)
    attr_creation_date = "NULL"
    if chaine != None:
        if len(chaine) > 15:
            attr_creation_date = re.search(r'\d{4}', chaine).group() + "-00-00"
        elif len(chaine) > 10:
            date_obj = str(str(chaine).lower())
            if len(date_obj.split()) == 3:
                for a in range(1,12):
                        date_obj = date_obj.replace(mois_fr[a], mois_en[a])
                print(date_obj)
                date_obj = datetime.strptime(date_obj, "%d %B %Y")
                date_obj = date_obj.strftime("%Y-%m-%d")
            else:
                for a in range(1,12):
                    date_obj = date_obj.replace(mois_fr[a], mois_en[a])
                print(date_obj)
                date_obj = datetime.strptime(date_obj, "%B %Y")
                date_obj = date_obj.strftime("00-%m-%d")
            attr_creation_date = date_obj
        elif len(chaine) < 6:
            attr_creation_date = chaine.replace(" ", "") + "-00-00"
        elif len(chaine) <10:
            date_obj = chaine.replace(" ", "").split("-")
            attr_creation_date = chaine + "-00-00" 
    return attr_creation_date

months = {
    "janvier": "01",
    "février": "02",
    "mars": "03",
    "avril": "04",
    "mai": "05",
    "juin": "06",
    "juillet": "07",
    "août": "08",
    "septembre": "09",
    "octobre": "10",
    "novembre": "11",
    "décembre": "12",

    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12"
}

def retirer_mois(chaine):
    chaine_lower = chaine.lower()
    for month_name, month_number in months.items():
        chaine_lower = chaine_lower.replace(month_name, month_number)
    chaine_cleaned = re.sub(r'(?<!\d)[^\d]+(?!\d)', ' ', chaine_lower)
    
    return chaine_cleaned


def convert_date(input_date):
    try:
        # Vérifier si la chaîne de date est 'None'
        if input_date.lower() == 'none':
            return None
        
        # Remplacer les noms de mois par les chiffres correspondants
        for month_name, month_number in months.items():
            input_date = input_date.replace(month_name, month_number)
        
        # Supprimer toutes les lettres de la chaîne
        input_date = ''.join(filter(str.isdigit, input_date))

        # Analyser la date en utilisant la bibliothèque dateutil.parser
        parsed_date = parser.parse(input_date, fuzzy=True)

        # Formater la date en AAAA/MM/JJ
        formatted_date = parsed_date.strftime("%Y/%m/%d")
        return formatted_date
    except Exception as e:
        print(f"Erreur lors de la conversion de la date : {e}")
        return None

print(retirer_mois('2024 (JOP)juillet 2025 (grand public)'))