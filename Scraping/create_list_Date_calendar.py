from datetime import datetime, timedelta
import sqlite3

def recup_date_dal():
    # Date de début et de fin
    start_date = datetime(2024, 7, 26)
    end_date = datetime(2024, 8, 11)

    # Initialiser la liste de dictionnaires
    date_list = []

    # Remplir la liste de dictionnaires avec des dates
    current_date = start_date

    while current_date <= end_date:
        attr_date_cal = current_date.strftime("%d/%m/%Y")
        attr_medal_cer = False
        date_list.append({"date_cal": attr_date_cal, "medal_ceremony_date_cal": attr_medal_cer})
        current_date += timedelta(days=1)

    return date_list

def send_site(result, bdd=""):
    send = ""
    for i in result:
        send += "INSERT INTO Site (Creation_date, Adress, Capacity, URL_site) VALUES ('"
        + i[0]+ "', '"
        + i[1] + "', "
        + i[2] + ", '"
        + i[3]+"');"
    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.close()
        curseur.execute(send)
        connexion.close()
        connexion.commit()
    return(send)


# Afficher le résultat de la fonction
print(recup_date_dal())
