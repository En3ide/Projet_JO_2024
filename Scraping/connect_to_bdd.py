import mysql.connector

def se_connecter_mysql(adresse_ip, utilisateur, mot_de_passe, nom_base_donnees):
    """
    Fonction pour se connecter à une base de données MySQL en utilisant une adresse IP.
    
    Args:
        adresse_ip (str): Adresse IP du serveur MySQL.
        utilisateur (str): Nom d'utilisateur pour se connecter à la base de données.
        mot_de_passe (str): Mot de passe pour se connecter à la base de données.
        nom_base_donnees (str): Nom de la base de données à laquelle se connecter.

    Returns:
        mysql.connector.connection.MySQLConnection: Objet de connexion à la base de données MySQL.
    """
    try:
        # Connexion à la base de données MySQL
        connexion = mysql.connector.connect(
            host=adresse_ip,
            user=utilisateur,
            password=mot_de_passe,
            database=nom_base_donnees
        )

        if connexion.is_connected():
            print("Connecté à la base de données MySQL")

        return connexion

    except mysql.connector.Error as erreur:
        print("Erreur lors de la connexion à la base de données MySQL :", erreur)
        return None
    
def execute_sql(connexion, requete_sql):
    """
    Fonction pour exécuter une requête SQL sur une connexion à une base de données MySQL.
    
    Args:
        connexion (mysql.connector.connection.MySQLConnection): Objet de connexion à la base de données MySQL.
        requete_sql (str): Requête SQL à exécuter.

    Returns:
        None
    """
    try:
        # Création d'un objet curseur pour exécuter des requêtes SQL
        curseur = connexion.cursor()

        # Exécution de la requête SQL
        curseur.execute(requete_sql)

        # Si la requête modifie les données de la base de données, vous devez appeler commit() pour valider les modifications
        connexion.commit()

        print("Requête SQL exécutée avec succès")

    except mysql.connector.Error as erreur:
        print("Erreur lors de l'exécution de la requête SQL :", erreur)

# Exemple d'utilisation de la fonction
# connexion = se_connecter_mysql("adresse_ip", "utilisateur", "mot_de_passe", "nom_base_donnees")
# requete_sql = "INSERT INTO ma_table (colonne1, colonne2) VALUES ('valeur1', 'valeur2');"
# executer_requete_sql(connexion, requete_sql)