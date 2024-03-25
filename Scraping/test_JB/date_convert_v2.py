import re, ast
from datetime import datetime

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
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]

def date_convert_v2(date):
    if date[:date.find(r'\d{4}')]:
        
    date = date.lower()
    result = ""
    tmp = re.search(r'(?<=\s|\D)\d{1,2}(?=\s|\D)', date)
    if tmp:
        result += tmp.group()
    for en, fr in zip(mois_en, mois_fr):
        if fr in date or en in date:
            if tmp and len(tmp.group()) != 0:
                result += " " + en
            else:
                result += en
            break
    tmp = re.search(r'\d{4}', date)
    if tmp:
        tmp = tmp.group()
        if len(tmp) != 0:
            if len(result) != 0:
                result += " " + tmp
            else:
                result += tmp
    return result

date_fr = "juillet 2025 mars 2028 15"
date_convertie = date_convert_v2(date_fr)
print("Date convertie :", date_convertie)