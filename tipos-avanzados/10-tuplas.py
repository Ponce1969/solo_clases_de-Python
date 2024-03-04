# las tuplas son inmutables, no se pueden modificar, ni agregar ni eliminar elementos.
numeros = (1, 2, 3) + (4, 5, 6) 
print(numeros) #resultado: (1, 2, 3, 4, 5, 6)

punto = tuple([3, 4])
print(punto) #resultado: (3, 4)

menos_numeros = numeros[ :2]
print(menos_numeros) #resultado: (1, 2)
primero, segundo, *otros = numeros
print(primero, segundo, otros) #resultado: 1 2 [3, 4, 5, 6]
for n in numeros:
    print(n) #resultado: 1, 2, 3, 4, 5, 6   
    


# las tuplas son mas rapidas que las listas, pero no se pueden modificar.
