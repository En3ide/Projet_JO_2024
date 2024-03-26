<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");

// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT * FROM Athlete";
$resultat = mysqli_query($connexion, $sql);
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
            <th>Prenom</th>
            <th>Date de Naissance</th>
            <th>Genre</th>
            <th>Code country</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat) {
            // Afficher les noms des tables
            echo "Liste des tables dans la base de données :<br>";
            echo "<tr>";
            foreach (mysqli_fetch_row($resultat) as $i) {
                echo "<td>" . $i . "</td>";
            }
            echo "</tr>";
        } else {
            echo "Erreur lors de l'exécution de la requête : " . mysqli_error($connexion);
        }

        // Fermer la connexion à la base de données
        mysqli_close($connexion); ?>
    </table>

</body>

</html>