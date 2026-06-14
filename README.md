# EC5801_SistemasEmbebidos1
## Repositorio para la electiva EC5801 de la Universidad Simón Bolívar

### Tarea 1: 
1. Clases
    - [x] Deben desarrollar una clase que describa una matriz de orden N x M, donde N representa las columnas y M las Filas.
    - [x] Para esta clase haciendo uso de sustitución de operaciones por polimorfismo deben implementar las operaciones matriciales de suma, resta, multiplicación y deshabilitar la división.
    - [x] Deben generar un método para imprimir las matrices en consola de manera organizada.

2. Herencia
    - [x] Deben desarrollar una clase padre que permita describir un punto en 3 dimensiones (X, Y, Z).
    - [x] La clase de tipo punto debe tener sus coordenadas (X, Y, Z) privadas y para poder obtenerlas desde la clase hija hace falta utilizar una función de tipo GETTER.
    - [x] El punto debe tener operaciones como suma de un escalar, multiplicación por un escalar en uno o varios de sus ejes, estas operaciones son públicas.
    - [x] La clase hijo que consumirá la clase Punto será un Vector cuyo origen siempre será 0 y debe tener un único método publico que permita calcular la magnitud del vector.
  
3. Polimorfismo
   - [x] Se debe crear tres clases distintas, una representara un disco duro, otra representara una memoria ram y por último una representara una memoria sram.
   - [x] Para cada clase se tendrá un método de lectura y uno de escritura para un arreglo de tamaño N que representará su memoria interna. Se deberán modelar los retrasos de lectura y escritura para cada uno según su funcionamiento real (SRAM <- RAM <- Disco Duro).
   - [x] Se deberán crear dos funciones polimórficas que deben aceptar las tres clases como si se tratase de un bus manejador de memoria.
   - [x] Se tendrá un esquema de dos funciones una que se encarga de leer de una posición en memoria y otra que busca escribir en una posición de memoria.

#### Restricciones
  - No se puede usar IA de ningun tipo.
  - No pueden usar librerias que no vengan integrada en python (Nada que se instale con pip)
  - Fecha límite 15/05/2026


### Tarea 2
1. Manejo de Archivos
    - [x] Haciendo uso del manejador de archivos integrado en Python deben generar dos funciones que permitan hacer lo siguiente:
        - [x] Permitir Leer la información de un archivo sea de texto o binario.
        - [x] Permitir Escribir la información a un archivo de texto o binario.
    - [x] En base a estas funciones generar una clase que las contenga como método. Haciendo una verificación de que la ruta es valida utilizando la clase de tipo Path.

2. PyYAML
    - [x] Usando la clase para el manejador de archivos como clase padre, generar una clase hija que herede sus métodos. Estos métodos se utilizarán como la base del stream de datos para las funciones de la librería PyYAML.
    - [x] Generar un método para la clase hija que permita abrir un archivo, pasar su stream de datos a la librería PyYAML y de esa forma sintetizar el diccionario asociado al archivo ‘.yaml‘
    - [x] El diccionario obtenido debe guardarse en un diccionario privado interno de la clase, siguiendo el siguiente esquema:
        {
            name:{
                path: str,
                data: dict
            },
            ...
        }
    - [x] Para obtener el valor del archivo se debe tener una función de tipo GETTER, que permita obtener los diccionarios correspondientes basados en el nombre asignado.
    - [x] Se debe tener un método adicional que permita modificar un diccionario ya pre-existente usando su nombre como identificador.
    - [x] Por último, debe existir un método que permita guardar los valores modificados de el diccionario modificado en el disco haciendo uso de los streams de datos y la librería PyYAML.

3. Decoradores y Schemas
    - [x] Se les proveerá un archivo de Python llamado schema_validator.py, el cual contiene una fabrica de decoradores llamado schema_validator. El uso de este decorador para cualquier función viene definido de la siguiente manera:
        @schema_validator(schema)
        def función_1(*args):
            …
    - [x] Un Schema es un validador para asegurarse que los datos de un diccionario contienen los tipos asignados y así evitar cualquier error al momento de utilizar los mismos. Ejemplo de un Schema:
        {
            "key":int,
            "key_2":{
                "variable":str,
                "lista":list
            }
        }
    - [x] El schema que deben validar viene dado por el archivo .yaml a generar. Para esta tarea en particular este archivo aceptara N cantidad de elementos con los siguientes ítems: nombre, altura, peso, edad, lista de habilidades, descripcion.

#### Restricciones
  - No se puede usar IA de ningún tipo.
  - No pueden usar librerías ajenas a PyYAML .
  - Fecha de entrega: 22/05/2026 (hubo una extensión hasta el 26)

### Tarea 3
0. Importación de Módulos Necesarios:
    ```Python
        import logging
        import threading
        import time
        from typing import Callable, Any, Dict, Optional
    ```
1. Registro de Eventos (Logging) en Python

    **Objetivo**: Familiarizarte con la biblioteca logging de Python, que viene instalada por defecto, y comprender sus diferentes niveles y modos de funcionamiento.

    - [x] Crea un script de Python (.py) dedicado exclusivamente a probar el módulo logging.
    - [x] Asegúrate de implementar y demostrar el uso de los distintos niveles de registro (o severidad) de mensajes: DEBUG, INFO, WARNING, y ERROR.

