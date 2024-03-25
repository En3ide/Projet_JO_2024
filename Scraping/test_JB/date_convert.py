###################
# Script de trouver et formater une date (AAAA-MM-JJ) dans une chaîne bizarre
###################

##### Import #####
import re
from datetime import datetime

##### Code #####
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
            date_obj = str(str(chaine).lower()).replace("1er", "1")
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

def trouver_dates(chaine):
    pattern = r'\b(\d{1,4}[-/]\d{1,2}[-/]\d{1,2})\b|\b(\d{1,2}\s?\d{0,2}\s?\d{2,4})\b'
    dates = re.findall(pattern, chaine)
    return [date for groups in dates for date in groups if date]

def retirer_mois(chaine):
    chaine_lower = chaine.lower()
    for month_name, month_number in months.items():
        chaine_lower = chaine_lower.replace(month_name, month_number)

    segments = re.split(r'[\(\)]', chaine_lower)
    extracted_dates = []
    for segment in segments:
        dates = trouver_dates(segment)
        if dates:
            extracted_dates.extend(dates)

    if len(extracted_dates) == 1:
        extracted_dates.append('')

    return tuple(extracted_dates)

def convert_in_date_format(chaine):
    parts = chaine.split()
    year = None
    month = None
    day = None

    if len(parts) == 1:
        year = parts[0]
    elif len(parts) == 3:
        day, month, year = parts
    elif len(parts) == 2:  # Ajout d'une condition pour gérer le cas de deux parties
        month, year = parts

    if year:
        year = year.zfill(4)
    if month:
        month = month.zfill(2)
    if day:
        day = day.zfill(2)

    return f"{year}-{month or '00'}-{day or '00'}"

def convert_date(date):
    rep = "NULL"
    if date is not None:
        premiere_date = retirer_mois(date)[0]
        premiere_date = re.sub(r"(?<=\b)(\d\s)", lambda match: "0" + match.group(1), premiere_date.strip())
        if premiere_date:
            rep = convert_in_date_format(premiere_date)
            #print(date, " -> ", premiere_date, " : ", rep)
    return rep



# convert_date('2024 (JOP)juillet 2025 (grand public)')
# convert_date("01 janvier 2024 07 octobre 2024")
# convert_date('2024')
# convert_date('3 juillet 2025 (grand public)')
# convert_date('juillet 2025')