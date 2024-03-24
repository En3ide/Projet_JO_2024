###################
# Script de scraping table Transport
###################

##### Import #####
import sqlite3

##### Code #####
list_transport = ['TRAIN', 'TRAMWAY', 'BUS', 'METRO']

def recup_transport():
    result = []
    for transport in list_transport:
        result.append({"name_trans": transport})
    return result

def send_transport(result, bdd=""):

    # Création de la requête SQL
    send = "INSERT INTO Transport (name_trans) VALUES\n"
    for dic in result:
        send += "('" + dic.get("name_trans") + "'),\n"
    send = send[:-2] + ";"

    if len(bdd) > 0:
        connexion = sqlite3.connect(bdd)
        curseur = connexion.cursor()
        curseur.execute(send)
        connexion.commit()
        curseur.close()
        connexion.close()

    return(send)

if __name__ == "__main__":
    print(send_transport(recup_transport()))