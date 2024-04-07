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
$sql = "SELECT To_Serve.*, Site.*, Transport.* 
        FROM To_Serve 
        JOIN Site ON To_Serve.id_site = Site.id_site 
        JOIN Transport ON To_Serve.id_trans = Transport.id_trans 
        WHERE To_Serve.id_site LIKE '" . $_GET['1'] . "' 
        AND Site.name_site LIKE '%" . $_GET['2'] . "%' 
        AND Transport.id_trans LIKE '%" . $_GET['3'] . "%' 
        AND Transport.name_trans LIKE '%" . $_GET['4'] . "%' 
        AND To_Serve.num_ligne LIKE '%" . $_GET['5'] . "%' 
        AND To_Serve.station_name LIKE '%" . $_GET['6'] . "%';";

$resultat = mysqli_query($connexion, $sql);
?>

<body>
    <h2>Tableau des sites déservie</h2>
    <nav id="filter-nav">
        <ul>
            <li>ID Site :<input type="text" class="id table-input" id="1"></li>
            <li>Nom Site :<input type="text" class="id table-input" id="2"></li>
            <li>ID transport :<input type="text" class="id_transport table-input" id="3"></li>
            <li>Type transport :<input type="text" class="id_transport table-input" id="4"></li>
            <li>Numero de ligne :<input type="text" class="id_transport table-input" id="5"></li>
            <li>Nom de station :<input type="text" class="station_name table-input" id="6"></li>
            <li><input value="" type="text" style="display:none;" class="table-input" id="7"></li>
            <li><input value="" type="text" style="display:none;" class="table-input" id="8"></li>
            <li><input value="" type="text" style="display:none;" class="table-input" id="9"></li>
        </ul>
    </nav>
    <button id="ok-filter-button" onclick="supp_table()">Lancer la recherche</button>
    <table id="table-donnee">
        <tbody></tbody>
        <tr>
            <th>Id Site</th>
            <th>Nom Site</th>
            <th>Id Transport</th>
            <th>Type Transport</th>
            <th>Numero de ligne</th>
            <th>Nom de station</th>
        </tr>

        <?php
        // Vérifier si la requête a réussi
        if ($resultat && mysqli_num_rows($resultat) > 0) {
            // Afficher les données de chaque athlète
            while ($row = mysqli_fetch_assoc($resultat)) {
                echo "<tr>";
                echo "<td>" . $row['id_site'] . "</td>";
                echo "<td>" . $row['name_site'] . "</td>";
                echo "<td>" . $row['id_trans'] . "</td>";
                echo "<td>" . $row['name_trans'] . "</td>";
                echo "<td>" . $row['num_ligne'] . "</td>";
                echo "<td>" . $row['station_name'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "Aucun pays trouvé dans la base de données.";
        }
        // Fermer la connexion à la base de données
        mysqli_close($connexion);
        ?>
        </tbody>
    </table>

</body>

</html>