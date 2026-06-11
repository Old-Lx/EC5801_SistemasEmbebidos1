import logging
import threading
from queue import Queue
from typing import Callable


# Inciso 1 - Gestión de colas
''' 
    Para este inciso estoy documentándome con https://www.geeksforgeeks.org/python/queue-in-python/ y https://docs.python.org/3/library/queue.html
'''
class Messages_Manager:
    ''' Este es un diccionario de colas, el diccionario interno guardará el Queue en sí y el Callback de cada cola'''
    Q_list: dict[str, dict] = {}

    def __init__(self):
        pass

    def creatio(callback: Callable):
        j = 1

    def destructio():
        je = 0