def suma(*numeros):# *args parametros infinitos con * se le dice a python que va a recibir una cantidad infinita de argumentos.
    total = 0
    for numero in numeros:
        total += numero
    print(total)  #importante la identacion
    
    
    
suma(1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) # podemos pasarle la cantidad de argumentos que queramos.
# son iterables y se pueden recorrer con un for.


#keyword arguments.