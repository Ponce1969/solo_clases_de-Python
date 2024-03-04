# si ponemos aqui la variable saludo nos queda en contexto global y podemos acceder a ella desde cualquier parte del codigo.
#saludo = "Hola Mundo" # variable global quee es una mala practica.


# alcance de las funciones.
def saludar():
    saludo = "Hola Mundo"
    
    
    
def saludaChanchito():
    saludo = "Hola Chanchito"
    
    
    
print(saludo) # no podemos acceder a la variable saludo porque esta dentro de la funcion saludar,esta fuera de alcance.
# para acceder a la variable saludo tenemos que llamar a la funcion saludar o poner la variable saludo dentro de la funcion saludar.
# no podemos llamar desde afuera.

saludar() # llamamos a la funcion saludar.

