<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");

// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}

// Vérifiez si les paramètres sont présents dans l'URL
if (isset($_GET['param1'])) {
    // Récupérez les valeurs des paramètres
    $param1 = $_GET['param1'];
    $param2 = $_GET['param2'];
    if ($param1 == "discipline") {
        $sql = "SELECT * FROM Event WHERE name_fr_disc LIKE '%" + $param2 + "%';";
    } elseif ($param1 == "event") {
        $sql = "SELECT * FROM Event WHERE name_event LIKE '%" + $param2 + "%';";
    } elseif ($param1 == "format") {
        $sql = "SELECT * FROM Event WHERE format_event LIKE '%" + $param2 + "%';";
    } elseif ($param1 == "genre") {
        $sql = "SELECT * FROM Event WHERE gender_event LIKE '%" + $param2 + "%';";
    } else {
        $sql = "SELECT * FROM Event WHERE name_event LIKE '%" + $param1 + "%';";
    }

    $resultat = mysqli_query($connexion, $sql);
} else {
    // Exécuter la requête pour afficher la liste des tables
    $sql = "SELECT * FROM Site;";
    $resultat = mysqli_query($connexion, $sql);
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau des Sites</title>
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

    <h2>Tableau des Sites</h2>

    <table class="table_donne">
        <tr>
            <th>Nom site</th>
            <th>Adresse site</th>
            <th>Date de création</th>
            <th>capacité</th>
            <th>URL d'information</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['name_site'] . "</td>";
                echo "<td>" . $row['adress_site'] . "</td>";
                echo "<td>" . $row['creation_date_site'] . "</td>";
                echo "<td>" . $row['capacity_site'] . "</td>";
                echo "<td>" . $row['URL_site'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "Aucun Site trouvé dans la base de données.";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </table>

</body>

</html>