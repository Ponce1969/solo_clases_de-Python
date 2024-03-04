# Metodos magicos en python (metodos especiales)
# constructor de la clase Perro (init) = __init__
# destructor de la clase Perro (del) = __del__
# representacion de la clase Perro (repr) = __repr__
# representacion de la clase Perro (str) = __str__
# todos los metodos magicos en python empiezan y terminan con dos guiones bajos.
# aca podemos ver todos los metodos magicos en python: https://docs.python.org/3/reference/datamodel.html#special-method-names

class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Clase Perro: {self.__nombre} de {self.edad} años"
        
    def __repr__(self):
        return f"Perro({self.__nombre}, {self.edad})"
    
    
    # metodo destructor de la clase Perro
    def __del__(self):
        print(f"El perro {self.__nombre} ha sido eliminado")
    
perro = Perro("Rocky", 2)
#print(perro)
#texto = str(perro)
#print(texto)
del perro


#https://rszalski.github.io/magicmethods/#representations
