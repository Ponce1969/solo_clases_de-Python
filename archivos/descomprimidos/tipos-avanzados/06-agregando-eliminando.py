mascotas = ['perro', 'gato', 'perico', 'pez', 'perro']
#agregar elementos a la lista
mascotas.append('hamster')#agrega al final de la lista
print(mascotas)

mascotas.insert(0, 'conejo')#agrega en el indice que le indiquemos
print(mascotas)

#eliminar elementos de la lista
mascotas.pop()#elimina el ultimo elemento de la lista
print(mascotas)

mascotas.pop(0)#elimina el elemento del indice que le indiquemos
print(mascotas)

mascotas.remove('perro')#elimina el elemento que le indiquemos
print(mascotas)

mascotas.clear()#elimina todos los elementos de la lista
print(mascotas)

del mascotas[0]#elimina el elemento del indice que le indiquemos
