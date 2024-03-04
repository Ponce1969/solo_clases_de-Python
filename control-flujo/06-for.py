# aprendemos a usar el bucle for.

# for i in range(5): # range(5) -> 0,1,2,3,4
#     print(i)

for numero in range(5):
    print(numero)
    

# for en profundidad (iteradores)
# buscar un numero en una lista
buscar = 5
for numero in range(10):
    print(numero) # imprime los numeros del 0 al 9 para buscar el numero 5.
    if numero == buscar:
        print("numero encontrado",buscar)
        break # rompe el bucle, no sigue iterando.
else:
    print("numero no encontrado") # si no encuentra el numero, imprime esto.
                                # el else pertenece al for, no al if. sirve para nuestros algortimos.    
    

# iterables.
# son objetos que se pueden recorrer elemento a elemento.
# listas, tuplas, diccionarios, rangos, cadenas, etc.
# podemos recorrerlos con un for.
# podemos usar la funcion iter() para convertir un iterable en un iterador.
for usuario in ["juan","pedro","pablo","nicolas"]: # lista
    print(usuario)
    
    
    
# iterador string
for caracter in "hola mundo":
    print(caracter)