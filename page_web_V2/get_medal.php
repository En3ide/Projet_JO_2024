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
$sql = "SELECT Medal.*, Event.*, Athlete.*, Date_calendar.*
        FROM Medal
        JOIN Event ON Medal.id_event = Event.id_event 
        JOIN Athlete ON Medal.id_athlete = Athlete.id_athlete 
        JOIN Date_calendar ON Medal.id_date_cal = Date_calendar.id_date_cal 
        WHERE Medal_id_medal LIKE '" . $_GET['1'] . "' 
        AND Medal.type_medal LIKE '%" . $_GET['2'] . "%' 
        AND Medal.id_event LIKE '%" . $_GET['3'] . "%' 
        AND Medal.name_event LIKE '%" . $_GET['4'] . "%' 
        AND Medal.id_athlete LIKE '%" . $_GET['5'] . "%' 
        AND Athlete.name_athlete LIKE '%" . $_GET['6'] . "%' 
        AND Athlete.firstname_athlete LIKE '%" . $_GET['7'] . "%' 
        AND Date.date_cal LIKE '%" . $_GET['8'] . "%';";

$resultat = mysqli_query($connexion, $sql);
?>

<body>
    <h2>Tableau des médailles</h2>
    <nav id="filter-nav">
        <ul>
            <li>ID :<input type="text" class="id table-input" id="1"></li>
            <li>Type :<input type="text" class="id table-input" id="2"></li>
            <li>Date de remise :<input value="" type="text" class="table-input" id="8"></li>
            <li>ID épreuve :<input type="text" class="id table-input" id="3"></li>
            <li>Nom épreuve :<input type="text" class="id_transport table-input" id="4"></li>
            <li>ID athlète :<input type="text" class="id_transport table-input" id="5"></li>
            <li>Prénom athlète :<input type="text" class="station_name table-input" id="7"></li>
            <li>Nom athlète :<input type="text" class="id_transport table-input" id="6"></li>
            <li style="display:none;"><input value="" type="text" class="table-input" id="9"></li>
        </ul>
    </nav>
    <button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
    <table id="table-donnee">
        <tbody></tbody>
        <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Date de remise</th>
            <th>ID épreuve</th>
            <th>Nom épreuve</th>
            <th>ID athlète</th>
            <th>Prénom athlète</th>
            <th>Nom athlète</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_medal'] . "</td>";
                echo "<td>" . $row['type_medal'] . "</td>";
                echo "<td>" . $row['date_cal'] . "</td>";
                echo "<td>" . $row['id_event'] . "</td>";
                echo "<td>" . $row['name_event'] . "</td>";
                echo "<td>" . $row['id_athlete'] . "</td>";
                echo "<td>" . $row['firstname_athlete'] . "</td>";
                echo "<td>" . $row['name_athlete'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<p>Aucune Medaille trouvé dans la base de données.</p>";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
        </tbody>
    </table>

</body>

</html>