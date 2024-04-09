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
if ($_GET['4'] == "") {
    $_GET['4'] = "%%";
}

// Exécuter la requête pour afficher la liste des tables
$sql = "SELECT * FROM Discipline WHERE
id_disc LIKE '" . $_GET['1'] . "' AND
name_fr_disc LIKE '%" . $_GET['2'] . "%' AND
name_an_disc LIKE '%" . $_GET['3'] . "%' AND
category_disc LIKE '" . $_GET['4'] . "';";
$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des disciplines</h2>
<nav id="filter-nav">
    <ul>
        <li>ID :<input type="text" class="table-input" id="1"></li>
        <li>Nom Français :<input type="text" class="table-input" id="2"></li>
        <li>Nom Anglais :<input type="text" class="table-input" id="3"></li>
        <li>Catégorie :
            <select class="table-input" id="4">
                <option value=""></option>
                <option value="OLYMPIC">Olympique</option>
                <option value="PARALYMPIC">Paralympique</option>
            </select>
        </li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="5"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="6"></li>
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
            <th>Nom français</th>
            <th>Nom Anglais</th>
            <th>Catégorie</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_disc'] . "</td>";
                echo "<td>" . ucfirst($row['name_fr_disc']) . "</td>";
                echo "<td>" . ucfirst($row['name_an_disc']) . "</td>";
                echo "<td>" . (($row['category_disc']) == "OLYMPIC" ? "Olympique" : "Paralympique") . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<p>Aucune Discipline trouvé dans la base de données.</p>";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </tbody>
</table>