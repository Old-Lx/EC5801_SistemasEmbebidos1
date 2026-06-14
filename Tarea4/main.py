import logging
from threading import Lock
from queue import Queue
from typing import Callable
import sys

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # The default is NOTSET que implica herencia del logger padre
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # Para configurar mejor el logger

console_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler("app.log")

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Inciso 1 - Gestión de colas
''' 
    Para este inciso estoy documentándome con https://www.geeksforgeeks.org/python/queue-in-python/ y https://docs.python.org/3/library/queue.html
'''

class Messages_Manager:
    ''' Este es un diccionario de colas, el diccionario interno guardará el Queue en sí y el Callback de cada cola'''
    Q_dict: dict[str, Queue] = {}
    Callback_dict: dict[str, Callable] = {}

    def __init__(self):
        pass

    # Con esto asignamos el callback
    def attach_callback(self, q_id: str, callback: Callable):
        if (not(self.Q_dict[q_id].full())):
            self.Callback_dict[q_id] = callback

            logger.debug("Se acopló un callback a la cola " + str(q_id))
        else:
            logger.warning("No se logró acoplar el callback a la cola " + str(q_id))


    def creatio(self, size: int, callback: Callable = lambda x: print(x)):
        q_id = 'Queu' + str(len(self.Q_dict))
        
        try:
            self.Q_dict[q_id] = Queue(size)
            self.attach_callback(q_id, callback)

            logger.debug("Cola creada correctamente")
        except:
            logger.warning("Hubo un error creando la cola")

    def destructio(self, q_id: str):
        try:
            # Eliminamos todos los elementos de la cola
            for i in range(self.Q_dict[q_id].qsize()):
                self.Q_dict[q_id].get()
            del self.Q_dict[q_id] 
            del self.Callback_dict[q_id]

            logger.debug("Cola destruída")
        except:
            logging.warning("La cola no pudo destruírse correctamente")

    def read_q(self, q_id):
        try:
            Lock.acquire()
            current_Q = self.Q_dict[q_id]
            current_callback = self.Callback_dict[q_id]
            Lock.release()
            logger.debug("Cola y callback leídos")
        except:
            logger.warning("Hubo un problema que impidió leer la cola")

        return current_Q, current_callback
    
    def write_q(self, q_id, item_2_write):
        Lock.acquire()
        try:
            self.Q_dict[q_id].put(item_2_write)
            logger.debug("Se agregó un elemento a la Queue")
        except:
            logger.warning("Hubo un problema al intentar escribir en la cola")
        