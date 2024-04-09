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
if ($_GET['4'] == "0000-00-00") {
    $date = "creation_date_site LIKE '" . $_GET['4'] . "' AND";
} else {
    $date = "";
}
if ($_GET['5'] == "") {
    $capacity = "";
} else {
    $capacity = " capacity_site LIKE '" . $_GET['5'] . "' AND";
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT * FROM Site WHERE
Site.id_site LIKE '" . $_GET['1'] . "' AND
Site.name_site LIKE '%" . $_GET['2'] . "%' AND
Site.adress_site LIKE '%" . $_GET['3'] . "%' AND " . $date . $capacity . " URL_site LIKE '%" . $_GET['6'] . "%';";

$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des sites</h2>
<nav id="filter-nav">
    <ul>
        <li>ID Site :<input type="text" class="id table-input" id="1"></li>
        <li>Nom Site :<input type="text" class="table-input" id="2"></li>
        <li>Adresse site :<input type="text" class="table-input" id="3"></li>
        <li>Date création :<input type="date" class="table-input" id="4"></li>
        <li>Capacité :<input type="text" class="genre table-input" id="5"></li>
        <li>URL :<input type="text" class="table-input" id="6"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="7"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="8"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="9"></li>
    </ul>
</nav>
<button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
<table id="table-donnee">
    <tbody>
        <tr>
            <th>ID</th>
            <th>Nom</th>
            <th>Adresse</th>
            <th>Date de création</th>
            <th>Capacité</th>
            <th>Site internet</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_site'] . "</td>";
                echo "<td>" . $row['name_site'] . "</td>";
                echo "<td>" . $row['adress_site'] . "</td>";
                echo "<td>" . (!empty($row['creation_date_site']) ? $row['creation_date_site'] : "Inconnu") . "</td>";
                echo "<td>" . (!empty($row['capacity_site']) ? $row['capacity_site'] : "Inconnu") . "</td>";
                echo '<td><a href="' . $row['URL_site'] . '" target="_blank">' . $row['URL_site'] . '</a></td>';
                echo "</tr>";
            }
        } else {
            echo "<p>Aucun Site trouvé dans la base de données.</p>";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </tbody>
</table>