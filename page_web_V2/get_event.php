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
if ($_GET['4'] == "") {
    $_GET['4'] = "%%";
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT Event.*, Discipline.* FROM Event JOIN Discipline ON Event.id_disc = Discipline.id_disc WHERE
Event.id_event LIKE '" . $_GET['1'] . "' AND
Event.name_event LIKE '%" . $_GET['2'] . "%' AND
Event.format_event LIKE '" . $_GET['3'] . "' AND
Event.gender_event LIKE '" . $_GET['4'] . "' AND
Discipline.id_disc LIKE '%" . $_GET['5'] . "%' AND
Discipline.name_fr_disc LIKE '%" . $_GET['6'] . "%';";
$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des épreuves</h2>
<nav id="filter-nav">
    <ul>
        <li>ID :<input type="text" class="id table-input" id="1"></li>
        <li>Nom :<input type="text" class="table-input" id="2"></li>
        <li>Format :
            <select class="table-input" id="3">
                <option value=""></option>
                <option value="INDIVIDUAL">Individuel</option>
                <option value="COLLECTIVE">Collectif</option>
            </select>
        </li>
        <li>Genre :
            <select class="genre table-input" id="4">
                <option value=""></option>
                <option value="MAN">Homme</option>
                <option value="WOMAN">Femme</option>
            </select>
        </li>
        <li>ID discipline :<input type="text" class="table-input" id="5"></li>
        <li>Nom discipline :<input type="text" class="table-input" id="6"></li>
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
            <th>Format</th>
            <th>Genre</th>
            <th>ID discipline</th>
            <th>Nom discipline</th>
        </tr>
        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_event'] . "</td>";
                echo "<td>" . $row['name_event'] . "</td>";
                echo "<td>" . (($row['format_event']) == "INDIVIDUAL" ? "Individuel" : "Collectif") . "</td>";
                echo "<td>" . (($row['gender_event']) == "MAN" ? "Homme" : "Femme") . "</td>";
                echo "<td>" . $row['id_disc'] . "</td>";
                echo "<td>" . ucfirst($row['name_fr_disc']) . "</td>";
                echo "</tr>";
            }
        } else {
            echo "Aucune Epreuve trouvé dans la base de données.";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </tbody>
</table>