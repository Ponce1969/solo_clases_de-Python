# metodos de una clase

class Perro:
    patas = 4  #variable de clase , se puede acceder a ella sin instanciar la clase.
    def __init__(self, nombre, edad):#constructor de la clase Perro , se ejecuta (self) al instanciar la clase.
        self.nombre = nombre
        self.edad = edad #atributos de la clase Perro = propiedades de la clase Perro.
        
     
    @classmethod #decorador de la clase Perro (habla)., se usa para acceder a la variable de clase patas.   
    def habla(cls): #metodo de la clase Perro (habla).
        print("Guau!")
        
    @classmethod
    def factory(cls):#metodo de la clase Perro (factory), se usa para crear objetos de la clase Perro (fabrica de perros)
        return cls("Rocky", 2)
    
    
Perro.habla() #se llama al metodo de la clase Perro (habla).
perro1 = Perro("Rocco", 1)
perro2 = Perro("Rocky", 2)
perro3 = Perro.factory()#se llama al metodo de la clase Perro (factory) para crear un objeto de la clase Perro.
print(perro3.nombre, perro3.edad)


    
        
        