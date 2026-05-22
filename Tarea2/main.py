import yaml
from pathlib import Path

''' Tarea 2 - EC3801 Sistemas Embebidos 1'''

# https://www.geeksforgeeks.org/python/file-handling-python/
# https://www.geeksforgeeks.org/python/python-open-function/

''' Inciso 1 '''
class file_manager:
    # Variable que guardará el lector//wrapper//buffer
    current_file: any # TextIOWrapper no está definido antes de la función open

    ''' Inicialización de la clase '''
    def __init__(self, file: Path):
        self.set_file(file)

    ''' Lectura del archivo '''
    def read_file(self):
        try:
            self.current_file.close()
            self.current_file = open(self.file_path, "r")
        except FileNotFoundError: # Si no consigue el archivo, lo crea
            open(self.file_path, "x")
            self.current_file = open(self.file_path, "r")
        finally:
            print("Operación de lectura realizada")

    ''' Lectura del archivo binario '''
    def read_bin_file(self):
        try:
            self.current_file.close()
            self.current_file = open(self.file_path, "rb")
        except FileNotFoundError:
            open(self.file_path, "xb")
            self.current_file = open(self.file_path, "rb")
        finally:
            print("Operación de lectura binaria realizada")

    ''' Escritura del archivo '''
    def write_file(self):
        try:
            self.current_file.close()
            self.current_file = open(self.file_path, "w")
        except FileNotFoundError:
            open(self.file_path, "x")
            self.current_file = open(self.file_path, "w")
        finally:
            print("Operación de escritura realizada")
    
    ''' Escritura del archivo binario '''
    def write_bin_file(self):
        try:
            self.current_file.close()
            self.current_file = open(self.file_path, "wb")
        except FileNotFoundError:
            open(self.file_path, "xb")
            self.current_file = open(self.file_path, "wb")
        finally:
            print("Operación de escritura binaria realizada")

    def close_file(self):
        self.current_file.close()
    
    def set_file(self, name: str):
        # Si el archivo es un path, proseguimos
        if (name.exists()):
            self.file_path = name
        else:
            print("La ruta '" + name + "' no es una ruta desconocida")


# https://pyyaml.org/wiki/PyYAMLDocumentation
# https://stackoverflow.com/questions/13019653/converting-yaml-file-to-python-dict
# https://www.geeksforgeeks.org/python/parse-a-yaml-file-in-python/

''' Inciso 2 '''
class yaml_manager(file_manager):
    __yaml_dict: dict # diccionario que se usará
    ''' Inicialización de la clase '''
    def __init__(self, file):
        super().__init__(file)

    ''' Genera un diccionario a partir de un stream de datos de un archivo cualquiera con la librería PyYAML '''
    def yaml_2_dict(self):
        self.__yaml_dict = yaml.load(self.current_file)

    ''' Toma el diccionario de la clase y lo convierte en archivo yaml está diseñado para que se cierre el archivo leído y se abra uno de escritura '''
    def dict_2_yaml(self, name):
        self.set_file(name)
        self.write_file()

        yaml.dump(self.__yaml_dict, self.current_file)
    
    def get_yaml_dict(self):
        return self.__yaml_dict

    def modify_yaml_dict(self, **kwargs):
        for (key, values) in kwargs.items():
            self.__yaml_dict[key] = values

