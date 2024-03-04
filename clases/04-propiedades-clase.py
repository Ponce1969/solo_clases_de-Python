#propiedades de una clase
class Perro:
    patas = 4  #variable de clase , se puede acceder a ella sin instanciar la clase.
    def __init__(self, nombre, edad):#constructor de la clase Perro , se ejecuta (self) al instanciar la clase.
        self.nombre = nombre
        self.edad = edad #atributos de la clase Perro = propiedades de la clase Perro.
        
        
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
        
        
mi_perro = Perro("Rocco", 1)
print(mi_perro.patas)#4 , se imprime el atributo patas de la clase Perro.