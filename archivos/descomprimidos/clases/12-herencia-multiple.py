# aprendo herencia multiple.
class Animal:
    def comer(self):
        print('Comiendo')#las clases deben ser los mas chicas posibles, por eso no se debe poner metodos que no se usen.
        
    def dormir(self):
        print('Durmiendo')
        
    def pasear(self):
        print('paseando animales')  # en herencia multiple no debemos tener metodos con el mismo nombre en las clases que heredan  
        
class Perro:# con esto heredamos todos los metodos de la clase Animal
    def pasear(self):
        print('paseando al perro')# este es un metodo de animal
        


        
class Chanchito(Perro, Animal):# con esto heredamos todos los metodos de la clase Animal
    def programar(self):
        print('Programando')
        
        
Chanchito = Chanchito()
Chanchito.comer()
Chanchito.dormir()
Chanchito.programar()
Chanchito.pasear()
# con esto heredamos todos los metodos de la clase Animal y de la clase Perro