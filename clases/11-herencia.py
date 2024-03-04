# Aprendemos sobre herencia en Python
"""
class Perro:
    def pasear(self):
        print('Paseando')
        
        
    def comer(self):# este metodo se va a sobreescribir en la clase Chanchito
        print('Comiendo')
        

class Chanchito:
    def comer(self):# este metodo se va a sobreescribir en la clase perro, por eso hay que usar herencia.
        print('Comiendo chanchito')
        
    def programar(self):
        print('Programando')
        
"""
class Animal:
    def comer(self):
        print('Comiendo')
        
    def dormir(self):
        print('Durmiendo')
        
class Perro(Animal):# con esto heredamos todos los metodos de la clase Animal
    def pasear(self):
        print('paseando')# este es un metodo de animal
        


        
class Chanchito(Animal):
    def programar(self):
        print('Programando')
        
        
        

chanchito = Chanchito()
chanchito.comer()
chanchito.dormir()
chanchito.programar()
