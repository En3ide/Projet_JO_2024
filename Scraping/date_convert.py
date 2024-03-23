import re
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

def date_convert(donne):
    if donne != None:
        if len(donne) > 15:
            attr_creation_date = re.search(r'\d{4}', donne).group() + "-00-00"
        elif len(donne) > 10:
            date_obj = str(str(donne).lower())
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
        elif len(donne) < 6:
            attr_creation_date = donne.replace(" ", "") + "-00-00"
        elif len(donne) <10:
            date_obj = donne.replace(" ", "").split("-")
            attr_creation_date = donne + "-00-00"
    else:
        attr_creation_date = "NULL"
    return attr_creation_date

print(date_convert('15 june 2008'))