from abc import ABC, abstractmethod
#Aprendo polimorfismo, es la capacidad de tomar varias formas,
# en este caso, la clase Model, puede tomar varias formas,
# en este caso, la clase Usuario, y la clase UsuarioAdministrador,
# ambas heredan de la clase Model, y ambas tienen el metodo guardar,
# pero cada una lo implementa de forma diferente.

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print('Guardando BBDD')
        

class Sesion(Model):
    def guardar(self):
        print('Guardando en sesion')
        

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario]) # Polimorfismo, la funcion guardar, puede recibir cualquier objeto que herede de Model