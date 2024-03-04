# aprendemos el concepto de contenedores en python, ingresar productos dentro de una categoria

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f' Producto: {self.nombre} - Precio: {self.precio}'
    


class Categoria:
    productos = []
    
    def __init__(self, nombre, productos):
        self.nombre = nombre 
        self.productos = productos
        
        
    def agregar(self, producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for producto in self.productos:
            print(producto)
            
kayak = Producto('Kayak', 100)
bicicleta = Producto('Bicicleta', 200)
pelota = Producto('Pelota', 10)
surfboard = Producto('Surfboard', 50) 
            
deportes = Categoria('Deportes', [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
# de esta manera almacenamos objetos dentro de objetos,
# en este caso objetos de la clase Producto dentro de la clase Categoria  y luego los imprimimos