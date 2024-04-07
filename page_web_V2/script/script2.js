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

FONCTIONS display_athlete, display_country, display_event, display_discipline, display_date, display_site, display_record :
-----------------------------------------------------------------------------------------------------------------------
Affiche les informations d'une x table sur la page web.
Ces fonctions récupère les informations d'une x table à partir de la base de données via une requête HTTP et les affiche sur la page web. 
Si un filtre est spécifié, il est utilisé pour filtrer les données du pays selon les critères fournis.

FONCTION init() :
-----------------
Cette fonction d'initialisation est appelée lorsque le DOM est entièrement chargé. 
Elle attache des gestionnaires d'événements aux boutons pour afficher les informations correspondantes lorsqu'ils sont cliqués. 
De plus, elle attache un gestionnaire d'événements au champ de recherche pour afficher les informations d'événement lorsqu'une touche "Entrée" est pressée.

ÉVÉNEMENT DOMContentLoaded :
----------------------------
Cet événement est écouté pour appeler la fonction d'initialisation init() une fois que le DOM est entièrement chargé.
**/


// VARIABLES NODES
// Button
const btn_athlete = document.getElementById("btn_athlete");
const btn_event = document.getElementById("btn_event");
const btn_country = document.getElementById("btn_country");
const btn_date = document.getElementById("btn_date");
const btn_discipline = document.getElementById("btn_discipline");
const btn_site = document.getElementById("btn_site");
const btn_record = document.getElementById("btn_record");
// Input
const search_input = document.getElementById("search-input");


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
FONCTION display_XXX(filtre = "")
Affiche les informations d'une x table sur la page web.
Ces fonctions récupère les informations d'une x table à partir de la base de données via une requête HTTP et les affiche sur la page web. 
Si un filtre est spécifié, il est utilisé pour filtrer les données du pays selon les critères fournis.
*/
function display_athlete(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_athlete.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_athlete.php?param1=" + filtre;
    }
    // Utiliser Fetch pour récupérer le contenu de la page
    recup_info(url, contentElement);
}

function display_country(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_country.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }

    }
    else {
        var url = window.location.href + "/get_country.php?param1=" + filtre;
    }
    recup_info(url, contentElement);
}

function display_event(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_event.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_event.php";
    }
    recup_info(url, contentElement);
}

function display_discipline(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_discipline.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_discipline.php";
    }
    // Utiliser Fetch pour récupérer le contenu de la page
    recup_info(url, contentElement);
}

function display_date(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_date.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_date.php";
    }
    // Utiliser Fetch pour récupérer le contenu de la page
    recup_info(url, contentElement);
}

function display_site(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_site.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_site.php";
    }
    // Utiliser Fetch pour récupérer le contenu de la page
    recup_info(url, contentElement);
}

function display_record(filtre = "") {
    // Récupérer l'élément avec l'ID "content"
    var contentElement = document.getElementById("content");
    // URL de la page à récupérer
    if (filtre.length > 0) {
        if (filtre.includes('=')) {
            filtre = filtre.split('=');
            var url = window.location.href + "/get_record.php?param1=" + filtre[0] + "&param2=" + filtre[1];
        }
    }
    else {
        var url = window.location.href + "/get_record.php";
    }
    // Utiliser Fetch pour récupérer le contenu de la page
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
    btn_athlete.addEventListener("click", function (event) {
        display_athlete();
    });
    btn_event.addEventListener("click", function (event) {
        display_event();
    });
    btn_country.addEventListener("click", function (event) {
        display_country();
    });
    btn_date.addEventListener("click", function (event) {
        display_date();
    });
    btn_discipline.addEventListener("click", function (event) {
        display_discipline();
    });
    btn_site.addEventListener("click", function (event) {
        display_site();
    });
    btn_record.addEventListener("click", function (event) {
        display_record();
    });
    search_input.addEventListener("keypress", function (event) {
        setTimeout(function () {
            // Code à exécuter après 1 milliseconde
            // Vérifiez si la touche enfoncée est "Enter" (code ASCII 13)
            if (event.keyCode === 13) {
                // Code à exécuter lorsque la touche "Entrée" est enfoncée
                display_event(search_input.value);
            }
        }, 1);
    });
}
// Écouteur d'événement DOMContentLoaded...
window.addEventListener("DOMContentLoaded", init);