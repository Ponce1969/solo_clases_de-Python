# usamos en las funciones return para devolver un valor
def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total  #importante la identacion


c = resultado = suma(1, 4) # la primera vez que llamo suma es resultado es igual a 5 se lo asignamos a c.
d = resultado(c ,4)# la segunda vez que llamo suma es resultado es igual a 9 se lo asignamos a d.
print(d)# con print imprimimos el valor de d que es 9.