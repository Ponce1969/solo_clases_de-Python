from pprint import pprint

#1. Eliminar los espacios en blanco de una cadena de caracteres.
#y devolver una lista con los caracteres restantes.
#2. Contar en un diccionario cuanto se repiten los caracteres de un string.
#3. Ordenar las llaves de un diccionario.
#por el valor que tienen y devpolver una lista que contiene tuplas[('a ', 3 ) ('b', 2), ('c', 4), ('d', 4)]
#de un listado de tuplas, devolver las tuplas tengan el mayor valor.
#[(' a', 3), ('b', 2), ('c', 4)] -> [('c', 4), ('d', 4)]
#5Crear un mensaje que diga: Los caracteres que mas se repiten   son: C y D.
#6. Juntar la solucion de los ejercicios anteriores, para encontrar los caracteres que mas se repiten en un string.

#1. Eliminar los espacios en blanco de una cadena de caracteres.
#y devolver una lista con los caracteres restantes.

lista = []
cadena = "Hola mundo"
cadena = cadena.replace(" ", "")
print(cadena)     

#devolver una lista con los caracteres restantes.
lista = list(cadena)
print(lista) #['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']

string = "Hola mundo"

def quita_espacios(texto):
    return [char for char in texto if char != " "]

sin_espacios = quita_espacios(string)
print(sin_espacios) #['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']

#2. Contar en un diccionario cuanto se repiten los caracteres de un string.
string = "Hola mundo"
def cuenta_caracteres(lista):
    caracteres = {}
    for char in lista:
        if char in caracteres:
            caracteres[char] += 1
        else:
            caracteres[char] = 1
    return caracteres

contados = cuenta_caracteres(lista)
pprint(contados, width=1) #{'H': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

#3. Ordenar las llaves de un diccionario.
#por el valor que tienen y devolver una lista que contiene tuplas y el mayor valor al principio.

def ordena_diccionario(diccionario):
    return sorted(diccionario.items(), key=lambda key: key[1], reverse=True)

ordenado = ordena_diccionario(contados)
print(ordenado) #[('H', 1), ('l', 1), ('a', 1), ('m', 1), ('u', 1), ('n', 1), ('d', 1), ('o', 2)]

#4. De un listado de tuplas, devolver las tuplas tengan el mayor valor.

def tuplas_mayor_valor(lista):
     maximo = lista[0][1]
     respuesta = {}
     for orden in lista:
         if maximo > orden[1]:
            break
         respuesta[orden[0]] = orden[1]
     return respuesta
 
mayores = tuplas_mayor_valor(ordenado)
print(mayores) #{'H': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

#5Crear un mensaje que diga: Los caracteres que mas se repiten con 4 repeticiones son: C y D.
def crea_mensaje(diccionario):
    mensaje = "Los caracteres que mas se repiten  son:  \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key}  con {valor} repeticiones \n"
    return mensaje
    
mensaje = crea_mensaje(mayores)
print(mensaje)