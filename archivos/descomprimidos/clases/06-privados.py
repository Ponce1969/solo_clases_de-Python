# aprendemos de las propiedades privadas de una clase.

class Perro:
   
    def __init__(self, nombre, edad):#constructor de la clase Perro , se ejecuta (self) al instanciar la clase.
        self.__nombre = nombre
        self.edad = edad #atributos de la clase Perro = propiedades de la clase Perro.
        
    
    def get_nombre(self):
        return self.__nombre 
    
    def set_nombre(self, nombre):#metodo set para cambiar el nombre del perro.
        self.__nombre = nombre
     
    def habla(self): #metodo de la clase Perro (habla).
        print(f"{self.__nombre} dice: Guau!")
        
    @classmethod
    def factory(cls):#metodo de la clase Perro (factory), se usa para crear objetos de la clase Perro (fabrica de perros)
        return cls("Rocky", 2)
    
    
perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())

# Accedemos a la propiedad privada __nombre de la clase Perro , pero no es recomendable hacerlo. con __dict__ podemos ver las propiedades de la clase Perro.
#print(perro1.__dict__)#no es recomendable acceder a las propiedades privadas de una clase.
print(perro1._Perro__nombre)#no es recomendable acceder a las propiedades privadas de una clase.
