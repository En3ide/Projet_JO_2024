<?php

// Paramètres de connexion à la base de données
$serveur = "localhost"; // Adresse du serveur MariaDB
$utilisateur = "mysql"; // Nom d'utilisateur de la base de données
$mot_de_passe = "confirmer"; // Mot de passe de la base de données
$base_de_donnees = "Projet_JO"; // Nom de la base de données

// Connexion à la base de données
$connexion = new mysqli($serveur, $utilisateur, $mot_de_passe, $base_de_donnees);

// Vérifier la connexion
if ($connexion->connect_error) {
    die("Erreur de connexion : " . $connexion->connect_error);
}

// Requête pour récupérer les données de la table "athlete"
$requete = "SELECT * FROM athlete";

// Exécution de la requête
$resultat = $connexion->query($requete);

?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau des Athlètes</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th,
        td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>

    <h2>Tableau des Athlètes</h2>

    <table>
        <tr>
            <th>ID</th>
            <th>Nom</th>
            <th>Pays</th>
        </tr>
        <?php
        // Vérifier si la requête a renvoyé des résultats
        if ($resultat->num_rows > 0) {
            // Parcourir les lignes de résultats
            while ($ligne = $resultat->fetch_assoc()) {
                // Afficher les données de chaque ligne dans un tableau HTML
                echo "<tr>";
                echo "<td>" . $ligne["id"] . "</td>";
                echo "<td>" . $ligne["nom"] . "</td>";
                echo "<td>" . $ligne["pays"] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='3'>Aucun résultat trouvé.</td></tr>";
        }
        ?>
    </table>

</body>

</html>

<?php
// Fermer la connexion à la base de données
$connexion->close();
?>