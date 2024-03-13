from datetime import datetime, timedelta

def recup_date_dal():
    # Date de début et de fin
    start_date = datetime(2024, 7, 26)
    end_date = datetime(2024, 8, 11)

    # Initialiser la liste de dictionnaires
    date_list = []

    # Remplir la liste de dictionnaires avec des dates
    current_date = start_date

    while current_date <= end_date:
        date_list.append({"date_cal": current_date.strftime("%d/%m/%Y"), "medal_ceremony_date_cal": False})
        current_date += timedelta(days=1)

    return date_list

# Afficher le résultat de la fonction
print(recup_date_dal())
