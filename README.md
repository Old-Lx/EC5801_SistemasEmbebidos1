# EC5801_SistemasEmbebidos1
## Repositorio para la electiva EC5801 de la Universidad Simón Bolívar

### Tarea 1: 
1. Clases
    - [ ] Deben desarrollar una clase que describa una matriz de orden N x M, donde N representa las columnas y M las Filas.
    - [ ] Para esta clase haciendo uso de sustitución de operaciones por polimorfismo deben implementar las operaciones matriciales de suma, resta, multiplicación y deshabilitar la división.
    - [ ] Deben generar un método para imprimir las matrices en consola de manera organizada.

2. Herencia
    - [ ] Deben desarrollar una clase padre que permita describir un punto en 3 dimensiones (X, Y, Z).
    - [ ] La clase de tipo punto debe tener sus coordenadas (X, Y, Z) privadas y para poder obtenerlas desde la clase hija hace falta utilizar una función de tipo GETTER.
    - [ ] El punto debe tener operaciones como suma de un escalar, multiplicación por un escalar en uno o varios de sus ejes, estas operaciones son públicas.
    - [ ] La clase hijo que consumirá la clase Punto será un Vector cuyo origen siempre será 0 y debe tener un único método publico que permita calcular la magnitud del vector.
  
3. Polimorfismo
   - [ ] Se debe crear tres clases distintas, una representara un disco duro, otra representara una memoria ram y por último una representara una memoria sram.
   - [ ] Para cada clase se tendrá un método de lectura y uno de escritura para un arreglo de tamaño N que representará su memoria interna. Se deberán modelar los retrasos de lectura y escritura para cada uno según su funcionamiento real (SRAM <- RAM <- Disco Duro).
   - [ ] Se deberán crear dos funciones polimórficas que deben aceptar las tres clases como si se tratase de un bus manejador de memoria.
   - [ ] Se tendrá un esquema de dos funciones una que se encarga de leer de una posición en memoria y otra que busca escribir en una posición de memoria.

## Restricciones
  - No se puede usar IA de ningun tipo.
  - No pueden usar librerias que no vengan integrada en python (Nada que se instale con pip)
