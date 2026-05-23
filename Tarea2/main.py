import yaml
from pathlib import Path
import schema_validator

''' Tarea 2 - EC3801 Sistemas Embebidos 1'''

# https://www.geeksforgeeks.org/python/file-handling-python/
# https://www.geeksforgeeks.org/python/python-open-function/

''' Inciso 1 Manejo de Archivos '''
class file_manager:
    # Variable que guardará el lector//wrapper//buffer
    current_file: any # TextIOWrapper no está definido antes de la función open

    ''' Inicialización de la clase '''
    def __init__(self, path: Path):
        self.set_file(path)

    ''' Lectura del archivo '''
    def read_file(self, name: str):
        try:
            self.current_file.close()
            self.current_file = open(str(self.file_path) + '\\' + name, "r")
        except AttributeError:
            try:
                self.current_file = open(str(self.file_path) + '\\' + name, "r")
            except FileNotFoundError: # Si no consigue el archivo, lo crea
                print('here')
                open(str(self.file_path) + '\\' + name, "x")
                self.current_file = open(str(self.file_path) + '\\' + name, "r")
        except FileNotFoundError: # Si no consigue el archivo, lo crea
            print('here')
            open(str(self.file_path) + '\\' + name, "x")
            self.current_file = open(str(self.file_path) + '\\' + name, "r")
        finally:
            print("Operación de lectura realizada")

    ''' Lectura del archivo binario '''
    def read_bin_file(self, name: str):
        try:
            self.current_file.close()
            self.current_file = open(str(self.file_path) + '\\' + name, "rb")
        except AttributeError:
            try:
                self.current_file = open(str(self.file_path) + '\\' + name, "rb")
            except FileNotFoundError: # Si no consigue el archivo, lo crea
                print('here')
                open(str(self.file_path) + '\\' + name, "x")
                self.current_file = open(str(self.file_path) + '\\' + name, "rb")
        except FileNotFoundError:
            open(str(self.file_path) + '\\' + name, "xb")
            self.current_file = open(str(self.file_path) + '\\' + name, "rb")
        finally:
            print("Operación de lectura binaria realizada")

    ''' Escritura del archivo '''
    def write_file(self, name: str):
        try:
            self.current_file.close()
            self.current_file = open(str(self.file_path) + '\\' + name, "w")
        except AttributeError:
            try:
                self.current_file = open(str(self.file_path) + '\\' + name, "w")
            except FileNotFoundError: # Si no consigue el archivo, lo crea
                print('here')
                open(str(self.file_path) + '\\' + name, "x")
                self.current_file = open(str(self.file_path) + '\\' + name, "w")
        except FileNotFoundError:
            open(str(self.file_path) + '\\' + name, "x")
            self.current_file = open(str(self.file_path) + '\\' + name, "w")
        finally:
            print("Operación de escritura realizada")
    
    ''' Escritura del archivo binario '''
    def write_bin_file(self, name: str):
        try:
            self.current_file.close()
            self.current_file = open(str(self.file_path) + '\\' + name, "wb")
        except AttributeError:
            try:
                self.current_file = open(str(self.file_path) + '\\' + name, "wb")
            except FileNotFoundError: # Si no consigue el archivo, lo crea
                print('here')
                open(str(self.file_path) + '\\' + name, "x")
                self.current_file = open(str(self.file_path) + '\\' + name, "wb")
        except FileNotFoundError:
            open(str(self.file_path) + '\\' + name, "xb")
            self.current_file = open(str(self.file_path) + '\\' + name, "wb")
        finally:
            print("Operación de escritura binaria realizada")

    def close_file(self):
        self.current_file.close()
    
    def set_file(self, path: Path):
        # Si el archivo es un path, proseguimos
        if (path.exists()):
            self.file_path = path
        else:
            print("La ruta '" + str(path) + "' es una ruta desconocida, así que se asignará el directorio actual")
            self.file_path = Path.cwd()


# https://pyyaml.org/wiki/PyYAMLDocumentation
# https://stackoverflow.com/questions/13019653/converting-yaml-file-to-python-dict
# https://www.geeksforgeeks.org/python/parse-a-yaml-file-in-python/

''' Inciso 2 PyYAML '''
class yaml_manager(file_manager):
    __yaml_dict: dict # diccionario que se usará
    ''' Inicialización de la clase '''
    def __init__(self, path: Path):
        super().__init__(path)

    ''' Genera un diccionario a partir de un stream de datos de un archivo cualquiera con la librería PyYAML '''
    def yaml_2_dict(self):
        self.__yaml_dict = yaml.safe_load(self.current_file)

    ''' Toma el diccionario de la clase y lo convierte en archivo yaml está diseñado para que se cierre el archivo leído y se abra uno de escritura '''
    def dict_2_yaml(self, name):
        self.set_file(name)
        self.write_file()

        yaml.safe_dump(self.__yaml_dict, self.current_file)
    
    def get_yaml_dict(self):
        return self.__yaml_dict

    def modify_yaml_dict(self, **kwargs):
        for (key, values) in kwargs.items():
            self.__yaml_dict[key] = values




''' Testing '''

# 1 Probaré escritura simple, pero lo demás funciona igual, confía
file_man = file_manager(Path('testing_file_man.txt'))
file_man.read_file('hola.txt')
print(file_man.current_file)
file_man.close_file()

# 2 Diccionarios
yaml_man = yaml_manager(Path.cwd())
yaml_man.read_file('hola.txt')
yaml_man.yaml_2_dict()
print(yaml_man.get_yaml_dict())

# 3 Schemas & Decorators
yaml_man2 = yaml_manager(Path.cwd())
yaml_man2.read_file('persona.txt')
yaml_man2.yaml_2_dict()
people = yaml_man2.get_yaml_dict()

''' Inciso 3 Decoradores y Schemas '''
@schema_validator.schema_validator({'nombre': [], 'altura': [], 'peso': [], 'edad': [], 'habilidades': [], 'descripcion': []})
def dict_2_yaml(content: dict, yaml_man=yaml_man2):
        yaml_man.write_file('persona_output.yaml') 

        yaml.safe_dump(content, yaml_man.current_file)
        yaml_man.close_file()

dict_2_yaml(people)