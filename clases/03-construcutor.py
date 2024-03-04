# aprendemos sobre el contructor de clases y sus propiedades.
class Perro:
    def __init__(self, nombre, edad):#constructor de la clase Perro , se ejecuta (self) al instanciar la clase.
        self.nombre = nombre
        self.edad = edad
        
        
    def habla(self):
        print(f"{self.nombre} dice: Guau!") #metodos de la clase Perro, accedemos a los atributos de la clase con self.

mi_perro = Perro("Rocco", 1) #self hace referencia a la instancia de la clase , en este caso mi_perro.
#mi_perro2 = Perro("Firulais")
#print(mi_perro.nombre)#Rocco , se imprime el atributo nombre del objeto mi_perro.
#print(mi_perro2.nombre)#Firulais , se imprime el atributo nombre del objeto mi_perro2.
mi_perro.habla()#Rocco dice: Guau! , se llama al metodo habla del objeto mi_perro.
