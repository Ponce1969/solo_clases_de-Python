#creando clases
class Perro:
    def habla(self):# deja de ser funcion y se convierte en metodo al estar dentro de una clase , se le agrega self siempre.
        print("Guau")


mi_perro = Perro()# instanciando la clase Perro ,en el objeto mi_perro , se crea un objeto de la clase Perro.
#print(type(mi_perro))#<class '__main__.Perro'> , el objeto mi_perro es de la clase Perro.
mi_perro.habla()#Guau , se llama al metodo habla de la clase Perro.
print(isinstance(mi_perro,Perro))#True , mi_perro es una instancia de la clase Perro.
print(isinstance(mi_perro,int))#False , mi_perro no es una instancia de la clase int.
