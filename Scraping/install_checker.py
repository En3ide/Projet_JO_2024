import importlib
import subprocess

def check_installation(module_name):
    try:
        importlib.import_module(module_name)
        print(f"Le module '{module_name}' est déjà installé.")
    except ImportError:
        print(f"Le module '{module_name}' n'est pas installé. Installion en cours...")
        subprocess.run(['pip', 'install', module_name])