import logging
import sys

''' 
    Para esta parte me guíe con:
    https://www.dash0.com/guides/logging-in-python  En esta página hacen una radiografía brutal for dummies casi
    https://www.geeksforgeeks.org/python/logging-in-python/
    https://docs.python.org/3/howto/logging.html
    
'''

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # The default is NOTSET que implica herencia del logger padre

'''
Estos son ejemplos de mensajes para cada nivel
logger.debug("a debug message")
logger.info("an info message")
logger.warning("a warning message")
logger.error("a error message")
logger.critical("a crit message")
'''

''' Para gestionar los loggers se usan handlers que permiten enviar un log dado a distintos lugares, si un logger no tiene
un handler configurado, se le asocia el handler padre más cercano (hasta llegar al root logger), si no hay handlers, Python
genera uno en sys.stderr que siempre estará en nivel WARNING '''

console_handler = logging.StreamHandler(stream=sys.stdout) # La mejor práctica es siempre configurar los handlers

# file_handler = logging.FileHandler("app.log") # Se puede generar un archivo de logs también
# logger.addHandler(file_handler)

''' A los handlers también se le puede asignar niveles que son independientes al nivel de su logger, así se tienen dos filtros, el primero
en el logger y el segundo en sus handlers '''
console_handler.setLevel(logging.DEBUG) # En este caso, tanto logger como handler tienen el mismo nivel, por lo que se obtiene desde debug para arriba
logger.addHandler(console_handler)

var = 7
logger.debug("El valor de var es " + str(var))

logger.info("El script está ejecutándose exitosamente")

logger.warning("¡Advertencia! Después de esta advertencia viene un error")

try:
    if 1 > 0:
        raise ValueError()
except ValueError:
    logging.error("Hubo un ValueError")

logger.critical("SE TERMINÓ EL SCRIPT, GRITO PORQUE ESTAMOS EN NIVEL CRÍTICO DE LOGGER")