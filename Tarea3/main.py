import logging
import threading
import time
from typing import Callable, Any, Dict, Optional, ParamSpec

''' El inciso 1 se encuentra en logging_script.py'''
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # The default is NOTSET que implica herencia del logger padre
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # Para configurar mejor el logger

''' Inciso 2 - Hilos '''
''' 
    Para este inciso estoy usando:
    https://www.geeksforgeeks.org/python/multithreading-python-set-1/
    https://docs.python.org/3/library/threading.html
    https://realpython.com/intro-to-python-threading/
    https://sobolevn.me/2021/12/paramspec-guide
    https://www.geeksforgeeks.org/python/synchronization-by-using-semaphore-in-python/
    https://www.geeksforgeeks.org/python/implement-inter-thread-communication-with-event-method-in-python/

'''
params = ParamSpec("P")

class spider: # Se llama araña porque gestiona los hilos de manera natural
    # Diccionario para almacenar la información del hilo
    thread_dicts: dict

    '''Inicializamos la clase '''
    def __init__(self, thread_num: int):
        self.thread_num = thread_num
        self.semaphore = threading.Semaphore(thread_num)
        self.thread_dicts = {}
    
    # Función para asignar un hilo para una tarea
    def ThreadAllocate(self, thread_name: str, function: Callable, *args, **kwargs):
        if (len(self.thread_dicts) < self.thread_num):
            thread = threading.Thread(target=function, args=(*args,), kwargs={**kwargs})
            thread.name = thread_name

            self.thread_dicts.update({
                    thread.name: {
                            'thread': thread,
                            'isDaemon': thread.daemon,
                            'isAlive': thread.is_alive(),
                            'ident': thread.ident,
                            'CallbackStart': Callable,
                            'CallbackEnd': Callable,
                            'event': threading.Event()
                        }
                }
            )
            logger.info(f"Hilo '{thread_name}' asignado correctamente.")
        else:
            logger.warning("No hay más hilos disponibles")
    
    def Thread_Callback_Register(self, thread_name: str, callback_start: Callable = lambda x: 0, callback_end: Callable = lambda x: 0):
        # Si el hilo no se está ejecutando, añadimos los callbacks
        if(not(self.thread_dicts[thread_name]['isAlive'])):
            self.thread_dicts[thread_name]['CallbackStart'] = callback_start
            self.thread_dicts[thread_name]['CallbackEnd'] = callback_end
            logger.info(f"Callbacks registrados para '{thread_name}'.")
        else:
            logger.info("El hilo ya se encuentra en ejecución")
    
    def Thread_Start(self, thread_name: str):
        self.semaphore.acquire()
        try:
            # Si hay callback se ejecuta
            if (self.thread_dicts[thread_name]['CallbackStart']):
                self.thread_dicts[thread_name]['CallbackStart']()
            self.thread_dicts[thread_name]['thread'].start()
        except:
            logger.debug("Algo falló al ejecutar el CallbackStart")

    def Thread_Sync(self, thread_name: str):
        try:
            self.thread_dicts[thread_name]['thread'].join()
        except:
            logger.error("No se pudo sincronizar con el hilo")
    
    def Thread_End(self, thread_name: str):
        time.sleep(3)
        try:
            self.thread_dicts[thread_name]['event'].set()
            # Si hay Callback, se ejecuta
            if (self.thread_dicts[thread_name]['CallbackEnd']):
                self.thread_dicts[thread_name]['CallbackEnd']()

            logger.info(f"Hilo '{thread_name}' finalizado y evento activado.")
        except:
            logger.info("No se detuvo el hilo correctamente")
        finally:
            self.semaphore.release()


''' Funciones de prueba '''

'''Función principal que ejecutará el hilo.'''
def task(nombre_tarea: str, tiempo_espera: int):
    logger.info(f"[{nombre_tarea}] Iniciando...")
    time.sleep(tiempo_espera)
    logger.info(f"[{nombre_tarea}] Terminado después de {tiempo_espera} segundos.")

def callback_start():
    logger.debug("CALLBACK: Empezando.")

def callback_end():
    logger.debug("CALLBACK: Finale.")

'''Función para probar la clase spider.'''
def test_spider():
    logger.info("¡Iniciando prueba!")
    
    spider_threading = spider(thread_num=2)
    
    spider_threading.ThreadAllocate(
        thread_name="hilo_1", 
        function=task, 
        nombre_tarea="Descarga de Datos", 
        tiempo_espera=2
    )
    
    spider_threading.Thread_Callback_Register(
        thread_name="hilo_1",
        callback_start=callback_start,
        callback_end=callback_end
    )
    
    spider_threading.Thread_Start("hilo_1")
    spider_threading.Thread_Sync("hilo_1")
    spider_threading.Thread_End("hilo_1")
    
    logger.info("Prueba terminada xoxo")

test_spider()