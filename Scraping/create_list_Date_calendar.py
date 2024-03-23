from datetime import datetime, timedelta
import sqlite3

def recup_date_cal():
    # Date de début et de fin
    start_date = datetime(2024, 7, 26)
    end_date = datetime(2024, 8, 11)

    # Initialiser la liste de dictionnaires
    date_list = []

    # Remplir la liste de dictionnaires avec des dates
    current_date = start_date

    while current_date <= end_date:
        attr_date_cal = current_date.strftime("%d/%m/%Y")
        attr_medal_cer = str(False)
        date_list.append({"date_cal": attr_date_cal, "medal_ceremony_date_cal": attr_medal_cer})
        current_date += timedelta(days=1)

    return date_list


def send_site(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Date_calendar_table (date_cal, medal_ceremony_date_cal) VALUES\n"
    for dic in result:
        send += ("('" + dic.get("date_cal") + "', '" +
            dic.get("medal_ceremony_date_cal") + "'),\n")
    send += send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()
    return(send)

if __name__ == "__main__":
    print(send_site(recup_date_cal()))