2. Gestión Avanzada de Hilos (Threading)

    **Objetivo**: Aplicar tus conocimientos sobre concurrencia para diseñar e implementar una clase robusta que actúe como un Gestor de Hilos utilizando la biblioteca threading.

    Requisitos de la Clase Gestora:

    - [x] Límite de Concurrencia: En la inicialización (init), la clase debe recibir un número entero que defina la cantidad total de hilos que pueden ejecutarse de manera concurrente, esto se conoce como Backlog.
    - [x] Registro de Hilos: Se debe implementar el método Thread_Allocate.
        - [x] Este método permitirá registrar un hilo, asignándole un nombre y el Callable (la función) que ejecutará.
        - [x] Debe aceptar argumentos posicionales y/o de palabra clave variádicos (*args y **kwargs) para la función a ejecutar.
        - [x] La información del hilo debe almacenarse en una estructura de datos interna (por ejemplo, un diccionario).
    - [x] Registro de Callbacks: Se debe implementar el método Thread_Callback_Register. Este método permitirá asociar funciones callback a los hilos ya registrados pero no en ejecución:
        - [x] Callback_Start: Función que se invoca justo al momento de iniciar la ejecución del hilo.
        - [x] Callback_End: Función que se invoca justo al momento de finalizar la ejecución del hilo.
    - [x] Inicio de Ejecución: Se debe implementar el método Thread_Start. Este método recibirá el nombre de un hilo registrado y comenzará su ejecución, respetando y gestionando los límites de concurrencia establecidos.

3. Sincronización con Eventos (Threading.Event)

    **Objetivo**: Ampliar la funcionalidad del Gestor de Hilos implementado, utilizando la clase Event de la biblioteca threading para garantizar la sincronización adecuada.

    Requisitos de Ampliación:

    - [x] Evento de Terminación: Integra un objeto Event de terminación para cada uno de los hilos gestionados.
    - [x] Finalización Síncrona: Después de iniciar la función principal, asegúrate de realizar el correspondiente join() para cada hilo.
    - [x] Propósito: Esta implementación busca hacer síncrona la finalización de la ejecución del hilo (a través del evento y el join()) antes de que el resto del código principal del programa continúe su flujo.
    - [x] Detención de Hilos por Nombre: Implementa el método Thread_End en el Gestor de Hilos. Este método debe recibir el nombre de un hilo y, utilizando el objeto Event de terminación, señalar la detención de la ejecución para que el hilo pueda finalizar de forma controlada.

#### Restricciones
    - Para el viernes 29/05/2026 

### Tarea 4 Comunicación Inter-Hilos con Colas Seguras
El objetivo de esta tarea es diseñar e implementar un sistema de mensajería robusto que permita el intercambio de datos entre hilos, de forma segura haciendo uso del módulo queue de Python.

1. Gestión de Colas
Deben desarrollar un gestor de colas como una clase central llamada Messages_Manager la cual debe permitir crear y eliminar colas en tiempo de ejecución.
    - [x] Creación de Colas: Implementar el método create. Este método debe generar una instancia de Queue recibiendo el máximo valor de parámetros que la cola podrá y asociarla a un identificador único (nombre) en un diccionario interno.
    - [x] Asociación de Callbacks: El método de creación debe permitir asignar una función con el tipo genérico Callable en un segundo diccionario interno, asociando por el identificador único (nombre).
    - [x] Eliminación Segura: Implementar el método delete para remover colas del sistema y liberar los recursos asociados, asegurando que posteriormente no se pueda acceder a los identificadores utilizados con anterioridad.

2. Sincronización y Exclusión Mutua (Mutex)
Se debe garantizar la integridad de las estructuras de datos compartidas dicts mediante el uso de bloqueos locks.
    - [x] Protección de Recursos: Usando los objetos de tipo Lock se debe asegurar que todas las operaciones de lectura y escritura sobre los diccionarios internos estén protegidas.

3. Intercambio de Mensajes
Se debe implementar los mecanismos de envío, recepción y procesamiento automático de mensajes de forma que pueda seguir el flujo principal de ejecución.
    - [x] Envío de Datos: Crear el método send que deposite información en una cola específica basándose en su nombre. Esta operación debe ser segura para hilos y bloqueante en caso de que la cola este totalmente llena.
    - [x] Recepción No Bloqueante: Implementar el método receive para extraer datos de una cola. Se debe configurar para que sea una operación de tipo no bloqueante, manejando adecuadamente los casos donde la cola esté vacía para evitar errores.

4. Polling
    - [x] Mecanismo de Polling: Desarrollar un método poll. Este método debe iterar sobre todas las colas activas y, si detecta datos entrantes debe recibirlos, para posteriormente ejecutar automáticamente el callback asociado a cada cola.

#### Restricciones
    - Para el viernes 12/06/2026
    - Prohibición de IA: No se permite el uso de herramientas de inteligencia artificial para la resolución de la tarea.
    - Librerías Permitidas: Solo se pueden utilizar módulos estándar de Python, específicamente logging, threading, y queue.
    - Registro de Eventos: El gestor debe incluir un sistema de logging interno que registre la creación, envío, recepción y errores del sistema.


### Prácticas con PIC16F13145
Durante clases presenciales desarrollamos distintas aplicaciones para el microcontrolador PIC16F13145, se adjuntará el código fuente escrito en C, sin embargo, fueron desarrollados con las extensiones de MPLAB disponibles para VS Code y necesitan ser configuradas para funcionar. Adjuntaré los `.hex` siempre que lo recuerde xd

1. BlinkingLED
    Es el típico proyecto de luz que parpadea, pero con un reloj HFSINTOC (no estoy seguro de cómo se escribía) a alta frecuencia y el código correspondiente, un poco más complejo que hacerlo en chips de desarrollo como ESP32 y Arduino, pero más sencillo que programar el PIC a más bajo nivel ya que estamos usando las herramientas de MPLAB

2. GPIO/Interruptions
    Proyecto que el toggle del Blinking LED y aprovecha las interrupciones del micro para generar un proyecto sencillo de interruptor de encendido y apagado, se usan conceptos de apuntadores a funciones para proceder, el código final es bastante sencillo.