<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");

// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}
if ($_GET['1'] == "") {
    $_GET['1'] = "%%";
}
if ($_GET['3'] == "") {
    $_GET['3'] = "%%";
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT * FROM Date_calendar WHERE id_date_cal LIKE '" . $_GET['1'] . "' AND
date_cal LIKE '%" . $_GET['2'] . "%' AND
medal_ceremony_date_cal LIKE '" . $_GET['3'] . "';";
$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des Dates</h2>
<nav id="filter-nav">
    <ul>
        <li>ID :<input type="text" class="id table-input" id="1"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="4"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="5"></li>
        <li>Date :<input type="date" class="date table-input" id="2"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="6"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="7"></li>
        <li>Cérémony :
            <select class="ceremony table-input" id="3">
                <option value=""></option>
                <option value="1">Oui</option>
                <option value="0">Non</option>
            </select>
        </li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="8"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="9"></li>
    </ul>
</nav>
<button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
<table id="table-donnee">
    <tbody>
        <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Cérémony</th>
        </tr>
        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_date_cal'] . "</td>";
                echo "<td>" . $row['date_cal'] . "</td>";
                echo "<td>" . (($row['medal_ceremony_date_cal']) ? "OUI" : "NON") . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<p>Aucune Date trouvé dans la base de données.</p>";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </tbody>
</table>