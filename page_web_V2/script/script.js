/**
Documentation générale :

Ce fichier JavaScript contient des fonctions pour récupérer des données à partir d'une API en utilisant Fetch, et des fonctions pour afficher ces données sur une page web. 
Il comprend également une fonction d'initialisation qui attache des gestionnaires d'événements à des boutons et à un champ de recherche.

VARIABLES NODES :
-----------------
- btn_athlete : Bouton pour afficher les informations d'un athlète.
- btn_event : Bouton pour afficher les informations d'un événement.
- btn_country : Bouton pour afficher les informations d'un pays.
- btn_date : Bouton pour afficher les informations d'une date.
- btn_discipline : Bouton pour afficher les informations d'une discipline.
- btn_site : Bouton pour afficher les informations d'un site.
- btn_record : Bouton pour afficher les informations d'un record.
- search_input : Champ de recherche pour filtrer les informations.

FONCTION recup_info(url, contentElement) :
-------------------------------------------
Cette fonction utilise Fetch pour récupérer le contenu d'une page à partir de l'URL spécifiée. 
Elle met ensuite à jour le contenu de l'élément DOM spécifié avec le contenu récupéré.

FONCTION display_entity(entity, filtre = "") :
----------------------------------------------
Cette fonction prend en paramètre le nom de l'entité à afficher (tel que "athlete", "country", etc.) et éventuellement un filtre. 
Elle construit l'URL appropriée en fonction de l'entité et du filtre, puis appelle la fonction recup_info pour récupérer et afficher les informations.

FONCTIONS display_athlete, display_country, display_event, display_discipline, display_date, display_site, display_record :
-----------------------------------------------------------------------------------------------------------------------
Ces fonctions sont des raccourcis pour afficher les informations spécifiques à une entité sans avoir à spécifier le nom de l'entité à chaque fois. 
Elles appellent simplement la fonction display_entity avec le nom approprié de l'entité.

FONCTION init() :
-----------------
Cette fonction d'initialisation est appelée lorsque le DOM est entièrement chargé. 
Elle attache des gestionnaires d'événements aux boutons pour afficher les informations correspondantes lorsqu'ils sont cliqués. 
De plus, elle attache un gestionnaire d'événements au champ de recherche pour afficher les informations d'événement lorsqu'une touche "Entrée" est pressée.

ÉVÉNEMENT DOMContentLoaded :
----------------------------
Cet événement est écouté pour appeler la fonction d'initialisation init() une fois que le DOM est entièrement chargé.
**/

// FONCTIONS
/*
FONCTION recup_info(url, contentElement) :
Cette fonction utilise Fetch pour récupérer le contenu d'une page à partir de l'URL spécifiée. 
Elle met ensuite à jour le contenu de l'élément DOM spécifié avec le contenu récupéré.
*/
function recup_info(url, contentElement) {
    // Utiliser Fetch pour récupérer le contenu de la page
    fetch(url)
        .then(response => {
            // Vérifier si la requête a réussi (code de statut 200)
            if (!response.ok) {
                throw new Error('La requête a échoué');
            }
            // Extraire le contenu texte de la réponse
            return response.text();
        })
        .then(data => {
            // Ajouter le contenu à l'élément "content"
            contentElement.innerHTML = data;
        })
        .catch(error => {
            console.error('Une erreur est survenue lors de la récupération du contenu :', error);
        });
}

/*
FONCTION display_entity(entity, filtre = "") :
Cette fonction prend en paramètre le nom de l'entité à afficher (tel que "athlete", "country", etc.) et éventuellement un filtre. 
Elle construit l'URL appropriée en fonction de l'entité et du filtre, puis appelle la fonction recup_info pour récupérer et afficher les informations.
*/
function display_entity(entity, filtre = "") {
    var contentElement = document.getElementById("content");
    var root = window.location.href;
    if (root.includes(".php") || root.includes(".html")) {
        var segments = root.split("/"); // Divise l'URL en segments
        segments.pop(); // Supprime le dernier segment (le nom du fichier)
        root = segments.join("/"); // Réassemble les segments en une seule chaîne avec des "/"
    }
    var url = root + "/get_" + entity + ".php";

    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            url += "?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    recup_info(url, contentElement);
}
// INIT
/*
FONCTION init() :
Cette fonction d'initialisation est appelée lorsque le DOM est entièrement chargé. 
Elle attache des gestionnaires d'événements aux boutons pour afficher les informations correspondantes lorsqu'ils sont cliqués. 
De plus, elle attache un gestionnaire d'événements au champ de recherche pour afficher les informations d'événement lorsqu'une touche "Entrée" est pressée.
*/
function init() {
    var contentElement = document.getElementById("content");
    // LA CULOTTE A COLETTE
    var search_input = document.getElementById("search_input");
    search_input.addEventListener("input", function (event) {
        display_entity(search_input.value);
    });
}
// Écouteur d'événement DOMContentLoaded...
window.addEventListener("DOMContentLoaded", init);