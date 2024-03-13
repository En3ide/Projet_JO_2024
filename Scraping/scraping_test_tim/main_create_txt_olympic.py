from install_checker import check_installation

# Vérifier l'installation de requests
check_installation('requests')
# Vérifier l'installation de html2text
check_installation('html2text')
# Vérifier l'installation de bs4
check_installation('bs4')

from scraper import get_calendar_url, create_txt

if __name__ == "__main__":
    url = get_calendar_url()
    if url:
        create_txt(url)