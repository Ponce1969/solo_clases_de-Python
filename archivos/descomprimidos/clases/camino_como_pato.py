class Usuario():
    def guardar(self):
        print('Guardando BBDD')
        
        
class Sesion():
    def guardar(self):
        print('Guardando en archivo')
        

def guardar(entidades): #aca le pasamos una lista de objetos
    for entidad in entidades:
        entidad.guardar()#aca llamamos al metodo guardar de cada objeto
        
        
        
usuario = Usuario()
sesion = Sesion()

guardar([usuario, sesion]) 

#python tiene tipado dinamico, no tipado fuerte
#Duck Typing: Si camina como pato, y hace cuac como pato, entonces es un pato (si tiene el metodo guardar, entonces es un objeto que hereda de Model)