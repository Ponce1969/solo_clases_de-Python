#aprendo funciones 
#defino la funcion


def mi_funcion():
    print("Hola desde mi funcion")
#llamo a la funcion
mi_funcion()


#defino la funcion con parametros
def mi_funcion2(nombre, apellido):
    print("Hola desde mi funcion", nombre, apellido)
    
    
#llamo a la funcion
mi_funcion2("Juan", "Perez")



# defino la funcion con parametros
def hola(nombre, apellido):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido} ")# aca nombre es un parametro
    
    
hola("Gonzalo", "Ponce")  # aca Gonzalo es un argumento



# parametros por defecto
def hola2(nombre, apellido, edad=18):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido} ")# aca nombre es un parametro
    print(f"Tu edad es {edad}")
    
    

# parametros opcionales

def hola3(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido} ")# aca nombre es un parametro
    
    
    
hola3("Gonzalo", "Ponce")  # al pasarle un argumento a apellido toma el valor que le pasamos.
hola3("Chanchito") # al no pasarle un , segundo argumento a apellido toma el valor por defecto "Feliz".







#Argumentos nombrados
hola3(apellido = "Ponce",nombre ="Gonzalo") # al pasarle un nombre a los argumentos no importa el orden en que los pasemos.











