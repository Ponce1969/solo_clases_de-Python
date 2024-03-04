numeros = [1, 5, 2, 4, 3]
numeros.sort()#ordena la lista de menor a mayor
print(numeros)

numeros.sort(reverse=True)#ordena la lista de mayor a menor
print(numeros)

print(sorted(numeros))#ordena la lista de menor a mayor sin modificar la lista original, devuelve una lista nueva.
print(numeros)

usuarios = [
    [4, "Juan"],
    [2, "Pedro"], 
    [3, "Ana"],
    [1, "Maria"]
    
]   

usuarios.sort()#ordena la lista de menor a mayor por el primer elemento de cada lista
print(usuarios)

#cuando cambiamos el orden de los elementos de la lista, el ordenamiento cambia, para ordenar usamos una funcion.
usuarios = [
    ["Juan", 4],
    ["Pedro", 2],
    ["Ana" , 3],
    ["Maria" , 1]
    
]   

def ordena(elemento):
    return elemento[1]


usuarios.sort(key= ordena, reverse= True)#ordena la lista de menor a mayor por el primer elemento de cada lista
print(usuarios)
# esto se mejora haciendo funcion lambda en el proximo archivo.