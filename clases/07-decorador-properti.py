class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
        
    @property
    def nombre(self):#metodo get para obtener el nombre del perro.
        print("pasando por getter")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre): #metodo set para cambiar el nombre del perro.
        print("pasando por setter")
        if nombre.strip():
           self.__nombre = nombre
        return self.__nombre
        
    def habla(self):
        print(f"{self.__nombre} dice: Guau!")
        
    @classmethod
    def factory(cls):
        return cls("Rocky", 2)
    
    
perro = Perro("Rocky", 2)
print(perro.nombre)