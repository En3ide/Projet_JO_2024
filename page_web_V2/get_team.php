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
$sql = "SELECT * FROM Team";
$resultat = mysqli_query($connexion, $sql);

$sql = "SELECT Team.*, To_pertain_team.*
        FROM Team JOIN To_pertain_team ON Team.id_team = Team.id_team
        JOIN Athlete ON To_pertain_team.id_athlete = Athlete.id_athlete
        JOIN Country ON Team.code_country = Country.code_country
        WHERE id_team LIKE '" . $_GET['1'] . "' 
        AND size_team LIKE '%" . $_GET['2'] . "%' 
        AND gender_team LIKE '%" . $_GET['3'] . "%' 
        AND To_pertain.id_athlete LIKE '" . $_GET['4'] . "' 
        AND Athlete.name_athlete LIKE '%" . $_GET['5'] . "%' 
        AND Athlete.firstname_athlete LIKE '%" . $_GET['6'] . "%';";
?>

<body>

    <h2>Tableau des Teams</h2>
    <nav id="filter-nav">
        <ul>
            <li>ID Team :<input type="text" class="id table-input" id="1"></li>
            <li>Taille Team :<input type="text" class="id table-input" id="2"></li>
            <li>Genre :<input type="text" class="id_transport table-input" id="3"></li>
            <li>ID Athlete :<input type="text" class="id_transport table-input" id="4"></li>
            <li>Nom Athlete :<input type="text" class="id_transport table-input" id="5"></li>
            <li>Prenom Athlete :<input type="text" class="station_name table-input" id="6"></li>
            <li>Pays :<input value="" type="text" class="table-input" id="7">
            </li>
            <li style="display: none;"><input value="" type="text" style="display:none;" class="table-input" id="8">
            </li>
            <li style="display: none;"><input value="" type="text" style="display:none;" class="table-input" id="9">
            </li>
        </ul>
    </nav>
    <button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
    <table id="table-donnee">
        <tbody>
            <tr>
                <th>ID Team</th>
                <th>Taille team</th>
                <th>Genre de la Team</th>
                <th>ID Athlete</th>
                <th>Nom Athlete</th>
                <th>Prenom Athlete</th>
                <th>pays</th>
            </tr>

            <?php
            // Vérifier si la requête a réussi
            if ($resultat && mysqli_num_rows($resultat) > 0) {
                // Afficher les données de chaque athlète
                while ($row = mysqli_fetch_assoc($resultat)) {
                    echo "<tr>";
                    echo "<td>" . $row['id_team'] . "</td>";
                    echo "<td>" . $row['size_team'] . "</td>";
                    echo "<td>" . $row['gender_team'] . "</td>";
                    echo "<td>" . $row['id_athlete'] . "</td>";
                    echo "<td>" . $row['name_athlete'] . "</td>";
                    echo "<td>" . $row['firstname_athlete'] . "</td>";
                    echo "<td>" . $row['name_country'] . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<p>Aucune Team trouvé dans la base de données.</p>";
            }
            // Fermer la connexion à la base de données
            mysqli_close($connexion);
            ?>
        </tbody>
    </table>

</body>

</html>