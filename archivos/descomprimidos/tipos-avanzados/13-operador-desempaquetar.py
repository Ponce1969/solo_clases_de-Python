lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista) #desempaqueta la lista y la imprime

# combinar listas
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
combinada = [*lista1, *lista2]
print(combinada)

# combinar diccionarios
dic1 = {'a':1, 'b':2}
dic2 = {'c':3, 'd':4}
combinado = {**dic1, **dic2}
print(combinado)

# combinar diccionarios con listas
lista = [1, 2, 3, 4]
diccionario = {'a':1, 'b':2}
combinado = [*lista, *diccionario.values()]#
print(combinado)
#GitHub Copilot: El fragmento de código que has proporcionado es un ejemplo de cómo combinar una lista y un diccionario en Python utilizando el operador de desempaquetado `*`.

#Primero, se crea una lista llamada `lista` que contiene los números del 1 al 4. Luego, se crea un diccionario llamado `diccionario` con las claves 'a' y 'b' y los valores 1 y 2, respectivamente.

#El operador de desempaquetado `*` se utiliza para extraer los valores de la lista y del diccionario. En el caso del diccionario, se utiliza el método `values()` para obtener solo los valores del diccionario, ya que el operador de desempaquetado no funciona directamente con diccionarios.

#Finalmente, se crea una nueva lista llamada `combinado` que contiene los valores de la lista original y los valores del diccionario. Esta lista se imprime en la consola.



