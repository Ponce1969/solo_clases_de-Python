from abc import ABC, abstractmethod

# Aprendo clases abstractas, Son clases que no se pueden instanciar, solo heredar.
class Model(ABC):
    @property
    @abstractmethod        
    def tabla(self):
        pass
    
    @abstractmethod        
    def guardar(self):
        pass
     
    @classmethod   
    def buscar_por_id(self, _id):
        print(f'Buscando por id {_id} en la tabla {self.tabla}')
        

class Usuario(Model):
    tabla = 'Usuarios'
    pass

    def guardar(self):
        print('Guardando usuario')
        

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)