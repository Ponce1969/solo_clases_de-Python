#aprendemos listas en python
#las listas son un tipo de dato que nos permite almacenar varios valores
#y acceder a ellos por medio de un indice
#las listas se declaran con corchetes
#las listas pueden almacenar cualquier tipo de dato
numeros = [1,2,3]#lista de numeros
letras = ['a','b','c']#lista de letras
palabras = ['hola','mundo']#lista de palabras
booleanos = [True,False,True]#lista de booleanos
mixta = [1,'a',True]#lista mixta
#para acceder a un elemento de la lista se usa el indice
#los indices empiezan en 0
print(numeros[0])#imprime 1
print(letras[2])#imprime c
print(palabras[1])#imprime mundo
print(booleanos[0])#imprime True
print(mixta[2])#imprime True
matriz = [[1,2],[3,4]]#lista de listas
print(matriz[0])#imprime [1,2]
print(matriz[1])#imprime [3,4]
print(matriz[0][0])#imprime 1
print(matriz[0][1])#imprime 2
print(matriz[1][0])#imprime 3
print(matriz[1][1])#imprime 4
#para modificar un elemento de la lista se usa el indice
numeros[0] = 10
print(numeros[0])#imprime 10
#para agregar un elemento a la lista se usa el metodo append
numeros.append(4)
print(numeros)#imprime [10,2,3,4]
#para eliminar un elemento de la lista se usa el metodo pop
numeros.pop()
print(numeros)#imprime [10,2,3]
#para saber el tamaño de la lista se usa la funcion len
print(len(numeros))#imprime 3
#para saber si un elemento esta en la lista se usa la palabra reservada in
print(10 in numeros)#imprime True
print(4 in numeros)#imprime False
#para saber la posicion de un elemento en la lista se usa el metodo index
print(numeros.index(10))#imprime 0
print(numeros.index(2))#imprime 1
print(numeros.index(3))#imprime 2
alfanumerico = numeros + letras 
print(alfanumerico)#imprime [10,2,3,'a','b','c']
rango = list(range(10)) #imprime [0,1,2,3,4,5,6,7,8,9]
rango = list(range(1,11)) #imprime [1,2,3,4,5,6,7,8,9,10]
#lista de strings
chars = list('hola mundo') #imprime ['h','o','l','a',' ','m','u','n','d','o']


