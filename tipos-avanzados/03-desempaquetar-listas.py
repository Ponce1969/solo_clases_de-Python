numeros = [1,2,3]

primero = numeros[0]
segundo = numeros[1]# esto es feo
tercero = numeros[2]


primero, segundo, tercero = numeros # esto es bonito
print(primero, segundo, tercero)

#como obtener el primer elemento de una lista
primero, *otros = numeros # esto es bonito enpaquetando la lista.
print(primero, otros)


