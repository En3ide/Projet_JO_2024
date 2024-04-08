import subprocess, os

PATH = os.path.dirname(os.path.abspath(__file__)) + "/../" #repart du dossier racine du projet

def installer_requirements(fichier_requirements):
    """
    Installe les dépendances spécifiées dans un fichier requirements.txt
    Args:
    - fichier_requirements (str): Le chemin vers le fichier requirements.txt
    Returns:
    - bool: True si l'installation s'est déroulée avec succès, False sinon
    """
    try:
        subprocess.check_call(["python.exe", "-m", "pip", "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError as e:
        print("Python.exe introuvable !!!")
    try:
        subprocess.check_call(["pip", "install", "-r", fichier_requirements])
        print('[',datetime.now().time(),'] ', "Installation des dépendances réussie.")
        return True
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'installation des dépendances :", e)
        return False

installer_requirements(PATH + "Scraping/requirements.txt")