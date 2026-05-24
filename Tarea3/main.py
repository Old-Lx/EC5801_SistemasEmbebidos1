import logging
import threading
import time
from typing import Callable, Any, Dict, Optional, ParamSpec

''' El inciso 1 se encuentra en logging_script.py'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # The default is NOTSET que implica herencia del logger padre

''' Inciso 2 - Hilos '''
''' 
    Para este inciso estoy usando:
    https://www.geeksforgeeks.org/python/multithreading-python-set-1/
    https://docs.python.org/3/library/threading.html
    https://realpython.com/intro-to-python-threading/
    https://sobolevn.me/2021/12/paramspec-guide

'''
params = ParamSpec("P")

class spider: # Se llama araña porque gestiona los hilos de manera natural
    # Diccionario para almacenar la información del hilo
    thread_dict: list[dict]
    # Hilos
    threads: list

    '''Inicializamos la clase '''
    def __init__(self, thread_num: int):
        self.thread_num = thread_num
    
    # Función para asignar
    def ThreadAllocate(self, function: Callable[params], *args, **kwargs):
        if (not(self.threads[self.thread_num - 1])):
            thread = threading.Thread(target=function, args=(*args,), kwargs={**kwargs})
            self.threads.append(thread)
        else:
            logger.info("No hay más hilos disponibles")