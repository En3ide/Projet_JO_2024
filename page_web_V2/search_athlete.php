<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");

// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}

// Exécuter la requête pour afficher la liste des tables
//$sql = "SELECT * FROM Athlete";
$sql = "SELECT * FROM Date_calendar
WHERE Date_calendar.id_date_cal LIKE " . $_GET['id_date_cal'] . " AND
Date_calendar.date_cal LIKE '%" . $_GET['date_cal'] . "%' AND
name_country LIKE '%" . $_GET['medal_ceremony_date_cal'] . "%';";
$resultat = mysqli_query($connexion, $sql);
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

<body>
    <?php
    // Vérifier si la requête a réussi
    if ($resultat && mysqli_num_rows($resultat) > 0) {
        // Afficher les données de chaque athlète
        while ($row = mysqli_fetch_assoc($resultat)) {
            echo "<tr>";
            echo "<td>" . $row['id_date_cal'] . "</td>";
            echo "<td>" . $row['date_cal'] . "</td>";
            echo "<td>" . $row['medal_ceremony_date_cal'] . "</td>";
            echo "</tr>";
        }
    } else {
        echo "Aucun athlète trouvé dans la base de données.";
    }
    // Fermer la connexion à la base de données
    mysqli_close($connexion);
    ?>
</body>

</html>