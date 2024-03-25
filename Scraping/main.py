from multiprocessing import Process, Queue, Pool
from create_list_Site import *
from create_list_Athlete import *
from create_list_Country import *
from create_list_Discipline import *
from create_list_Record import *
from create_list_To_Serve import *
from create_list_Date_calendar import *

def test_1(parametre):
    result = parametre * 2
    return result

if __name__ == "__main__":
    with Pool() as pool:
        result1 = pool.apply(test_1, (5))
        result2 = pool.apply(test_1, (10))

"""if __name__ == "__main__":
    # Création d'un processus
    result_site = Queue()
    result_athlete = Queue()
    result_country = Queue()
    result_discipline = Queue()
    result_record = Queue()
    result_transport = Queue()
    result_calendar = Queue()
    site = multiprocessing.Process(target=recup_site, args=())
    athlete = multiprocessing.Process(target=recup_athlete, args=())
    country = multiprocessing.Process(target=recup_country, args=())
    discipline = multiprocessing.Process(target=recup_discipline, args=())
    record = multiprocessing.Process(target=recup_transp, args=())
    transport = multiprocessing.Process(target=recup_transp, args=())
    date_calendar = multiprocessing.Process(target=recup_date_calendar, args=())
    # Démarrage du processus
    site.start()
    athlete
    # Attente que le processus se termine
    site.join()

    print("Le processus principal a terminé.")"""