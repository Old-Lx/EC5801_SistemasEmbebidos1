import logging
from threading import RLock
from queue import Queue
from typing import Callable
import sys

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # The default is NOTSET que implica herencia del logger padre
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # Para configurar mejor el logger

console_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler("app.log")

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.WARNING)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

lock = RLock()


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

    # Crea una cola
    def creatio(self, size: int, callback: Callable = lambda x: print(x)):
        q_id = 'Queue' + str(len(self.Q_dict))
        
        try:
            self.Q_dict[q_id] = Queue(size)
            self.attach_callback(q_id, callback)

            logger.debug("Cola creada correctamente")
        except:
            logger.warning("Hubo un error creando la cola")

    # Destruye una cola
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

    # Inciso 2
    def read_q(self, q_id: str):
        try:
            lock.acquire()
            current_Q = self.Q_dict[q_id]
            current_callback = self.Callback_dict[q_id]
            lock.release()
            logger.debug("Cola y callback leídos")
        except:
            logger.warning("Hubo un problema que impidió leer la cola")

        return current_Q, current_callback
    
    def write_q(self, q_id: str, item_2_write: any):
        lock.acquire()
        try:
            self.Q_dict[q_id].put(item_2_write)
            logger.debug("Se agregó un elemento a la Queue")
        except:
            logger.warning("Hubo un problema al intentar escribir en la cola")
        lock.release()
    
    # Inciso 3
    def send(self, q_id: str, data: any):
        lock.acquire()
        try:
            self.write_q(q_id, data)
            logger.debug("Se envió la data a la cola")
        except:
            logger.warning("No se pudo enviar data a la cola")
        lock.release()
    
    def receive(self, q_id: str):
        try:
             if self.Q_dict[q_id].empty():
                 raise ValueError("La cola está vacía")
             current_q, current_callback = self.read_q(q_id)
             logger.debug("Se recibió la información de la cola")
             return current_q.get()
        except ValueError:
            logger.warning("La cola está vacía")
        except:
            logger.warning("Ocurrió un error desconocido al recibir información de la cola")
    
    # Inciso 4
    def poll(self):
        for q_id, q in self.Q_dict.items():
            if not q.empty():
                data = self.receive(q_id)
                self.Callback_dict[q_id](data)

def generic_callback():
    print("Callback genérico")

def main():
    # Inicializo la clase
    manager = Messages_Manager()

    # Creo par de queues con sus respectivos callbacks
    manager.creatio(size=5, callback=generic_callback)
    manager.creatio(size=5, callback=lambda x: print(f"Lambda callback: {x}"))

    # Verifico el envío
    manager.send('Queu0', 'Mensaje A para Queu0')
    manager.send('Queu0', 'Mensaje B para Queu0')
    manager.send('Queu1', 'Mensaje para Queu1')

    # Probamos el poll también
    manager.poll()

    # Destruímos un callback a ver si funciona
    manager.destructio('Queu0')

if __name__ == "__main__":
    main()