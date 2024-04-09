<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");

// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT * FROM Country";
$resultat = mysqli_query($connexion, $sql);
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau des pays</title>
</head>

<body>

    <h2>Tableau des pays</h2>
    <nav id="filter-nav">
        <ul>
            <li>Code Pays :<input type="text" class="code table-input" id="code_country"></li>
            <li>Nom Pays :<input type="text" class="name table-input" id="name_country"></li>
        </ul>
    </nav>
    <button id="ok-filter-button" onclick="supp_table(document.getElementById('table_donnee'))">Lancer la
        recherche</button>

    <table id="table-donnee">
        <tbody>
            <tr>
                <th>Code pays</th>
                <th>Pays</th>
            </tr>

            <?php
            // Vérifier si la requête a réussi
            if ($resultat && mysqli_num_rows($resultat) > 0) {
                // Afficher les données de chaque athlète
                while ($row = mysqli_fetch_assoc($resultat)) {
                    echo "<tr>";
                    echo "<td>" . $row['code_country'] . "</td>";
                    echo "<td>" . $row['name_country'] . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<p>Aucun pays trouvé dans la base de données.</p>";
            }
            // Fermer la connexion à la base de données
            mysqli_close($connexion);
            ?>
        </tbody>
    </table>

</body>

</html>