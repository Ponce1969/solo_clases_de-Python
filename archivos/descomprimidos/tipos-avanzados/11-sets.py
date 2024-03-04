#sets significa grupo o conjunto. No tienen orden y no se pueden repetir elementos
primer = {1, 1, 2, 2, 3, 4}
primer.add(5)
primer.remove(1)
print(primer)

segundo = [1, 3, 6]
segundo = set(segundo)
print(segundo | primer) #union de conjuntos
print(segundo & primer) #interseccion de conjuntos
print(segundo - primer) #diferencia de conjuntos
print(segundo ^ primer) #diferencia simetrica de conjuntos
print(1 in segundo) #verificar si un elemento esta en el conjunto
print(1 not in segundo) #verificar si un elemento no esta en el conjunto
