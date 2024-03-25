###################
# Script de scraping table Date_calendar
###################

##### Import #####
from bs4 import BeautifulSoup
import requests, ast, sqlite3, re, locale
from datetime import datetime
from create_list_Site import *
from get_id_table_selon_attr import *
from datetime import datetime

##### Code #####
main_url= "https://olympics.com/fr/paris-2024/sites"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
file_name = "transport.json"

def recup_to_register_athlete(event, athlete):
    