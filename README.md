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
   - [ ] Se debe crear tres clases distintas, una representara un disco duro, otra representara una memoria ram y por último una representara una memoria sram.
   - [ ] Para cada clase se tendrá un método de lectura y uno de escritura para un arreglo de tamaño N que representará su memoria interna. Se deberán modelar los retrasos de lectura y escritura para cada uno según su funcionamiento real (SRAM <- RAM <- Disco Duro).
   - [ ] Se deberán crear dos funciones polimórficas que deben aceptar las tres clases como si se tratase de un bus manejador de memoria.
   - [ ] Se tendrá un esquema de dos funciones una que se encarga de leer de una posición en memoria y otra que busca escribir en una posición de memoria.

#### Restricciones
  - No se puede usar IA de ningun tipo.
  - No pueden usar librerias que no vengan integrada en python (Nada que se instale con pip)
  - Fecha límite 15/05/2026


### Tarea 2
1. Manejo de Archivos
    - [ ] Haciendo uso del manejador de archivos integrado en Python deben generar dos funciones que permitan hacer lo siguiente:
        - [ ] Permitir Leer la información de un archivo sea de texto o binario.
        - [ ] Permitir Escribir la información a un archivo de texto o binario.
    - [ ] En base a estas funciones generar una clase que las contenga como método. Haciendo una verificación de que la ruta es valida utilizando la clase de tipo Path.

2. PyYAML
    - [ ] Usando la clase para el manejador de archivos como clase padre, generar una clase hija que herede sus métodos. Estos métodos se utilizarán como la base del stream de datos para las funciones de la librería PyYAML.
    - [ ] Generar un método para la clase hija que permita abrir un archivo, pasar su stream de datos a la librería PyYAML y de esa forma sintetizar el diccionario asociado al archivo ‘.yaml‘
    - [ ] El diccionario obtenido debe guardarse en un diccionario privado interno de la clase, siguiendo el siguiente esquema:
        {
            name:{
                path: str,
                data: dict
            },
            ...
        }
    - [ ] Para obtener el valor del archivo se debe tener una función de tipo GETTER, que permita obtener los diccionarios correspondientes basados en el nombre asignado.
    - [ ] Se debe tener un método adicional que permita modificar un diccionario ya pre-existente usando su nombre como identificador.
    - [ ] Por último, debe existir un método que permita guardar los valores modificados de el diccionario modificado en el disco haciendo uso de los streams de datos y la librería PyYAML.

3. Decoradores y Schemas
    - [ ] Se les proveerá un archivo de Python llamado schema_validator.py, el cual contiene una fabrica de decoradores llamado schema_validator. El uso de este decorador para cualquier función viene definido de la siguiente manera:
        @schema_validator(schema)
        def función_1(*args):
            …
    - [ ] Un Schema es un validador para asegurarse que los datos de un diccionario contienen los tipos asignados y así evitar cualquier error al momento de utilizar los mismos. Ejemplo de un Schema:
        {
            "key":int,
            "key_2":{
                "variable":str,
                "lista":list
            }
        }
    - [ ] El schema que deben validar viene dado por el archivo .yaml a generar. Para esta tarea en particular este archivo aceptara N cantidad de elementos con los siguientes ítems: nombre, altura, peso, edad, lista de habilidades, descripcion.

#### Restricciones
    - No se puede usar IA de ningún tipo.
    - No pueden usar librerías ajenas a PyYAML .
    - Fecha de entrega: 22/05/2026 

