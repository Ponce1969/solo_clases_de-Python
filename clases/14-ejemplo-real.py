 # Ejemplo de la vida real con herencia en python

#metodo guardar
class Model():
    tabla = False
    def __init__(self):
        if not self.tabla:
            print('Error, no se ha definido la tabla')
            
            
    def guardar(self):
        print(f'Guardando  {self.tabla} en la base de datos')
     
    @classmethod   
    def buscar_por_id(self, _id):
        print(f'Buscando por id {_id} en la tabla {self.tabla}')
        

class Usuario(Model):
    tabla = 'Usuarios'
    pass

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)