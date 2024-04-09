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
if ($_GET['5'] == "") {
    if ($_GET['6'] == "") {
        // Exécuter la requête pour afficher la liste des tables
        $sql = "SELECT Record.*, Event.*, Athlete.* 
    FROM Record 
    LEFT JOIN Event ON Record.id_event = Event.id_event 
    LEFT JOIN Athlete ON Record.id_athlete = Athlete.id_athlete
    WHERE Record.id_record LIKE '%" . $_GET['1'] . "%' AND
    Record.stat_record LIKE '%" . $_GET['2'] . "%' AND
    Record.date_record LIKE '%" . $_GET['3'] . "%';";
    }
}
/*
if ($_GET['5'] == "") {
    if ($_GET['6'] == "") {
        $name_athlete = "";
    } else {
        $name_athlete = " Athlete.name_athlete LIKE '" . $_GET['6'] . "' AND";
    }
    if ($_GET['7'] == "") {
        $firstname_athlete = "";
    } else {
        $firstname_athlete = " Athlete.firstname_athlete LIKE '%" . $_GET['7'] . "%'";
    }

    // Exécuter la requête pour afficher la liste des tables
    $sql = "SELECT Record.*, Event.*, Athlete.* 
    FROM Record 
    LEFT JOIN Event ON Record.id_event = Event.id_event 
    LEFT JOIN Athlete ON Record.id_athlete = Athlete.id_athlete
    WHERE Record.id_record LIKE '%" . $_GET['1'] . "%' AND
    Record.stat_record LIKE '%" . $_GET['2'] . "%' AND
    Record.date_record LIKE '%" . $_GET['3'] . "%' AND"
        . $name_athlete
        . $firstname_athlete . ";";
}*/

$resultat = mysqli_query($connexion, $sql);
?>
<h2>Tableau des Records</h2>
<nav id="filter-nav">
    <ul>
        <li>ID :<input value="" type="text" class="table-input" id="1"></li>
        <li>Statistique :<input value="" type="text" class="genre table-input" id="2"></li>
        <li>Date : <input value="" type="date" class="table-input" id="3"></li>
        <li>Discipline :<input value="" type="text" style="display: none;" class="table-input" id="4"></li>
        <li>Épreuve :<input value="" type="text" class="table-input" id="5"></li>
        <li>Athlète Prenom :<input value="" type="text" class="table-input" id="7"></li>
        <li>Athlète Nom :<input value="" type="text" class="table-input" id="6"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="8"></li>
        <li><input value="" type="text" style="display:none;" class="table-input" id="9"></li>
    </ul>
</nav>
<button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
<table id="table-donnee">
    <tbody>
        <tr>
            <th>Id</th>
            <th>Statistique</th>
            <th>Date</th>
            <!--<th>Discipline</th>-->
            <th>Épreuve</th>
            <th>Nom athlète</th>
            <th>Prénom athlète</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_record'] . "</td>";
                echo "<td>" . $row['stat_record'] . "</td>";
                echo "<td>" . $row['date_record'] . "</td>";
                echo "<td>" . $row['name_event'] . "</td>";
                echo "<td>" . $row['name_athlete'] . "</td>";
                echo "<td>" . $row['firstname_athlete'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<p>Aucun Record trouvé dans la base de données.</p>";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
    </tbody>
</table>