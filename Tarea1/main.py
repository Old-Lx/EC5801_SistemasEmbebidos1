

''' 
        EC5801 Sistemas Embebidos 1
        Tarea 1
'''

''' Para mayor información sobre clases consulté https://www.geeksforgeeks.org/python/python-classes-and-objects/ o si alguien prefiere complicarse
también está la documentación de python https://docs.python.org/3/tutorial/classes.html '''
class matrix:
    # Dimensiones
    n: float
    m: float

    # Matriz (Numpy tiene matrices mucho más eficientes)
    ''' Recordemos que la manera más fácil de implementar la matriz es mediante una lista de listas, configurando una lista para
     representar las filas y otra para las columnas, para mayor información sobre listas de listas https://www.geeksforgeeks.org/python/python-list-of-lists/ '''
    matrix_values: list

    ''' Inicializa una matriz de n filas y m columnas, se espera valores positivos de n y m '''
    def __init__(self, n: int, m: int):
        if (n > 0 and m > 0):
            self.n = n
            self.m = m
        else:
            print("Sólo se permiten enteros positivos (el cero no es positivo ni negativo)")
            return

        self.matrix_values = [[i for i in range(n)] for j in range(m)]
        
        ''' La inicializamos como matriz identidad '''
        for i in range(n):
            for j in range(m):
                if(i == j):
                    self.matrix_values[i][j] = 1
                else:
                    self.matrix_values[i][j] = 0

    ''' Evaluamos consistencia para suma y resta // Para conocer sobre métodos privados https://www.geeksforgeeks.org/python/private-methods-in-python/'''
    def __add_and_sub_consistency(self, matriz_2):
        if(self.n == matriz_2.n and self.m == matriz_2.m):
            return True
        
        print("Ambas matrices deben tener el mismo número de filas y columnas")
        return False

    ''' Hacemos function overload de las operaciones básicas, para mayor información sobre function overloading 
    https://www.geeksforgeeks.org/python/operator-overloading-in-python/ '''

    ''' Overload de suma '''
    def __add__(self, matriz_2):
        result_matrix = matrix(self.n, self.m)

        if(self.__add_and_sub_consistency(matriz_2)):
            for i in range(self.n):
                for j in range(self.m):
                    result_matrix.matrix_values[i][j] = self.matrix_values[i][j] + matriz_2.matrix_values[i][j]
        else:
            return

        return result_matrix
    
    ''' Overload de resta '''
    def __sub__(self, matriz_2):
        result_matrix = matrix(self.n, self.m)

        if(self.__add_and_sub_consistency(matriz_2)):
            for i in range(self.n):
                for j in range(self.m):
                    result_matrix.matrix_values[i][j] = self.matrix_values[i][j] - matriz_2.matrix_values[i][j]
        else:
            return

        return result_matrix
    
    ''' Overload de multiplicación '''
    def __mul__(self, elemento_2):
        result_matrix = matrix(self.n, self.m)

        if(self.m == elemento_2.n):
            for i in range(self.n):
                for j in range(elemento_2.m):
                    for k in range(self.m):
                        result_matrix.matrix_values[i][j] += self.matrix_values[i][k] * elemento_2.matrix_values[k][j]
        elif(isinstance(elemento_2, float) or isinstance(elemento_2, int)):
            for i in range(self.n):
                for j in range(self.m):
                    result_matrix.matrix_values[i][j] += self.matrix_values[i][k] * elemento_2


        else:
            return

        return result_matrix
    
    ''' Overload de división '''
    def __truediv__(self, matriz_2):
        print("No existe la división de matrices")
        return
    
    def __floordiv__(self, matriz_2):
        print("No existe la división de matrices")
        return
    
    ''' Overload potencia '''
    def __pow__(self, exp: int):
        result_matrix = matrix(self.n, self.m)

        if(exp > 0):
            for i in range(exp):
                result_matrix = result_matrix * result_matrix
        elif(not(exp)):
            result_matrix = matrix(self.n, self.m)
        else:
            print("La potencia negativa no ha sido definida para esta clase")

    ''' Transposición de la matriz '''
    def transpose(self):
        result_matrix = matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                result_matrix.matrix_values[j][i] = self.matrix_values[i][j]
        return result_matrix

    def print_matrix(self):
        for i in range(self.n):
            print(self.matrix_values[i])
        print("\n")

''' Para más información sobre herencia se puede consultar https://www.geeksforgeeks.org/python/inheritance-in-python/'''
class cartesian_point:
    def __init__(self, x: float, y: float, z: float):
        self.__point = [x, y, z]

    # getter del punto
    def get_point(self):
        return self.__point
    
    ''' Overload de suma '''
    def __add__(self, elemento_2):
        point = self.get_point()
        if(isinstance(elemento_2, (int, float))):
            point[0] += elemento_2
            point[1] += elemento_2
            point[2] += elemento_2
        elif(isinstance(elemento_2, cartesian_point)):
            point[0] += elemento_2[0]
            point[1] += elemento_2[1]
            point[2] += elemento_2[2]
        else:
            print("Esta suma no está definida")
        
        return point

    ''' Overload de multiplicación '''
    def __mul__(self, elemento_2):
        point = self.get_point()
        if(isinstance(elemento_2, (int, float))):
            point[0] *= elemento_2
            point[1] *= elemento_2
            point[2] *= elemento_2
        else:
            print("Esta multiplicación no está definida")
        
        return point
    
    ''' Acá se pone el num (número de dimensiones a ser multiplicadas), coord_1 y coord_2 para las coordenadas a multiplicar por el escalar, donde 3 implica no multiplicar
     ninguno de los ejes '''
    def special_mult(self, elemento_2, num = 3, coord_1 = 3, coord_2 = 3):
        match(num):
            case 3:
                return self * elemento_2
            case 2:
                point = self.get_point()
                if(not(coord_1 >= 3 or coord_2 >= 3 or coord_1 < 0 or coord_2 <0)):
                    point[coord_1] *= elemento_2
                    point[coord_2] *= elemento_2
                else:
                    print("Esta multiplicación no está definida actualmente")
            case 1:
                point = self.get_point()
                if(not(coord_1 >= 3 or coord_1 < 0)):
                    point[coord_1] *= elemento_2
                else:
                    print("Esta multiplicación no está definida actualmente")
            case _:
                print("Esta multiplicación no está definida actualmente")

class vector(cartesian_point):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def magnitude(self):
        point = self.get_point()
        mag = pow((point[0] ** 2) + (point[1] ** 2) + (point[2] ** 2), 0.5)
        return mag 


def main():
    matriz_1 = matrix(5, 5)
    matriz_2 = matrix(5, 5)
    matriz_2.matrix_values[0][1] = 2
    matriz_2.matrix_values[3][1] = 7
    matriz_2.matrix_values[1][1] = 9
    matriz_2.matrix_values[2][2] = 5
    matriz_2.matrix_values[4][1] = -7

    # Matriz identidad
    matriz_1.print_matrix()
    # Suma
    (matriz_1 + matriz_2).print_matrix()
    # Resta
    (matriz_1 - matriz_2).print_matrix()
    # Multiplicación
    (matriz_1 * matriz_2).print_matrix()
    # Transposed
    matriz_2.print_matrix()
    matriz_2.transpose().print_matrix()

    vec = vector(5, 4, 3)
    print(vec.magnitude())


main()
    