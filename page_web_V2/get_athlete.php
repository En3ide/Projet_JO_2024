<?php

// Connexion à la base de données MySQL
$connexion = mysqli_connect("localhost", "mysql", "confirmer", "Projet_JO");
$_genre = "";


// Vérifier la connexion
if ($connexion === false) {
    die("Erreur de connexion : " . mysqli_connect_error());
}
if ($_GET['1'] == "") {
    $_GET['1'] = "%%";
}
if ($_GET['5'] == "") {
    $_GET['5'] = "%%";
}

// Exécuter la requête pour afficher la liste des tables
//$sql = "SELECT * FROM Athlete";
$sql = "SELECT Athlete.*, Country.* 
FROM Athlete 
JOIN Country ON Athlete.code_country = Country.code_country
WHERE Athlete.id_athlete LIKE '" . $_GET['1'] . "' AND 
Athlete.firstname_athlete LIKE '%" . $_GET['2'] . "%' AND 
Athlete.name_athlete LIKE '%" . $_GET['3'] . "%' AND 
Athlete.birthday_athlete LIKE '%" . $_GET['4'] . "%' AND 
Athlete.gender_athlete LIKE '" . $_GET['5'] . "' AND 
Country.name_country LIKE '%" . $_GET['6'] . "%';";

$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des athlètes</h2>
<nav id="filter-nav">
    <ul>
        <li><input value="athlete" type="text" style="display: none;" class="id table-input" id="0"></li>
        <li>ID :<input value="" type="text" class="id table-input" id="1"></li>
        <li>Prénom :<input value="" type="text" class="table-input" id="2"></li>
        <li>Nom :<input value="" type="text" class="table-input" id="3"></li>
        <li>Année de Naissance :<input value="" type="date" class="table-input" id="4"></li>
        <li>Genre :
            <select value="" class="genre table-input" id="5">
                <option value=""></option>
                <option value="MAN">Homme</option>
                <option value="WOMAN">Femme</option>
            </select>
        </li>
        <li>Pays :<input type="text" class="table-input" id="6"></li>
        <li style="display:none;"><input style="display:none;" class="table-input" id="7"></li>
        <li style="display:none;"><input type="text" style="display:none;" class="table-input" id="8"></li>
        <li style="display:none;"><input value="" type="text" style="display:none;" class="table-input" id="9"></li>
    </ul>
</nav>
<button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
<table id="table-donnee">
    <tbody>
        <tr>
            <th>ID</th>
            <th>Nom</th>
            <th>Prénom</th>
            <th>Date de Naissance</th>
            <th>Genre</th>
            <th>Pays</th>
        </tr>
        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_athlete'] . "</td>";
                echo "<td>" . $row['firstname_athlete'] . "</td>";
                echo "<td>" . $row['name_athlete'] . "</td>";
                echo "<td>" . $row['birthday_athlete'] . "</td>";
                echo "<td>" . (($row['gender_athlete']) == "MAN" ? "Homme" : "Femme") . "</td>";
                echo "<td>" . $row['name_country'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo '<p>Aucun athlète trouvé dans la base de données.</p>';
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);

        ?>
    </tbody>
</table>